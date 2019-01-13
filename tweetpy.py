import tweepy 
  
 
consumer_key = "uV5llk4vadI7FuEJuWWhf3LwP" 
consumer_secret = "REXEkkBJtHxyDtvoPaq7wmGP5HrBoijLkHHnFNEpO31WDhVpdx"
access_key = "1083221054401757185-atuhYr2CfmTDZNNSoWsLnns2Qz5X4g"
access_secret = "3H7LwFoCbYr9JWMHWpmyGgF4xtkb3ZoP3kFr2O9d6GgdP"
  
def get_tweets(username): 
          
         
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
         
        auth.set_access_token(access_key, access_secret) 
  
         
        api = tweepy.API(auth) 
  
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username) 
  
        tmp=[]  
  
         
        tweets_for_csv = [tweet.text for tweet in tweets]   
        for j in tweets_for_csv: 
  
            tmp.append(j)  
  
        print(tmp) 
  
  
# Driver code 
if __name__ == '__main__': 
    get_tweets("@chetanbhagat")