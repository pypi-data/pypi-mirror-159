# EtherChainPy
A python interface to the ethereum blockchain explorer at https://www.etherscan.io

## Features
- Accounts - Address balance or balances.
- Contracts - ABIs and source codes
- Transactions - Status of contract execution, tx receipts.
- Blocks - Rewards by block number as well as its uncle, daily block count and rewards, daily avg block mining time, daily uncle count and rewards 
- Logs - Daily event logs from an address by optional block range
- Geth routines - Etherum JSON RPC calls. https://eth.wiki/json-rpc/API

## Installation
EtherChainPy is available for distribution as a pip packgage
```sh
pip install EtherChainPy
```

## Usage - Gas Price
```sh
e = EtherChainPy(apikey=environ['API_KEY_ETHERSCAN'], conversion_api_key=<from min-cryptocompare>)
print(e.geth.getGasPrice(to="WEI"))
11914121454

print(e.geth.getGasPrice(to="GWEI"))
11.914121454

print(e.geth.getGasPrice(to="ETH"))
1.3277968305e-08

print(e.geth.getGasPrice(to="ZAR"))
0.00027490572798988955
```

## Usage - Balances
```sh
e = EtherChainPy(apikey=environ['API_KEY_ETHERSCAN'], conversion_api_key=<from min-cryptocompare>)

Single address
balance = e.accounts.balance("0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae","latest")
gwei = balance.toGWEI()
eth  = balance.toETH()
zar  = balance.toZAR()
eur  = balance.toFIAT(value=eth, to="EUR")

print(gwei)
343270355903185.8

print(eth)
343270.35590318585

print(zar)
7121809477.702042

print(eur)
408656493.2956247


Multi addresses
balances = e.accounts.balances(["0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a","0x63a9975ba31b0b9626b34300f7f627147df1f526"],"latest")
gwei = balances.toGWEI()

print(gwei)
[{'account': '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a', 'balance': '40891626854930000000000', 'gwei': 40891626854930.0}, {'account': '0x63a9975ba31b0b9626b34300f7f627147df1f526', 'balance': '332567136222827062478', 'gwei': 332567136222.8271}]

eth  = balances.toETH()
print(eth)
[{'account': '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a', 'balance': '40891626854930000000000', 'eth': 40891.62685493}, {'account': '0x63a9975ba31b0b9626b34300f7f627147df1f526', 'balance': '332567136222827062478', 'eth': 332.56713622282706}]

zar = balances.toZAR()
print(zar)
[{'account': '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a', 'balance': '40891626854930000000000', 'eth': 40891.62685493, 'ZAR': 848376128.8616214}, {'account': '0x63a9975ba31b0b9626b34300f7f627147df1f526', 'balance': '332567136222827062478', 'eth': 332.56713622282706, 'ZAR': 6899750.421186819}]

cad = balances.toFIAT(value=eth, to="CAD")
print(cad)
[{'account': '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a', 'balance': '40891626854930000000000', 'eth': 40891.62685493, 'CAD': 64019113.1715413}, {'account': '0x63a9975ba31b0b9626b34300f7f627147df1f526', 'balance': '332567136222827062478', 'eth': 332.56713622282706, 'CAD': 520660.45712773356}]

```

## Usage - Transactions
```sh
Tx detail by HASH
e = EtherChainPy(apikey=environ['API_KEY_ETHERSCAN'], conversion_api_key=<from min-cryptocompare>)
b = e.geth.getTransactionByHash(txhash="0x111ae3586321f205dfc52c0a8143091973c0c9c9bdd4b3128cdf930dc5633ffc").json()
    
print(b)
{'jsonrpc': '2.0', 'id': 1, 'result': {'blockHash': '0x81f42ba1386c44b651e3a81887e4eede04195a278df5f83c57341b421581174f', 'blockNumber': '0xe708a4', 'from': '0x133050c897614fef58bc351eacd9b8efd9328e51', 'gas': '0x8617', 'gasPrice': '0x4dfa1ca9c', 'maxFeePerGas': '0x52cf9a3e5', 'maxPriorityFeePerGas': '0x59682f00', 'hash': '0x111ae3586321f205dfc52c0a8143091973c0c9c9bdd4b3128cdf930dc5633ffc', 'input': '0xe63d38ed000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000001000000000000000000000000b5b0b88bcc3dbfd0c39d1d35d22ef52890adbf1d0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000018de76816d80000', 'nonce': '0x0', 'to': '0xd152f549545093347a162dce210e7293f1452150', 'transactionIndex': '0x125', 'value': '0x18de76816d80000', 'type': '0x2', 'accessList': [], 'chainId': '0x1', 'v': '0x0', 'r': '0x2bd6d496695ba1f79700c95e4c6b326b9c20b3aca97e90d560bf476dd59ad787', 's': '0x5e2eacd9481b6bc44c89cef7039d54df494c4a9ac1c3f35fdbca9bdc4e83afd8'}}

```
