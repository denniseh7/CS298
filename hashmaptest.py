#Dennis Hsu

import re
import collections


with open('metamapoutputtest1.txt') as f:
    for line in f:


        ses={}
        ses2={}
        keyval=line.split(":",1)
        name=keyval[0]

        fullhashstr=keyval[1]

        hashstr=re.sub('}', '', fullhashstr)
        hashstr=re.sub('{', '', hashstr)


        hashlist=hashstr.split(',')

        print("hello")
        #print(hashlist)

        for pair in hashlist:
            kvpair=pair.split("=")

            if len(kvpair) == 2:
                key=kvpair[0].strip()
                val=int(kvpair[1])
                ses[key]=val


        print(name)
        #print("done")
        #soses = collections.OrderedDict(sorted(ses.items(),key=ses.get, reverse=True))

        for k in sorted(ses, key=ses.get, reverse=True):
            print(k +' '+ str(ses[k]))
            g = open('xanaxlist.txt', 'a')
            g.write(k + '\n')
            g.close()


        #soses=sorted(ses.items(), key=ses.get, reverse=True)
        #print(soses)

        break


