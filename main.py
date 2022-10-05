from coinbase_api import api_pull_coinbase
from twitter_api import twitter_eth_pull, twitter_bitcoin_pull
import time


def main():

    api_pull_coinbase()
    twitter_eth_pull()
    twitter_bitcoin_pull()

if __name__ == '__main__':
    main()