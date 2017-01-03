filename="drugtweet4.txt"
count=0

with open (filename, encoding='utf8', errors='ignore') as f:
    for line in f:
        tweet=line.lower()
        if not(tweet.startswith("rt")):
            f = open('nortfile4.txt', 'ab')
            f.write(tweet.encode('utf-8'))
            f.close()
            count+=1

print("TweetCount: " + str(count))