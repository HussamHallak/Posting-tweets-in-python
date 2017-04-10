import tweepy

def get_api(config):
  auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
  auth.set_access_token(config['access_token'], config['access_token_secret'])
  return tweepy.API(auth)

def main():
  config = { 
    "consumer_key"        : "put_your_consumer_key_here",
    "consumer_secret"     : "put_your_consumer_secret_here",
    "access_token"        : "put_your_access_token_here",
    "access_token_secret" : "put_your_access_token_secret_here" 
    }

  api = get_api(config)
  tweet = "Put_your_tweet_here"
  status = api.update_status(status=tweet) 

if __name__ == "__main__":
  main()
