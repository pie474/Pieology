__author__ = 'chinmay'
def get_odd_numbers(i):
    return range(1, i, 2)
def yield_odd_numbers(i):
    for x in range(1, i, 2):
       yield x
foo = get_odd_numbers(10)
print(foo)
bar = yield_odd_numbers(10)
print(bar)

for dig in bar:
    print(dig)

exit()

def fib():
    cur,last = 0,1
    while True:
        yield cur
        cur, last = last, cur+last
fibcnt=0
for f in fib():
    print('%ith fibonacci number: %i'%(fibcnt,f))
    fibcnt += 1
    if(fibcnt > 100): break
