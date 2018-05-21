import tweepy
import random
from .get_lyric import get_lyrics
from .curiosidades import curioso
from .chistes import get_chistes
from .didyouk import dykList
#accesing twitter
def access_twitter():
	cosumer_key = 'Your consumer_key'
	cosumer_secret = 'Your consumer secret'

	access_token = 'Your Access token'
	access_token_secret = 'Your Access token secret '

	auth = tweepy.OAuthHandler(cosumer_key, cosumer_secret)
	auth.set_access_token(access_token,access_token_secret)

	api = tweepy.API(auth)

	return api

#update the status by selecting a function of curiosidades or paramore lyrics 
def update_status():
	
	tweet = access_twitter()	
	tweet_random = [get_lyrics(),curioso(),get_chistes(),dykList()]
	
	#random function select
	tweet_about_random = random.choice(tweet_random)
	tweet_about = tweet_about_random

	#add a hashtag on depending what the function was
	if tweet_about == tweet_random[0]:
		new_status = tweet_about
		tweet.update_status(new_status + '\n #BotTweet #paramore #music #up!  #tweepy')
		
		
	if tweet_about == tweet_random[1]:
		new_status = tweet_about
		tweet.update_status(new_status + '\n #BotTweet #curiosidades #SabiasQué #tweepy')
	
	if tweet_about == tweet_random[2]:
		new_status = tweet_about
		tweet.update_status(new_status + '\n bardos a (www.chistes12.com) #BotTweet #noentendi #reite #humornegro #humor #cambialacara #tweepy')

	if tweet_about == tweet_random[3]:
		new_status = tweet_about
		tweet.update_status('#DidYouKnow ' + new_status + '. \n #BotTweet #fact #dyk #fun #tweepy')

	#returning the frase about to twitt
	dic_tweet = {'tweet':new_status}
	return dic_tweet

#printing what the function return
if __name__ == '__main__':
	print(update_status())
	
