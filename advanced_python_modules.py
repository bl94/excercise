from collections import Counter

my_list=[2,2,2,1,1,3]
c=Counter(my_list)
print(c["Bartek"])
print(c)

print(*c.values())

product=1
for factor in c.elements():
    product*=factor
print(product)

print(c.most_common(2))

print(list(c))

my_list=["Kiebling","Lewandowski","Benzema","Lewandowski"]

footballers=Counter(my_list)
print(*footballers.items())

print(footballers.most_common(1))



from collections import defaultdict

d=defaultdict(lambda : "None")
print(d.get("Wrong"))
#d.get['True'] = "Truth"
d["False"]="Error"
print(*d)
d['a']=10
print(*d.items(),sep="\n")

#named tuples

from collections import namedtuple

Dog=namedtuple("Dog",["age",'breed','name'])
sammy=Dog(age=5,breed="Husky",name="Sam")
print(sammy.age)
print(sammy.breed)