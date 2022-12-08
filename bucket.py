G =[5,8,7,9,11,44,55,24,66,77,99,88,32,36,63,49,91,39,72,81,94,22,14,18]
min = 0
max =99
print("Before sorting the elements:")
print(G)
no_bucket = 10
bucket =[]
bucket =[[] for i in range(no_bucket)]
A= []
for j in G:
    bucket_no = (j - min)// no_bucket
    bucket[bucket_no].append(j)
def bubblesort(bucket):
    n = len(bucket) - 1
    for i in range(0, len(bucket)):
        for j in range(0,n):
            if (bucket[j]>bucket[j+1]):
                temp=bucket[j]
                bucket[j]=bucket[j+1]
                bucket[j+1]=temp
        n=n-1
for k in range(1,10):
    bubblesort(bucket[k])
print("After sorting the elements:")
print(bucket)