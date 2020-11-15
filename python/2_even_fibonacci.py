# Sum of even Fibonacci numbers up to 4 million
# 15/11/20, Robert McLeod (rbbi)

def even_fib_rec(first,second,lim):
    next=first+second
    if (next>=lim):
        return 0 
    if next % 2 == 0:
        return next + even_fib_rec(second, next, lim)
    return even_fib_rec(second, next, lim)

if __name__ == "__main__":
    print(even_fib_rec(0,1,4_000_000))