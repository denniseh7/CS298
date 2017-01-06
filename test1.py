
count=0
count2=0
count3=0
count4=0
count5=0
with open('predictedcombined2.txt') as f:
    for line in f:
        if "xanax" in line:
            count+=1

        if "adderall" in line:
            count2+=1

        if "benadryl" in line:
            count3+=1


        if "vyvanse" in line:
            count4+=1

        if "gabapentin" in line:
            count5+=1

print("xanax " + str(count))
print("adderall " + str(count2))
print("benadryl " + str(count3))
print("vyvanse " + str(count4))
print("gabapentin " + str(count5))