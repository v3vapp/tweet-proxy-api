import tweepy
import config
if __name__ == '__main__':

    auth = tweepy.OAuthHandler(config.TWITTER_API_KEY,config.TWITTER_API_KEY_SECRET)

    auth.set_access_token(config.TWITTER_API_ACCESS_TOKEN,config.TWITTER_API_ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    message = "Hello World. This is a BOT."
    
    api.update_status(message)