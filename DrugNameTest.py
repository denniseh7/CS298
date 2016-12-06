
count=0

l1=""
l2=""
with open("Drug_Names.txt") as f:
    for line in f:
        name = line.strip()
        if count<199:
            l1+=(name+',')
        else:
            l2+=(name+',')

        count+=1

    l1+='\n'
    f = open('drugnamelist.txt', 'a')
    f.write(l1)  # python will convert \n to os.linesep
    f.write(l2)
    f.close()
