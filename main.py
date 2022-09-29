from coinbase_api import api_pull_coinbase
from twitter import twitter_api_pull



def main():

    api_pull_coinbase()
    twitter_api_pull()


if __name__ == '__main__':
    main()    