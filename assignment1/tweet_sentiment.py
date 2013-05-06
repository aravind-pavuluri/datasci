import sys
import json

def sentimentAnalysis(sent_file, tweet_file):
	# build a dict of sentiments
	sentiment_dict = dict({ })
	for line in sent_file:
		# split string for word (items[0]) and sentiment value (items[1])
		items = line.split('\t')
		# build a sentiment dictionary we can use for tweet lookup
		sentiment_dict.update({items[0] : items[1]})
	
	# read in each tweet feed line in the file	
	for feed in tweet_file:
		feed_json = json.loads(feed)
		# get at the tweet
		try:
			tweet = feed_json['text']
			sentiment_score = 0
			# parse the words in the tweet
			words = tweet.split()
			for word in words:
				try:
					# check is sentiment word
					if(sentiment_dict[word] != None):
						sentiment_score += int(sentiment_dict[word])
				except:
					pass
			print '%d' %(sentiment_score)	 
		except :
			pass
		

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sentimentAnalysis(sent_file, tweet_file)

    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()

