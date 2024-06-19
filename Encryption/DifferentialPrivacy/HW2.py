import random
from math import log
from math import exp
import os
import csv
import numpy as np
import copy

# line buffer
buff = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

# file name
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'vote.csv')

# initialize rows and columns(fields)
fields= []

# dictionary of class a and b yes'
foo = {'A':{},'B':{}}
LaFoo = {'A':{},'B':{}}


with open(filename, 'r') as csvfile:
    # csv reader object
    csvreader = csv.DictReader(csvfile)

    # Extracting column names from first row
    fields = next(csvreader)


    # get data from each row
    for row in csvreader:
        for key, value in row.items():
            if row["Class"] == 'A':
                if not foo['A'].get(key,  None):
                    foo['A'][key] = {}
                    foo['A'][key]['y'] = 0
                    foo['A'][key]['n'] = 0
                foo['A'][key]['n'] += row[key].count('n')
                foo['A'][key]['y'] += row[key].count('y')
            else:
                if not foo['B'].get(key, None):
                    foo['B'][key] = {}
                    foo['B'][key]['y'] = 0
                    foo['B'][key]['n'] = 0
                foo['B'][key]['n'] += row[key].count('n')
                foo['B'][key]['y'] += row[key].count('y')


def flip():
    x = random.random()
    return x

def coinTable(n):
    num = n
    i = 1
    totaly = 0
    totaln = 0
    while i < num:
        x = flip()
        if x > 0.5:
            totaly += 1
        else:
            y = flip()
            if y > 0.5:
                totaly += 1
            else:
                totaln += 1
        i += 1
    return totaly, totaln

def laplace(f, s):
    l = np.random.laplace(f, s)
    return l

def gauss(f, s):
    g = np.random.normal(f, s)
    return g

def expon(b, s):
    e = np.random.exponential(b, s)
    return e

if __name__ == "__main__":

    # separator
    for x in range(0, 2):
        print(buff)

    # our un-ambigious data, the True data
    print("This is the True data Dict: %s" % foo)

    # separator
    for x in range(0, 2):
        print(buff)

    # The Random Response Dict
    RR = copy.deepcopy(foo)

    for k, _ in RR.items():
        for k1, _ in RR[k].items():
            yesNum = RR[k][k1]['y']
            noNum = RR[k][k1]['n']
            a, b = coinTable(yesNum)
            x, y = coinTable(noNum)
            RR[k][k1]['y'] = a
            RR[k][k1]['n'] = y
    
    print("This is the new RR Dict: %s" % RR)


    # The LaPlace generation with Beta

    B = 1/0.01

    x = laplace(0, B)

    # Create the LaPlace dict to be modified
    LaFoo = copy.deepcopy(foo)

    # separator
    for x in range(0, 2):
        print(buff)

    # Our laplace ambigious data w ep = 0.01

    for k, _ in LaFoo.items():
        for k1, _ in LaFoo[k].items():
            LaFoo[k][k1]['y'] += x
            LaFoo[k][k1]['n'] += x


    print("This is the LaPlace Dict: %s" % LaFoo)

    # separator
    for x in range(0, 2):
        print(buff)

    LaFooToo = copy.deepcopy(foo)

    # The LaPlace generation with Beta
    # B = delta(f)/ep
    B = 1/1

    x = laplace(0, B)


    # Our LaPlace ambigious data with ep = 1

    for k, _ in LaFooToo.items():
        for k1, _ in LaFooToo[k].items():
            LaFooToo[k][k1]['y'] += x
            LaFooToo[k][k1]['n'] += x

    print("This is the LaFoo data with eps = 1 : %s" % LaFooToo)

    # separator
    for x in range(0, 2):
        print(buff)

    Gauss = copy.deepcopy(foo)

    # Gauss generator with Values

    mu = 0
    ldelta = 0.05
    o = 2*log(1.25/ldelta)*1/0.0001

    x = gauss(mu, o)

    # Our Gauss ambigious data with ep = 0.01 & ld = 0.05

    for k, _ in Gauss.items():
        for k1, _ in Gauss[k].items():
            Gauss[k][k1]['y'] += x
            Gauss[k][k1]['n'] += x

    print("This is the Gauss data with ep = 0.01 & little delta = 0.05: %s" % Gauss)

    # separator
    for x in range(0, 2):
        print(buff)


    GaussToo = copy.deepcopy(foo)

    # Gauss generator with Values

    mu = 0
    ldelta = 0.5
    o = 2*log(1.25/ldelta)*1/1

    x = gauss(mu, o)

    # Our Gauss ambigious data with ep = 1 & ld = 0.5

    for k, _ in GaussToo.items():
        for k1, _ in GaussToo[k].items():
            GaussToo[k][k1]['y'] += x
            GaussToo[k][k1]['n'] += x

    print("This is the Gauss data with ep = 1 & little delta = 0.5: %s" % Gauss)

    # separator
    for x in range(0, 2):
        print(buff)


    Expo = copy.deepcopy(foo)
    ExpoToo = copy.deepcopy(foo)

    # Exponential generator with values

    B = 1/1

    for k, _ in Expo.items():
        for k1, _ in Expo[k].items():
            q = Expo[k][k1]['y']
            q += Expo[k][k1]['n']
            a = expon(B, q)
            for x in range(0, q):
                Expo[k][k1]['y'] += a[x]
                Expo[k][k1]['n'] += a[x]

    print("This is the Exponential data set 1 : %s" % Expo)

        # separator
    for x in range(0, 2):
        print(buff)


    # Exponential generator with values

    B = 1/1

    for k, _ in ExpoToo.items():
        for k1, _ in ExpoToo[k].items():
            q = ExpoToo[k][k1]['y']
            q += ExpoToo[k][k1]['n']
            a = expon(B, q)
            for x in range(0, q):
                ExpoToo[k][k1]['y'] += a[x]
                ExpoToo[k][k1]['n'] += a[x]

    print("This is the Exponential data set 1 : %s" % ExpoToo)