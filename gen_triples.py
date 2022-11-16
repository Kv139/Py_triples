def gen_triples(lam, mew):
    x = 2 * lam * mew
    y = lam ** 2 - mew ** 2
    z = lam ** 2 + mew ** 2
    corresponding_triple = [x,y,z]
    return corresponding_triple

print(gen_triples(1,2))
print(gen_triples(2,3))


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

print(gen_triplesTY1(10))
print(gen_triplesTYN1(10))