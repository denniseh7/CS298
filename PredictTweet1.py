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

with open('trainfile1.txt') as f:
    afinnscores = []
    swnscores=[]
    textlist=[]

    for line in f:
        datalist=line.strip().split(',')
        afinnscores.append(float(datalist[0]))
        swnscores.append(float(datalist[1]))
        textlist.append(datalist[2])

shifter=50 #change to positive
flag=True
flag2=True

amin=min(afinnscores)
if amin<0:
    afinnscores = [x + shifter for x in afinnscores]
    flag=False

smin=min(swnscores)
if smin<0:
    swnscores = [x + shifter for x in swnscores]
    flag2=False


a=np.array(afinnscores)
b=np.array(swnscores)

c=np.column_stack((a,b))

enc=OneHotEncoder()

enc.fit()


d=enc.transform(c)

d=d.todense()

#count or tfidf
#vec=CountVectorizer(analyzer='word',ngram_range=(2,3))
vec=TfidfVectorizer(analyzer='word',ngram_range=(1,3))

sparsedata=vec.fit_transform(textlist)

e=sparsedata.todense()

x=np.hstack([e,d])

y=[]
for i in range(0,200):
    y.append(1)

for i in range(0,200):
    y.append(0)




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