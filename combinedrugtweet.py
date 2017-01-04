filename="drugtweet13.txt"
count=0

with open (filename, encoding='utf8', errors='ignore') as f:
    for line in f:
        tweet=line.lower()
        f = open('combinedtweet1.txt', 'ab')
        f.write(tweet.encode('utf-8'))
        f.close()
        count += 1

print(count)