import sys
import json
import re


def frequency(tweet_file):
	freq_dict = dict({})
	for feed in tweet_file:		
		try:
			feed_json = json.loads(feed)

			# process only ENGLISH tweets
			if(feed_json['user']['lang'] != 'en'):
				continue

			# process the tweet
			tweet = feed_json['text']
			tweet = tweet.lower()
			terms = tweet.split()

			for term in terms:
				term = re.sub('[@!#$%^&()-?,.]', '', term)
				# in dict or not?
				if(freq_dict.get(term) == None):
					freq_dict.update({term : 1})
				else:
					freq = freq_dict[term]
					freq_dict.update({term : freq + 1})
		except:
			continue		

	# get a count of all terms
	total_terms = 0
	for k, v in freq_dict.iteritems():
		total_terms += v

	# now output freq ratio for each term
	for k, v in freq_dict.iteritems():
		print '%s %.4f' % (k.encode('utf-8'), float(v) / float(total_terms))


def main():
	tweet_file = open(sys.argv[1])
	frequency(tweet_file)


if __name__ == '__main__':
	main()
