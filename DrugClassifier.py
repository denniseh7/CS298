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
if amin<0:
    afinnscores = [x - amin for x in afinnscores]

smin=min(swnscores)
if smin<0:
    swnscores = [x - smin for x in swnscores]

print(afinnscores)
print(swnscores)


a=np.array(afinnscores)
b=np.array(swnscores)

c=np.column_stack((a,b))

enc=OneHotEncoder()

d=enc.fit_transform(c)

d=d.todense()

#count or tfidf
#vec=CountVectorizer(analyzer='char',ngram_range=(1,4))
vec=TfidfVectorizer(analyzer='char_wb',ngram_range=(1,4))

sparsedata=vec.fit_transform(textlist)

e=sparsedata.todense()

x=np.hstack([e,d])

y=[]
for i in range(0,100):
    y.append(1)

for i in range(0,100):
    y.append(0)




clf=SVC(kernel="linear",probability=True)
gnb=GaussianNB()
lgr=LogisticRegression()
sgd=SGDClassifier("modified_huber")
knn=KNeighborsClassifier()
dtc=DecisionTreeClassifier()
rfc=RandomForestClassifier()

clf2=SVC(kernel="linear",probability=True)
gnb2=GaussianNB()
lgr2=LogisticRegression()
sgd2=SGDClassifier(loss="modified_huber")
knn2=KNeighborsClassifier()
dtc2=DecisionTreeClassifier()
rfc2=RandomForestClassifier()

voc=VotingClassifier(estimators=[('svc', clf2), ('gnb', gnb2), ('lr',lgr2), ('sgd',sgd2),('knn',knn2),('dtc',dtc2)],voting='soft',weights=[1,1,1,1,1,1])
voc2=VotingClassifier(estimators=[('svc', clf2), ('gnb', gnb2), ('lr',lgr2), ('sgd',sgd2),('knn',knn2),('dtc',dtc2)],voting='hard',weights=[1,1,1,1,1,1])


clfscore=cross_val_score(clf,x,y,cv=5,scoring="f1_weighted")
gnbscore=cross_val_score(gnb,x,y,cv=5,scoring="f1_weighted")
lgrscore=cross_val_score(lgr,x,y,cv=5,scoring="f1_weighted")
sgdscore=cross_val_score(sgd,x,y,cv=5,scoring="f1_weighted")
knnscore=cross_val_score(knn,x,y,cv=5,scoring="f1_weighted")
dtcscore=cross_val_score(dtc,x,y,cv=5,scoring="f1_weighted")
rfcscore=cross_val_score(rfc,x,y,cv=5,scoring="f1_weighted")
svocscore=cross_val_score(voc,x,y,cv=5,scoring="f1_weighted")
hvocscore=cross_val_score(voc2,x,y,cv=5,scoring="f1_weighted")

print("svc: " + str(np.mean(clfscore)))
print("gnb: " + str(np.mean(gnbscore)))
print("lgr: " + str(np.mean(lgrscore)))
print("sgd: " + str(np.mean(sgdscore)))
print("knn: " + str(np.mean(knnscore)))
print("dtc: " + str(np.mean(dtcscore)))
print("rfc: " + str(np.mean(rfcscore)))
print("soft voc: " + str(np.mean(svocscore)))
print("hard voc: " + str(np.mean(hvocscore)))