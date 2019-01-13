import tweepy 

consumer_key= "uV5llk4vadI7FuEJuWWhf3LwP" # API key 
consumer_secret= "REXEkkBJtHxyDtvoPaq7wmGP5HrBoijLkHHnFNEpO31WDhVpdx" # API secret key 
access_key= "1083221054401757185-atuhYr2CfmTDZNNSoWsLnns2Qz5X4g"
access_secret= "3H7LwFoCbYr9JWMHWpmyGgF4xtkb3ZoP3kFr2O9d6GgdP"

def extract(username):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret) # Allows access through a customer id
	auth.set_access_token(access_key, access_secret) # Provides the access key for the customer id 
	api = tweepy.API(auth) # Calls the API 
	
	#The number of tweets to be extracted 
	number_of_tweets=200
	tweets = api.user_timeline(screen_name=username)#.user_timeline() returns a list of status' of the id being parsed 
	arr=[] 

	tweets_file=[tweet.text for tweet in tweets] #extracting the text from the tweets list and putting it in a file 
	for j in tweets_file : 
		arr.append(j) #appending all the extracted information in an array for future use 
	
	print(arr)

	if __name__ == "__main__" :
		extract("Insert_twitter_handle_here")
