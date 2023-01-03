data=[]
n=int(input("enter size of array:"))
for i in range(n):
    ele=int(input("Enter data:"))
    data.append(ele)
    print("Data:",data)
minv=0 
maxv=99
print(data)
nb=int(input("enter no of bucket"))
bucket=[]
print(bucket)

bucket=[[]for number in range(nb)]
print(bucket)

for number in data:
   bucketsort=(number-minv)//nb
   bucket[bucketsort].append(number)
print(bucket)



n=len(data)
for i in range(0,n):
    min_=i
    for j in range(i+1,n):
        if(data[j]<data[min_]):
            min_=j 
    if(min_!=i):
        data[min_],data[i]=data[i],data[min_]
print("After bucket sort, we have :",data)

print("top 5",data[10:5:-1])
    
