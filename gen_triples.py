import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import pandas as pd
sns.set_theme(style="dark")

def gen_triples(lam, mew):
    x = 2 * lam * mew
    y = lam ** 2 - mew ** 2
    z = lam ** 2 + mew ** 2
    corresponding_triple = [x,y,z]
    return corresponding_triple

print(gen_triples(1,2))
print(gen_triples(2,3))

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

# Testing Relatively_prime
# Case 3,5 - True
print(relatively_prime(3,5))
# Case 4,7 - True
print(relatively_prime(4,7))
# Case 3,6 - False
print(relatively_prime(3,6))
# Case 5,10- False
print(relatively_prime(5,10))
# Case 5, 3 - True
print(relatively_prime(5,3))
# Case 20,15 - False
print(relatively_prime(20,15))



def verify_triples(my_triple):
    sum1 = my_triple[0] ** 2
    sum2 = my_triple[1] ** 2
    sum3 = my_triple[2] ** 2
    if sum1 + sum2 == sum3:
        return "This is a Pythagorean Triple"
    else:
        return "Not a triple - double check please"


print(verify_triples(gen_triples(1,2)))
print(verify_triples(gen_triples(2,3)))


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

#print(gen_triplesTY1(20))
#print(gen_triplesTYN1(20))

data = gen_triplesTY1(20)

params = ['mew','lam','total']
df = pd.DataFrame(data,columns=params)
df.to_csv('./dataset.csv')


triples=pd.read_csv("./dataset.csv")

# Need to find a good way to visualize
# Also more data variations, along with negative 
# instances to make the data more interesting!

sns.catplot(data=triples,kind='swarm', x='mew',y='lam',hue='total')
sns.relplot(x="mew", y="lam", hue="total",
            sizes=(40, 400), alpha=.5, palette="muted",
            height=6, data=triples)

#plt.show()