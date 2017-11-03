# generator functions (with yield statement) are in fact iterators
def gen123():
    yield 1
    yield 2
    yield 3

# function returns generator object
g = gen123()
print(g)
print(next(g))

# new object on each assignment
h = gen123()
print(h)
print(next(h))

# can be used in loops
for v in gen123():
    print(v)

# on iteration all code above yield function is executed

def gen_chunks():
    print("Code above first yield")
    yield "part one"
    print("Code above second yield")
    yield "part two"
    print("Code above third yield")
    yield "part three"


i = gen_chunks()

print(next(i))
print(next(i))
print(next(i))