'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def read():
    import sys
    return list(map(int, sys.stdin.readline().strip().split()))

def solve():
    n,m=read()
    a=[0]*(n+1)
    for i in range(m):
        v,u,dollars=read()
        a[u]+=dollars
        a[v]-=dollars
    res=0
    print(a)
    for i in range(n+1):
        if a[i]>0: res+=a[i]
    print(res)


if __name__=='__main__':
	solve()