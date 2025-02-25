# Web3-Porfolio-Builder
Builds porfolio of cryptocurrency tokens with current price data and tokens held

## Why Web3 Porfolio Builder?

There are thousands of cryptocurrency tokens across several chains that a user must keep track of in order to track the total value of their porfolio.

Due to the decentralized nature of blockchain, it may be difficult for a new user to track their porfolio's performance across several chains.

Coinmarketcap.com allows users to create free API keys and pull price information up to 30 different tokens and has a powerful oracle that tracks the price of thousands of tokens across several liquidity pools from CEXs and DEXs.

This script allows the user to input the tickers of their tokens and tokens held to output the total value of their porfolio in the same spreadsheet.

## Features

- Fetches current price data and token metadata
- Filters spam tokens using key words
- Checks and writes target file in specified directory
- Outputs report in CSV format
- Allows user to select FIAT currency of their choice

## How to Use

- Install Python
- Create account with coinmarketcap and obtain your free API key
- Open config.ini and input your API keys
- Run the script twice.  Once to create the file, a second time to execute the script.

## Upcoming Features
- Note: This script is incomplete.  Uncommenting print commands allows you to see the structure of the json dumps from CMC.
- Correct array structure for price and ticker data
