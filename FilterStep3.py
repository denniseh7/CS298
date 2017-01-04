count=0
with open('noduprtfilecombined1.txt') as f:
    for line in f:
        line=line.lower()
        if "lithium" not in line:
            if "testosterone" not in line:
                if "botox" not in line:
                    if "viagra" not in line:
                        if "sonata" not in line:
                            if "senna" not in line:
                                if not (("fish" in line) and ("oil" in line)):
                                    f = open('noduplithiumfilecombined1.txt', 'a')
                                    f.write(line)
                                    f.close()
                                    count+=1

print(count)