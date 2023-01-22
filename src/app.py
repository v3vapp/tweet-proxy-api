import tweepy
import config
if __name__ == '__main__':

    auth = tweepy.OAuthHandler(config.TWITTER_API_KEY,config.TWITTER_API_KEY_SECRET)
    auth.set_access_token(config.TWITTER_API_ACCESS_TOKEN,config.TWITTER_API_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Upload image
    media_1 = api.media_upload("./static/testimg.png")
    media_2 = api.media_upload("./static/testimg.png")
    media_3 = api.media_upload("./static/testimg.png")
    media_4 = api.media_upload("./static/testimg.png")


    list_img = [media_1.media_id,\
                media_2.media_id,\
                media_3.media_id,\
                media_4.media_id]

    message = "test img upload via api. multiple"

    post_result = api.update_status(status=message, media_ids=list_img)

