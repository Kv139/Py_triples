import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import pandas as pd
import random
sns.set_theme(style="dark")

def gen_triples(lam, mew):
    x = 2 * lam * mew
    y = lam ** 2 - mew ** 2
    z = lam ** 2 + mew ** 2
    corresponding_triple = [x,y,z]
    return corresponding_triple


def relatively_prime(x,y):
    if y == 1:
        return True
    if y == 0:
        return False
    else:
        y = y % x
        try:
            return relatively_prime(y,x)
        except ZeroDivisionError:
            return False

# 6, 8 
def relatively_prime2(x,y):
    if y == 1:
        return False
    if y == 0:
        return x
    else:
        y = y % x
        try:
            return relatively_prime2(y,x)
        except ZeroDivisionError:
            return x


print("Testing relatively Prime")
# Case 3,5 - True
print(relatively_prime(3,5))
# Case 4,7 - True
print(relatively_prime(4,7))
# Case 3,6 - False
print("==========")
print("Testing relatively Prime2")
#print(relatively_prime2(3,6))
# Case 5,10- False
print(relatively_prime2(6,8))
# Case 5, 3 - True
print(relatively_prime2(5,3))
# Case 20,15 - False
print(relatively_prime2(20,15))
print("============")



def verify_triples(my_triple):
    sum1 = my_triple[0] ** 2
    sum2 = my_triple[1] ** 2
    sum3 = my_triple[2] ** 2
    if sum1 + sum2 == sum3:
        return True
    else:
        return False


def gen_ran_triples(quantity):
    set_triples = []
    for i in range(1,quantity):
        x = random.randrange(1,1000)
        y = random.randrange(1,1000)
        set_triples.append(gen_triples(x,y))
    return set_triples

print("TESTING")
#print(gen_ran_triples(10))
print("========")

print("TESTING RANDOM GENERATION")
data2 = gen_ran_triples(500)
for i in data2:
    if verify_triples(i) == False:
        print("FAILED TRIPLE")
print("=============")

# haha it works!

def normalize_triple(triple):
    is_prime = relatively_prime2(triple[0],triple[1])
    while is_prime != False:
        triple[0] = triple[0] / is_prime
        triple[1] = triple[1] / is_prime
        triple[2] = triple[2] / is_prime
        is_prime = relatively_prime2(triple[0],triple[1])
    if verify_triples(triple) == False:
        print(triple)
    return triple

print("TESTING NORMALIZATION OF RANDOM DATA")
for i in data2:
    if verify_triples(i) == False:
        print(i)
        print("FAILED TRIPLE")
print()
print("================")

print("TESTING SPECIFIC INSTANCE OF FAILURE")

print("TESTING normalize_triple")
#print(relatively_prime2(8,6))
#normalize_triple([6,8,10])
#normalize_triple([12,16,20])
print("=========")

def gen_triplesTY1(cutoff):
    set_triples = []
    for i in range(1,cutoff):
        set_triples.append(gen_triples(1,i))
    return set_triples

def gen_triplesTYN1(cutoff):
    set_triples = []
    for i in range(1,cutoff):
        set_triples.append(gen_triples(-1,i))
    return set_triples

params = ['mew','lam','total']
df = pd.DataFrame(data2,columns=params)
df.to_csv('./dataset.csv')


triples=pd.read_csv("./dataset.csv")

# Need to find a good way to visualize
# Also more data variations, along with negative 
# instances to make the data more interesting!

#sns.catplot(data=triples,kind='swarm', x='mew',y='total',hue='lam')
sns.relplot(x="mew", y="lam", hue="total",
        alpha=.5, palette="muted",
        height=5, data=triples)

plt.show()