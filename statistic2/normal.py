import numpy as np
import random
import math
import collections
from scipy import stats
import copy

def intervals_zi_mi(array, interval, amount,l_lim):
     zi_min = min(array)
     zi_max = zi_min + interval
     counter = 0
     intervals = [zi_min]
     zi = []
     mi = []
     for i in range(amount):
        if array[i] <= round(zi_max,3)+0.003:
            counter += 1
            if i == amount - 1:
                intervals.append(zi_max)
                zi.append((zi_min + zi_max) / 2)
                mi.append(counter)
        else:
            intervals.append(zi_max)
            zi.append((zi_min + zi_max) / 2)
            mi.append(counter)
            zi_min = zi_max
            zi_max += interval
            counter = 1 

     return {'intervals':intervals,'zi':zi,'mi':mi}

def average(zi,mi,amount):
    sum = 0
    for i in range(len(zi)):
        sum+=zi[i] * mi[i]
    return round(sum / amount,3)

def standart(zi,mi,average, intervals_amount,amount):
    deviation = 0
    for i in range(intervals_amount):
       deviation +=((zi[i] - average) ** 2) * mi[i]
    variance = deviation / (amount - 1)
    return round(math.sqrt(variance),3)

def norm_value(x):
    return stats.norm.cdf(x) - 0.5

def probability(x,y,s,avg):
    return norm_value((y-avg)/s)-norm_value((x-avg)/s)


def merge(t):
    i = 0
    k = 1
    while i < len(t['n*pi']):
        if len(t['n*pi']) == 1: break
        if t['n*pi'][i] < 10 or t['mi'][i] < 5:
            if i == 0 or i != len(t['n*pi']) - 1 and t['n*pi'][i + 1] <= t['n*pi'][i - 1]:
                t['mi'][i + 1] += t['mi'][i]
                t['pi'][i + 1] += t['pi'][i]
                t['n*pi'][i + 1] = t['n*pi'][i] + t['n*pi'][i + 1]
                t['intervals'][i + 1] = t['intervals'][i]
                t['zi'][i + 1] = (t['intervals'][i] + t['intervals'][i + 2]) / 2
            else:
                t['mi'][i - 1] += t['mi'][i]
                t['pi'][i - 1] = t['pi'][i] + t['pi'][i - 2]
                t['n*pi'][i - 1] = t['n*pi'][i - 1] + t['n*pi'][i]
                #t['intervals'][i] = t['intervals'][i]
                t['zi'][i - 1] = (t['intervals'][i] + t['intervals'][i - 1]) / 2

            t['intervals'].pop(i)
            t['mi'].pop(i)
            t['zi'].pop(i)
            t['pi'].pop(i)
            t['n*pi'].pop(i)
            i = - 1
        i += 1

def info_func(amount,left,right,alpha):
    d = {}
    d['alpha'] = alpha
    d['amount'] = amount
    d['l_lim'] = left
    d['r_lim'] = right


    d['or_ar'] = []
    for i in range(d['amount']):
        d['or_ar'].append(round(random.uniform(d['l_lim'],d['r_lim']),3))
    d['array'] = sorted(d['or_ar'])
   # info['array'] = [0.016, 0.024, 0.03, 0.067, 0.068, 0.115, 0.142, 0.182, 0.193, 0.209, 0.251, 0.252, 0.276, 0.304, 0.312, 0.315, 0.316, 0.336, 0.347, 0.359, 0.378, 0.381, 0.402, 0.404, 0.42, 0.424, 0.437, 0.46, 0.479, 0.483, 0.49, 0.519, 0.551, 0.563, 0.646, 0.654, 0.671, 0.718, 0.728, 0.836, 0.841, 0.909, 0.963, 0.964, 0.991, 1.008, 1.025, 1.032, 1.041, 1.071, 1.075, 1.22, 1.222, 1.223, 1.225, 1.235, 1.258, 1.277, 1.315, 1.364, 1.368, 1.474, 1.587, 1.594, 1.61, 1.617, 1.654, 1.698, 1.712, 1.746, 1.756, 1.762, 1.776, 1.846, 1.904, 1.929, 1.961, 1.967, 1.995, 2.007, 2.012, 2.07, 2.087, 2.097, 2.121, 2.127, 2.146, 2.157, 2.232, 2.272, 2.353, 2.407, 2.417, 2.452, 2.502, 2.52, 2.586, 2.669, 2.684, 2.692, 2.696, 2.743, 2.762, 2.779, 2.783, 2.802, 2.817, 2.84, 2.841, 2.907, 2.969, 2.969, 3.097, 3.103, 3.121, 3.131, 3.164, 3.169, 3.18, 3.185, 3.213, 3.227, 3.245, 3.264, 3.266, 3.297, 3.298, 3.329, 3.331, 3.357, 3.365, 3.367, 3.39, 3.416, 3.474, 3.507, 3.511, 3.514, 3.515, 3.519, 3.53, 3.579, 3.582, 3.634, 3.682, 3.687, 3.704, 3.712, 3.72, 3.759, 3.795, 3.874, 3.914, 3.924, 3.947, 3.957, 3.982, 4.021, 4.022, 4.025, 4.071, 4.116, 4.121, 4.144, 4.156, 4.189, 4.253, 4.268, 4.271, 4.275, 4.355, 4.362, 4.363, 4.43, 4.443, 4.451, 4.452, 4.468, 4.497, 4.565, 4.582, 4.601, 4.615, 4.629, 4.649, 4.671, 4.703, 4.766, 4.773, 4.783, 4.793, 4.803, 4.804, 4.85, 4.861, 4.892, 4.897, 4.916, 4.986, 4.986]

    r = math.log(d['amount'], 2)
    if r == int(r):
        d['intervals_amount'] = r + 1
    else:
        d['intervals_amount'] = math.ceil(r)


    
    d['interval'] = round((d['array'][-1] - d['array'][0]) / d['intervals_amount'],3)
    d['t'] = intervals_zi_mi(d['array'],d['interval'],d['amount'],d['l_lim'])
    d['average'] = average(d['t']['zi'],d['t']['mi'], d['amount']) 
    d['standart'] = standart(d['t']['zi'],d['t']['mi'],
                                       d['average'], d['intervals_amount'],d['amount'])

    d['t']['zi']=[round(i,4) for i in d['t']['zi']]
    d['t']['intervals']=[round(i,4) for i in d['t']['intervals']]

    d['i-vals_old']=[]
    for i in range(1,len(d['t']['intervals'])):
         d['i-vals_old'].append('( {} ; {} ]'.format(d['t']['intervals'][i-1],d['t']['intervals'][i]))

    d['t']['pi'] = []
    d['t']['n*pi'] = []

    for i in range(1,d['intervals_amount'] + 1):
        pi = probability(d['t']['intervals'][i-1],d['t']['intervals'][i],d['standart'],d['average'])
        d['t']['pi'].append(round(pi,4))
        d['t']['n*pi'].append(round(pi * d['amount'],4))



    print('interval', "\t", 'zi',"\t",'mi'," ",'pi'," ",'n*pi')
    for i in range(d['intervals_amount']):
       print(d['t']['intervals'][i],"-", d['t']['intervals'][i+1], "\t",d['t']['zi'][i]," ",d['t']['mi'][i]," ",d['t']['pi'][i]," ",
             d['t']['n*pi'][i])
 
    d['zi_copy']=copy.deepcopy(d['t']['zi'])
    d['mi_copy']=copy.deepcopy(d['t']['mi'])
    d['pi_copy']=copy.deepcopy(d['t']['pi'])
    d['n*pi_copy']=copy.deepcopy(d['t']['n*pi'])
   

    merge(d['t'])

    d['t']['pi']=[round(i,4) for i in d['t']['pi']]
    d['t']['n*pi']=[round(i,4) for i in d['t']['n*pi']]
    d['t']['intervals']=[round(i,4) for i in d['t']['intervals']]
    d['t']['zi']=[round(i,4) for i in d['t']['zi']]

    d['d.f.'] = len(d['t']['mi'])- 3

    d['i-vals_new']=[]
    for i in range(1,len(d['t']['intervals'])):
         d['i-vals_new'].append('( {} ; {} ]'.format(d['t']['intervals'][i-1],d['t']['intervals'][i]))

    print('after')
    for i in range(len(d['t']['n*pi'])):
       print(d['t']['intervals'][i],"-", d['t']['intervals'][i+1],"\t", d['t']['zi'][i]," ",d['t']['mi'][i]," ",d['t']['pi'][i]," ",
             d['t']['n*pi'][i])

    print(d['array'])

    d['x^2emp']=0
    for i, el in enumerate(d['t']['mi']):
        d['x^2emp'] += ((el-d['t']['n*pi'][i])**2)/d['t']['n*pi'][i]

    d['x^2emp']=round(d['x^2emp'],5)
    d['x^2kr']=round(stats.chi2.isf(d['alpha'],d['d.f.']),5)
  
    for k,v in d.items():
        print(k,'\t',v)
    return d

#info_func(200,0,5,0.05)
