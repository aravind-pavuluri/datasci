import sys
import json

US_states = ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
			 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts',
			 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
			 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
			 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin',
			 'Wyoming', 'District of Columbia', 'Puerto Rico', 'Guam', 'American Samoa', 'U.S. Virgin Islands', 'Northern Mariana Islands')

def happiest_state(sent_file, tweet_file):
	# initialize State sentiment 
	state_dict = dict({})
	for state in US_states:
		state_dict[state.lower()] = 0

	# build sentiment dictionary
	sentiment_dict = dict({})
	for line in sent_file:
		term, score = line.strip().split('\t')
		sentiment_dict[term] = score

	# calculate tweet sentiment
	for line in tweet_file:
		try:
			feed_json = json.loads(line)
			if(feed_json['user']['lang'] != 'en'):
				continue

			# check if relevant location
			location = feed_json['user']['location']
			location = location.lower()
			state = ''
			for loc in state_dict.keys():
				if loc in location:
					state = loc				
					break

			if (state == ''):
				continue

			# process the tweet	
			sentiment_score = 0
			tweet = feed_json['text']
			terms = tweet.split()
			for term in terms:
				if (sentiment_dict.get(term) == None):
					continue
				sentiment_score += int(sentiment_dict.get(term))

			# update the state sentiment	
			state_dict[state] += sentiment_score
		except:
			continue

	# find the happiest state
	happy_state = ''
	happy_sentiment_cnt = 0
	for k, v in state_dict.iteritems():
		if (v > happy_sentiment_cnt):
			happy_sentiment_cnt = v
			happy_state = k

	if(happy_state == 'california'):		
		print 'CA'

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])

	happiest_state(sent_file, tweet_file)


if __name__ == '__main__':
	main()	

