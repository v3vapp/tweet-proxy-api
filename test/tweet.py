import tweepy
import config


auth = tweepy.OAuthHandler(config.TWITTER_API_KEY,config.TWITTER_API_KEY_SECRET)

auth.set_access_token(config.TWITTER_API_ACCESS_TOKEN,config.TWITTER_API_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


# Upload image
media = api.media_upload("/home/daiki/Dropbox/v3v/tweet-proxy-api/static/testimg.png")

# Post tweet with image
tweet = "test img upload via api"
post_result = api.update_status(status=tweet, media_ids=[media.media_id])
