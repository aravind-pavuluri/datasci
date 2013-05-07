import sys
import json
import re

def lines(fp):
    print str(len(fp.readlines()))

def termSentiment(sent_file, tweet_file):
	# from sentiment file build queryble sentiment directory
	sentiment_dict = dict({})
	for line in sent_file:
		items = line.split('\t')
		sentiment_dict.update({items[0] : items[1]})

	# build term sentiment dict from tweets 
	tweet_sentiment_dict = dict({})	

	for feed in tweet_file:
		feed_json = json.loads(feed)
		try:
			if(feed_json['user']['lang'] != 'en'):
				continue
			tweet = feed_json['text']
			terms = tweet.split()
			sentiment_score = 0
			for term in terms:
				term = re.sub('[!?@#$,&-]', '', term)
				term = term.lower()
				try:
					if(sentiment_dict.get(term) != None):
						sentiment_score += int(sentiment_dict.get(term))
				except:
					continue
			# print '<sentiment : ', sentiment_score, '>'		

			# update the term sentiment dictionary
			for term in terms:
				term = re.sub('[!@#$.,&-?]', '', term)
				term = term.lower()
				if(sentiment_dict.get(term) == None):
					if(tweet_sentiment_dict.get(term) == None):
						tweet_sentiment_dict.update({term : [sentiment_score, 1]})
					else:
						term_list = tweet_sentiment_dict.get(term)
						term_sentiment_score = term_list[0]
						term_freq = term_list[1]
						tweet_sentiment_dict.update({term : [term_sentiment_score + sentiment_score, term_freq + 1]})
		except:
			continue

	# print the term sentiment dictionary				
	for k, v in tweet_sentiment_dict.iteritems():
		term = k
		term_sentiment = v[0]
		term_freq = v[1]
		print '%s %.3f' %(term.encode('utf-8'), term_sentiment / term_freq)


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    lines(sent_file)
    lines(tweet_file)

    termSentiment(sent_file, tweet_file)


if __name__ == '__main__':
    main()
