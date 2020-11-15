# Multiples of 3 and 5
# 15/11/20, Robert McLeod (rbbi)

def SumMultiples(lim):
    sum=0
    for val in range(lim):
        if val % 3 == 0 or val % 5 == 0:
            sum+=val
    return sum

if __name__ == "__main__":
    print(SumMultiples(1000))