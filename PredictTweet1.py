from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder

from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,VotingClassifier

from sklearn.model_selection import cross_val_score
import numpy as np
import random

#drug list
namelist=["abilify","acetaminophen","acyclovir","adderall","albuterol","aleve","allopurinol","alprazolam","ambien","amiodarone","amitriptyline","amlodipine","amoxicillin","aricept","aspirin","atenolol","ativan","atorvastatin","augmentin","azithromycin","baclofen","bactrim","bactroban","belsomra","benadryl","benicar","biaxin","bisoprolol","boniva","boniva","breo ellipta","brilinta","brovana","bupropion","buspar","buspirone","butrans","bydureon","bystolic","cardizem","carvedilol","celebrex","celexa","cephalexin","cetirizine","cialis","cipro","ciprofloxacin","citalopram","claritin","clindamycin","clonazepam","clonidine","coreg","coumadin","cozaar","crestor","cyclobenzaprine","cymbalta","demerol","depakote","detrol","dexamethasone","dextromethorphan","diazepam","diclofenac","diflucan","digoxin","dilantin","dilaudid","diltiazem","diovan","diphenhydramine","ditropan","doxazosin","doxycycline","dulera","duoneb","dyazide","effexor","effient","elavil","eligard","eliquis","enalapril","enbrel","endocet","entresto","epipen","epogen","erythromycin","estrace","estradiol","etodolac","evista","excedrin","exelon","exforge","ezetimibe","famotidine","farxiga","faslodex","femara","fenofibrate","fentanyl","ferrous sulfate","fioricet","flagyl","flexeril","flomax","flonase","flovent","fluoxetine","focalin","folic acid","forteo","fosamax","furosemide","gabapentin","gammagard","garcinia cambogia","gardasil","gemfibrozil","gemzar","genvoya","geodon","gilenya","gilotrif","gleevec","glipizide","glucophage","glucotrol","glucovance","glyburide","glyxambi","gralise","guaifenesin","guaifenex","halaven","harvoni","havrix","hcg","heparin","herceptin","hetlioz","hizentra","horizant","humalog","humira","humulin","humulin n","hydrochlorothiazide","hydrocodone","hydroxychloroquine","hydroxyzine","hysingla er","hytrin","hyzaar","ibrance","ibuprofen","imbruvica","imdur","imitrex","imodium","implanon","incruse ellipta","inderal","injectafer","inlyta","insulin","intelence","intuniv","invega","invokamet","invokana","iressa","isentress","isosorbide","jakafi","jalyn","janumet","januvia","jardiance","jentadueto","jetrea","jevtana","jublia","juvederm","juvisync","juxtapid","k-dur","kadcyla","kadian","kaletra","kalydeco","kapidex","kapvay","glatiramer","duloxetine","kazano","keflex","kenalog","keppra","kerydin","keytruda","kineret","klonopin","klor-con","kombiglyze xr","krill oil","kyprolis","kytril","lamictal","lansoprazole","lasix","latuda","levaquin","levothyroxine","levoxyl","lexapro","lidoderm","linzess","lipitor","lisinopril","loratadine","lorazepam","losartan","lovenox","lumigan","lupron","lyrica","macrobid","meclizine","melatonin","meloxicam","metformin","methadone","methocarbamol","methotrexate","methylphenidate","methylprednisolone","metoclopramide","metoprolol","metronidazole","miralax","mirtazapine","mobic","morphine","motrin","mucinex","myrbetriq","naloxone","namenda","naprosyn","naproxen","nasacort","nasonex","neulasta","neurontin","nexium","niacin","niaspan","nicotine","nifedipine","nitrofurantoin","norco","nortriptyline","norvasc","novolog","nucynta","nuvigil","ofev","omeprazole","omnicef","ondansetron","onfi","onglyza","opana","opdivo","opsumit","orencia","orlistat","ortho tri-cyclen","orthovisc","oseltamivir","osphena","otezla","oxybutynin","oxycodone","oxycontin","oxytrol","paroxetine","paxil","pepcid","percocet","phenergan","plaquenil","plavix","potassium chloride","pradaxa","pravachol","pravastatin","prednisone","pregabalin","premarin","prevacid","prilosec","prolia","promethazine","propranolol","protonix","prozac","qnasl","qsymia","quillivant xr","qutenza","ramipril","ranexa","ranitidine","rapaflo","reclast","reglan","relafen","remeron","remicade","renvela","requip","restasis","restoril","revlimid","risperdal","risperidone","ritalin","rituxan","robaxin","rocephin","saphris","savella","sensipar","septra","seroquel","sertraline","sildenafil","simvastatin","singulair","skelaxin","spiriva","spironolactone","stiolto respimat","strattera","suboxone","symbicort","synthroid","tamoxifen","tamsulosin","tegretol","temazepam","terazosin","","tizanidine","topamax","toprol","toradol","tradjenta","tramadol","travatan","trazodone","triamcinolone","triamterene","tricor","trileptal","trintellix","tylenol","uceris","ulesfia","uloric","ultane","ultracet","ultram","ultresa","uptravi","uroxatral","utibron neohaler","valacyclovir","valium","valtrex","vancomycin","vasotec","venlafaxine","ventolin","verapamil","vesicare","vicodin","victoza","viibryd","vimpat","vistaril","vitamin e","voltaren","voltaren gel","vytorin","vyvanse","warfarin","wellbutrin","wilate","xalatan","xalkori","xanax","xanax xr","xarelto","xeljanz","xeloda","xenazine","xenical","xeomin","xgeva","xifaxan","xigduo xr","xiidra","xofigo","xolair","xopenex","xtandi","xyrem","xyzal","yervoy","yondelis","yosprala","zanaflex","zantac","zemplar","zestoretic","zestril","zetia","ziac","zithromax","zocor","zofran","zoloft","zolpidem","zometa","zostavax","zosyn","zovirax","zyprexa","zyrtec","zytiga","zyvox"]

#dataset
with open('testfeaturefiledrugcombined1.txt') as f:
    afinnscores2 = []
    swnscores2=[]

    for line in f:
        datalist2=line.strip().split(',')
        afinnscores2.append(float(datalist2[0]))
        swnscores2.append(float(datalist2[1]))



#train file
with open('testfeaturefiledrug1.txt') as f:
    afinnscores = []
    swnscores=[]
    textlist=[]

    for line in f:
        datalist=line.strip().split(',')
        afinnscores.append(float(datalist[0]))
        swnscores.append(float(datalist[1]))
        textlist.append(datalist[2])

amin=min(afinnscores)
amin2=min(afinnscores2)

smin=min(swnscores)
smin2=min(swnscores2)

afullmin=min(amin,amin2)
sfullmin=min(smin,smin2)

if afullmin<0:
    afinnscores2 = [x - afullmin for x in afinnscores2]
    afinnscores = [x - afullmin for x in afinnscores]

if sfullmin<0:
    swnscores2 = [x - sfullmin for x in swnscores2]
    swnscores = [x - sfullmin for x in swnscores]

a=np.array(afinnscores)
b=np.array(swnscores)

c=np.column_stack((a,b))

print("finish train file")

a2=np.array(afinnscores2)
b2=np.array(swnscores2)

c2=np.column_stack((a2,b2))#all dataset


#encoder
enc=OneHotEncoder()

enc.fit(c2) #all

d=enc.transform(c) #train

d=d.todense()

#count or tfidf
#vec=CountVectorizer(analyzer='word',ngram_range=(2,3))
vec=TfidfVectorizer(analyzer='char_wb',ngram_range=(1,3))

sparsedata=vec.fit_transform(textlist)

e=sparsedata.todense()

x=np.hstack([e,d])

y=[]
for i in range(0,100):
    y.append(1)

for i in range(0,100):
    y.append(0)


print("finish train data setup")

clf=SVC(kernel="linear",probability=True)
#gnb=GaussianNB()
#lgr=LogisticRegression()
#sgd=SGDClassifier("modified_huber")
#knn=KNeighborsClassifier()
#dtc=DecisionTreeClassifier()
#rfc=RandomForestClassifier()

#clf2=SVC(kernel="linear",probability=True)
#gnb2=GaussianNB()
#lgr2=LogisticRegression()
#sgd2=SGDClassifier(loss="modified_huber")
#knn2=KNeighborsClassifier()
#dtc2=DecisionTreeClassifier()
#rfc2=RandomForestClassifier()

#voc=VotingClassifier(estimators=[('svc', clf2), ('gnb', gnb2), ('lr',lgr2), ('sgd',sgd2),('knn',knn2),('dtc',dtc2)],voting='soft',weights=[1,1,1,1,1,1])
#voc2=VotingClassifier(estimators=[('svc', clf2), ('gnb', gnb2), ('lr',lgr2), ('sgd',sgd2),('knn',knn2),('dtc',dtc2)],voting='hard',weights=[1,1,1,1,1,1])

clf.fit(x,y)

print("finish fitting, begin predictions")

totalcount=0
count=0

with open('testfeaturefiledrugcombined1.txt') as f:
    for line in f:
        afinnscores3=[]
        swnscores3=[]
        textlist3=[]

        datalist3 = line.strip().split(',')
        afinnscores3.append(float(datalist3[0]) - amin2)
        swnscores3.append(float(datalist3[1]) - smin2)

        testline = datalist3[2].split()
        output = []
        outline = ""
        for word in testline:
            if word in namelist:
                output.append("drug")
            else:
                output.append(word)

        outline = ' '.join(output)
        textlist3.append(outline)

        atest = np.array(afinnscores3)
        btest = np.array(swnscores3)

        ctest = np.column_stack((atest, btest))

        dtest=enc.transform(ctest)

        dtest=dtest.todense()

        sparsetest=vec.transform(textlist3)

        etest=sparsetest.todense()

        xtest = np.hstack([etest, dtest])

        predicted=clf.predict(xtest)

        if (predicted==1):
            g = open('predictedcombined2.txt', 'a')
            g.write(datalist3[2]+'\n')
            g.close()
            count+=1

            if (count%10000==0):
                print("predicted: " + str(count))

        totalcount+=1
        if(totalcount%20000==0):
            print(totalcount)


print("predicted: " + str(count))
print("total: " + str(totalcount))