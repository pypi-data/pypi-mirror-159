from setuptools import setup, find_packages
exec(open("src/crypto_wallet/_resources.py").read())
setup(
    name=__package_name__,
    version=__version__,
    author=__author__,
    author_email='battenetciz@gmail.com',
    description='My Crypto Wallet library',
    install_requires=[
        'bitcoinlib==0.6.4',
        'myloguru-deskent==0.0.12'
    ],
    scripts=['src/crypto_wallet/wallet.py'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/Deskent/my_cryptowallet",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
)
