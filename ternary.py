def ternarySearch(l,r,key,arr):
    if (r>=l):
        mid1=l+(r-1)//3
        mid2=r-(r-l)//3
        if(arr[mid1] == key):
            return mid1
        if(arr[mid2] == key):
            return mid2
        if(key<=arr[mid1]):
            return ternarySearch(l,mid1-1,key,arr)
        elif(key>=arr[mid2]):
            return ternarySearch(mid2+1,r,key,arr)
        else:
            return ternarySearch(mid1+1,mid2-1,key,arr)
            return-1
l,p,r=0,9,5
arr=[1,2,3,4,5,6,7,8,9,10]
l=0
r=9
key=4
p=ternarySearch(l,r,key,arr)
print("if index",key,"is",p)
key=9
p=ternarySearch(l,r,key,arr)
print("index of",key,"is",p)