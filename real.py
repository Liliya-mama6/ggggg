
def all_variants(a):
    i=1
    while i<=len(a):
        for j in range(len(a)-i+1):
            yield a[j:j+i]
        i+=1
store=all_variants(input())
for i in store:
    print(i)
