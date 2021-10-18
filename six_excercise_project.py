#decorator
def play_again(game):
    print("I play again")
    def game_round(a):
        print("first round")
    return game_round
    
def war_game():
    return "War game"

def calc(square_func):
    print("Calculator")
    def square(a):
        print("Square field : ")
        square_func(a)
    return square

def square_field(a):
    print(a**2)

#square_field(2)

#another example 
def adder_10(func_number):
    def add(*args,**kwargs):
        print(f"First number is {args[0]} Second number is {args[1]}")
        return func_number(*args,**kwargs)+10
    return add

def adder_15(func_number):
    def add(*args,**kwargs):
        print(f"First number is {args[0]} Second number is {args[1]}")
        return func_number(*args,**kwargs)+15
    return add

@adder_15
@adder_10
def number(x,y): 
    return x+y

print(number(4,5))

#Another example
def create_adder(x):
    def adder(y):
        return x+y
    return adder

add_15=create_adder(15)
print(add_15(10))

def create_minusor(x):
    def minusor(y):
        return x-y
    return minusor

minus_15=create_minusor(15)
print(minus_15(10))

def action(surname_and_name_func):
    def add_action(*args,**kwargs):
        return surname_and_name_func(*args,**kwargs)+ " are digging"
    return add_action

def name(surname_method):
    def add_name(*args,**kwargs):
        return surname_method(*args,**kwargs) + " Lepa"
    return add_name

@action
@name
def surname_func(surname):
    return surname

print(surname_func("bartek"))
#

#yield
def generate_numbers(n):
    for x in range(n):
        yield x**3

for x in generate_numbers(10):
    print(x)

gen_list=list(generate_numbers(10))
print(*gen_list)


def gen_fibon(n):
    a=1
    b=1
    for i in range(n):
        a,b=b,a+b
        yield a

gen_fib_list=gen_fibon(4)

print(next(gen_fib_list))
print(next(gen_fib_list))

def generate_letters(index_name):
    double_letter_name=""
    for letter in index_name:
        yield letter*2
 
print(*generate_letters("bartek"),sep=" ")


g = generate_letters("bartek")
#next
print(next(g))
print(next(g))
#iter
sentence="Bartek is programming in Python"
sentence_iter=iter(sentence)
print(next(sentence_iter))  


list_of_words_from_sentence=[sentence.split()]
list_of_words=iter(list_of_words_from_sentence)
print(next(list_of_words))
      
#default dict

#namedtuple
