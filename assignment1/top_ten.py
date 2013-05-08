import sys
import json
import operator

def top_ten(tweet_file):
	# create a hash tag dict
	hashtag_dict = dict({})	

	for line in tweet_file:
		feed_json = json.loads(line)
		try:
			if(feed_json['user']['lang'] != 'en'):
				continue

			hashtags = feed_json['entities']['hashtags']			
			tag = hashtags[0]['text'].lower()
			if(hashtag_dict.get(tag) == None):
				hashtag_dict[tag] = 1
			else:
				tag_cnt = int(hashtag_dict.get(tag))
				hashtag_dict[tag] = tag_cnt + 1	
		except:
			continue

	tag_sorted = sorted(hashtag_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
	count = 0
	for tag in tag_sorted:
		print '%s %.1f' % (tag[0], tag[1])
		count += 1
		if(count > 10):
			break
	
def main():
	tweet_file = open(sys.argv[1])
	top_ten(tweet_file)


if __name__ == '__main__':
	main()	

