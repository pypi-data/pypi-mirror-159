# -*- coding: UTF-8 -*-
from decimal import Decimal, getcontext
from functools import wraps
from typing import Optional, Callable, Any

import bitcoinlib
from bitcoinlib.wallets import Wallet, wallet_delete, WalletError, WalletTransaction
from bitcoinlib.mnemonic import Mnemonic
from bitcoinlib.keys import HDKey
from myloguru.my_loguru import get_logger
from crypto_wallet import WalletExists, PassphraseError

getcontext().prec = 5
logger = get_logger(level=20)


def load_wallet_data(func: Callable) -> Callable:
    """Decorator for create wallet inside instance if wallet is not exists"""

    @wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        name: str = func.__name__
        if args and hasattr(args[0].__class__, name):
            wallet: 'Wallet' = getattr(args[0], "_wallet")
            if not wallet:
                await args[0].load_data()
            return await func(*args, **kwargs)
        return await func(*args, **kwargs)

    return wrapper


class CryptoWallet:
    """
    Crypto wallet manager.
    Create or get crypto wallet by name and passphrase.
    Get balance, address and wallet info.
    Transfer money to another wallet by address.

    Attributes
        wallet_name: str - Wallet name

        passphrase: str = ''
            Passphrase for get wallet

        main_wallet: str = ''
            Wallet address for transfer money in send_money method

        network: str = 'litecoin'
            Crypto network

        fee: Decimal = Decimal(0.0015)
            Fee for transfer

    Methods
        get_wallet

        get_wallet_address

        get_wallet_balance

        get_wallet_balance_str

        send_money

        info
    """

    def __init__(
            self,
            wallet_name: str,
            passphrase: str = '',
            main_wallet: str = '',
            network: str = 'litecoin',
            fee: Decimal = Decimal(0.0015),
    ) -> None:
        self._network = network
        self._wallet_name: str = wallet_name
        self._passphrase: str = passphrase
        self._wallet: Optional['Wallet'] = None
        self._wallet_id: int = 0
        self._main_wallet: str = main_wallet
        self._fee: Decimal = fee

    async def get_wallet(self) -> 'CryptoWallet':
        return await self._get_or_create_wallet()

    async def _create_new_wallet(self) -> 'CryptoWallet':
        passphrase: str = Mnemonic().generate()
        try:
            self._wallet: 'Wallet' = Wallet.create(
                self._wallet_name, keys=self._passphrase, network=self._network)
            logger.debug(f"Wallet created with name: [{self._wallet_name}]")
            self._passphrase = passphrase
        except WalletError:
            logger.debug(f"Wallet with name [{self._wallet_name}] already exists.")
            raise WalletExists
        return self

    def _get_fee(self) -> 'Decimal':
        return self.fee

    async def load_data(self) -> 'CryptoWallet':
        """Returns CryptoWallet instance contains Wallet data loaded from passphrase

        :return Updated CryptoWallet instance
        """

        wallet: 'Wallet' = await self._get_wallet_from_passphrase()
        self._wallet = wallet
        self._wallet_id = wallet.wallet_id
        logger.debug(f"Wallet with name {self._wallet_name}\tWallet_id: {self._wallet_id}")

        return self

    async def _get_or_create_wallet(self) -> 'CryptoWallet':
        await self._create_new_wallet()
        if self._wallet:
            return self
        return await self.load_data()

    async def _get_wallet_from_passphrase(self) -> Wallet:
        if not self._passphrase:
            raise PassphraseError
        try:
            hd_key: 'HDKey' = HDKey.from_passphrase(
                passphrase=self._passphrase, network=self._network)
            return Wallet(wallet=self._wallet_name, main_key_object=hd_key.private_hex)
        except WalletError as err:
            logger.error(f"Passphrase error: {err}")
            raise PassphraseError

    @load_wallet_data
    async def get_wallet_address(self) -> str:
        """Returns wallet address"""

        address = self._wallet.get_key().address
        logger.debug(f"Wallet with name: {self._wallet_name}\tAddress: {address}")

        return address

    @load_wallet_data
    async def get_wallet_balance(self) -> 'Decimal':
        """Returns balance in integer format

        Example: 109531
        """

        self._wallet.scan()
        balance: 'Decimal' = Decimal(self._wallet.balance(network=self._network))
        logger.debug(f"Wallet with name: {self._wallet_name}\tBalance: {balance}")

        return balance

    @load_wallet_data
    async def get_wallet_balance_str(self) -> str:
        """Returns balance in string format.

        Example: '0.0001235 LTC'
        """
        self._wallet.scan()
        balance: str = self._wallet.balance(network=self._network, as_string=True)

        logger.debug(f"Wallet with name: {self._wallet_name}\tBalance: {balance}")
        return balance

    @load_wallet_data
    async def info(self) -> dict:
        """
        Returns dictionary wallet data:

        {
            "wallet_id": wallet_id:, - int

            "name": wallet_name, - str

            "passphrase": wallet_passphrase, - str

            "address": wallet_address, - str

            "main_network": wallet_main_network, - str

            "main_balance": wallet_main_balance, - int

            "main_balance_str": wallet_main_balance_str, - str

        }

        :return: Dictionary wallet data
        """

        wallet_data: dict = self._wallet.as_dict()
        address: str = await self.get_wallet_address()
        data_for_save = {
            "wallet_id": wallet_data.get("wallet_id"),
            "name": wallet_data.get("name"),
            "passphrase": self._passphrase,
            "address": address,
            "main_network": wallet_data.get("main_network"),
            "main_balance": wallet_data.get("main_balance"),
            "main_balance_str": wallet_data.get("main_balance_str")
        }
        return data_for_save

    async def _cost_with_fee(self, amount: str) -> str:
        """Returns price in string format with fee.

        Example: '0.0001235 LTC'
        """
        cost, currency = amount.split()
        cost: 'Decimal' = Decimal(cost) - self._get_fee()
        if cost < 0:
            cost = Decimal(0)
        cost: str = str(cost) + ' ' + currency

        return cost

    @load_wallet_data
    async def send_money(self, amount: str, address: str) -> dict:
        """Sends money to address, by default all money will be sent

        :param amount: String format. For example: '0.0015544 LTC'
        :param address: String target address
        :return: bool: Success result
        """

        amount: str = await self._cost_with_fee(amount)
        try:
            transaction: 'WalletTransaction' = await self.__send_money(
                amount=amount, address=address)
            result: dict = transaction.as_dict()
            logger.info(f"Status: {transaction.status}"
                        f"\nResult: {result}")

            return result
        except WalletError as err:
            logger.error(
                f"Send money error: "
                f"\nWallet name: {self._wallet_name}\tSending: {amount} to {self._main_wallet}"
                f"\nError: {err}")
        except bitcoinlib.encoding.EncodingError as err:
            logger.error(f"MAIN WALLET ERROR: {err}")
        except bitcoinlib.transactions.TransactionError as err:
            logger.error(f"Transaction ERROR: {err}")

        return {}

    async def __send_money(self, amount: str, address: str) -> WalletTransaction:
        logger.debug(f"Wallet name: {self._wallet_name}\tSending: {amount} to {self._main_wallet}")
        return self._wallet.send_to(address, amount, offline=False)

    async def delete_wallet(self):
        try:
            if wallet_delete(self._wallet_name):
                logger.debug(f"Wallet name: {self._wallet_name} deleted")
                return True
        except WalletError as err:
            logger.debug(f"Wallet name: {self._wallet_name} delete error: {err}")
        return False

    @property
    def wallet_id(self) -> int:
        return self._wallet_id

    @property
    def wallet(self) -> 'Wallet':
        return self._wallet

    @property
    def fee(self) -> Decimal:
        return Decimal(self._fee)

    @property
    def passphrase(self) -> str:
        return self._passphrase

    @property
    def main_wallet(self) -> str:
        return self._main_wallet

    @main_wallet.setter
    def main_wallet(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f"Main wallet must be str, {type(value)} got.")
        self._main_wallet = value
