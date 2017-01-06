import plotly.plotly as py
import plotly.graph_objs as go
import plotly

sosylist=[]
xanaxMap={}
xanaxkey=[]
xanaxval=[]

with open('xanaxsosy.txt') as f:
    for line in f:
        sosy=line.strip()
        sosylist.append(sosy)


with open('xanaxkv.txt') as f:
    for line in f:
        kvpair=line.split(',')
        key=kvpair[0]
        val=int(kvpair[1].strip())
        if key in sosylist:
            xanaxMap[key]=val


#xanaxkey=sorted(xanaxMap, key=xanaxMap.get, reverse=True)
#xanaxval=sorted(xanaxMap.values(),reverse=True)

xanaxkey=['Chills', 'spells', 'Malaise', 'Blackout', 'Catch', 'Halitosis', 'Tired', 'Hunger', 'Blurred vision', 'Muscle Cramp', 'Earache', 'Withdrawal', 'Vomiting', 'unwanted hair', 'Agitation', 'Sleeplessness', 'Muscle twitch', 'Pruritus', 'Sighing resp.', 'Clumsiness', 'Headache', 'Nausea', 'Memory Loss', 'Drooling','Seizures', 'Other']
xanaxval=[98, 39, 21, 13, 13, 11, 8, 6, 6, 5, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2,24]
print(xanaxkey)
print(xanaxval)
print(len(xanaxval))
print(len(xanaxkey))

data = [go.Bar(
            x=xanaxkey,
            y=xanaxval
    )]

layout = go.Layout(
    annotations=[
        dict(x=xi, y=yi,
             text=str(yi),
             xanchor='center',
             yanchor='bottom',
             showarrow=False,
             ) for xi, yi in zip(xanaxkey, xanaxval)],
    yaxis=dict(title='Number Reported'),
    font=dict(size=18)

)

fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='xanax_final.html')
