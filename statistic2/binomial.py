import numpy as np
import collections
import math
from scipy import stats
import copy

def merge(d):
    i = 0
    while i < len(d['n*pi']):
        if d['n*pi'][i] < 10 or d['mi'][i]<5:
            if i == 0 or (i != len(d['n*pi'])-1 and d['n*pi'][i+1] < d['n*pi'][i-1]):
                d['mi'][i+1] += d['mi'][i]
                d['pi'][i+1] += d['pi'][i]
                d['n*pi'][i+1] = d['n*pi'][i]+ d['n*pi'][i+1]

                if type(d['xi'][i+1]) is tuple and type(d['xi'][i]) is tuple:
                    d['xi'][i+1]=d['xi'][i]+d['xi'][i+1]
                elif type(d['xi'][i+1]) is tuple:
                    d['xi'][i+1]=(d['xi'][i],)+d['xi'][i+1]
                elif type(d['xi'][i]) is tuple:
                    d['xi'][i+1]=d['xi'][i]+(d['xi'][i+1],)
                else: d['xi'][i+1]= (d['xi'][i],d['xi'][i+1])

            else:
                d['mi'][i-1] += d['mi'][i]
                d['pi'][i-1] = d['pi'][i]+ d['pi'][i-1]
                d['n*pi'][i-1] = d['n*pi'][i-1]+d['n*pi'][i]

                if type(d['xi'][i-1]) is tuple and type(d['xi'][i]) is tuple:
                    d['xi'][i-1]=d['xi'][i-1]+d['xi'][i]
                elif type(d['xi'][i]) is tuple:
                    d['xi'][i-1]=(d['xi'][i-1],)+d['xi'][i]
                elif type(d['xi'][i-1]) is tuple:
                     d['xi'][i-1]+=(d['xi'][i],)
                else: d['xi'][i-1]= (d['xi'][i-1],d['xi'][i])

            d['mi'].pop(i)
            d['xi'].pop(i)
            d['pi'].pop(i)
            d['n*pi'].pop(i)
            i =- 1
        i += 1

def info_func(n,left,N,alpha=0.05):
    d = {}
    d['alpha']=alpha 
    d['n'] = n
    d['N'] = N
    d['left'] = left
    d['or_arr'] = np.random.randint(d['left'], d['N']+1,d['n'])
    d['array'] = sorted(d['or_arr'])

    table = collections.OrderedDict(collections.Counter(d['array']))
    d['xi'] = list(table.keys())
    d['mi'] = list(table.values())
    table.clear()

    sum=0
    for i in range(len(d['xi'])):
        sum+=d['xi'][i] * d['mi'][i]

    d['p*'] = round(sum/(d['N']*d['n']),4)
    d['q*'] = 1-d['p*']
  

    d['pi']=[]
    d['n*pi']=[]
    for i in range(d['N']+1):
        pi=math.comb(d['N'],i)*d['p*']**i*d['q*']**(d['N']-i)
        d['pi'].append(round(pi,4))
        d['n*pi'].append(round(pi*d['n'],4))

    print('xi'," ",'mi'," ",'pi'," ",'n*pi')
    for i in range(d['N']+1):
       print(d['xi'][i]," ",d['mi'][i]," ",d['pi'][i]," ",d['n*pi'][i])

    d['xi_copy']=copy.deepcopy(d['xi'])
    d['mi_copy']=copy.deepcopy(d['mi'])
    d['pi_copy']=copy.deepcopy(d['pi'])
    d['n*pi_copy']=copy.deepcopy(d['n*pi'])

    merge(d)
   
    d['d.f.']=len(d['xi'])-2
    d['pi']=[round(i,4) for i in d['pi']]
    d['n*pi']=[round(i,4) for i in d['n*pi']]

    d['x^2emp']=0
    for i in range(len(d['n*pi'])):
         d['x^2emp']+=(d['mi'][i]-d['n*pi'][i])**2/d['n*pi'][i]
    d['x^2emp']=round(d['x^2emp'],5)
    for i in range(len(d['n*pi'])):
       print(d['xi'][i]," ",d['mi'][i]," ",d['pi'][i]," ",d['n*pi'][i])

    d['x^2kr']=round(stats.chi2.isf(d['alpha'],d['d.f.']),5)
    print(d['x^2emp'])
    print(len(d['xi']))
    print(d['d.f.'])
    print(d['x^2kr'])
    return d
   
