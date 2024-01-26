<<<<<<< HEAD
### 
I am Priya Patel, a current fintech student attending Rutgers University. I previously majored in business administration, and upon graduation I started working in supply chain for a paper bag manufacturer. I chose to pursue fintech because it is a growing industry with rising demand, and it offers a wide range of career paths. Also because it is a field I can continually be challenged in, and learn more as the field evolves in the future.

# FinTech Boot Camp
## Usage
### Updating Courseware
Before each class, pull in the latest courseware.
```
git pull coursware main
```

The repository is configured to have your origin be available on GitHub,
simply use `git push`.
```
git push origin
```

### Using Alpaca Markets
To allow for interacting with the Alpaca API, we're using the Alpaca Python SDK
within several of the classes notebooks.

When interacting with this repository, rebuild the exported Anaconda 
environment:
```
conda env create -f alpaca-environment.yml
```

When new packages are added, be sure to export the enviroment file:
```
conda env export | grep -v "^prefix: " > alpaca-environment.yml
```

Reference the installation instructions for Alpaca Markets in

## Unit 6: PyViz
### Helpful Links
=======
# Blockchain Terminology Guide

This guide provides an overview of key blockchain terminology that will help you understand the concepts discussed in this unit. 
>>>>>>> 4532ba98ae02936848d7de057ff885625038fd4e

* **Blockchain**:  A network of nodes, or machines, linked in a peer-to-peer fashion that facilitates transactions in a verifiable and permanent way. A blockchain network is also often called an **open distributed ledger**.

* **Node**: A single machine that contributes to the infrastructure of a blockchain network. Blockchain networks are composed of multiple nodes that are interconnected and exchange the latest blockchain data with each other. This way, each node is up-to-date with the latest verified transactions on the blockchain network.

* **Mining**: The process of adding verified transaction records to the current blockchain data. Miners act as separate nodes that are paid a fee to verify blockchain transactions by solving intense computations to finalize transactions.

* **Hash**: A product of a function that converts an input of letters and numbers into an encrypted output of a fixed length. Hashing is one way to enable security during message transmission when the message is intended for a particular recipient only. This ensures that the message has not been tampered with, as doing so would generate a new hash value different from the originating hash value.

* **Consensus algorithm**: A protocol used to verify the validity of transactions on a blockchain network. Because the blockchain network is decentralized, there is no central authority. Therefore, nodes within the blockchain network must be able to verify such transactions with certainty.

* **Proof of work (PoW)**: An asset-based consensus algorithm in which the model relies on producing a piece of data that is both resource (computation) and time intensive, but allows for others to verify the validity of the transaction. Proof of work is directly related to the blockchain mining concept in which miners solve intense computations to finalize transactions.

* **Proof of stake (PoS)**: A collateral-based consensus algorithm in which the model relies on transactional validators that are selected based on the amount of bitcoin or ether they hold. When they validate transactions, they put up a stake of their own bitcoin or ether and are rewarded (proportional to their stake) when a new block or transaction is added to the blockchain.


## Helpful Links

<details><summary>Blockchain</summary>

* <https://www.investopedia.com/terms/b/blockchain.asp>

</details>

<details><summary>Nodes</summary>

* <https://medium.com/coinmonks/blockchain-what-is-a-node-or-masternode-and-what-does-it-do-4d9a4200938f>

</details>

<details><summary>Hash</summary>

* <https://www.investopedia.com/terms/h/hash.asp>

</details>
<details><summary>Blockchain Mining</summary>

* <https://www.bitcoinmining.com/>

</details>
<details><summary>Consensus Algorithms</summary>

* <https://www.binance.vision/blockchain/what-is-a-blockchain-consensus-algorithm>

</details>
<details><summary>Proof of Authority</summary>

* <https://www.binance.vision/blockchain/proof-of-authority-explained>

</details>
<details><summary>Proof of Work</summary>

* <https://en.bitcoin.it/wiki/Proof_of_work>

</details>
<details><summary>Proof of Stake</summary>

* <https://www.investopedia.com/terms/p/proof-stake-pos.asp>

</details>

<<<<<<< HEAD
© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
=======
>>>>>>> 4532ba98ae02936848d7de057ff885625038fd4e
