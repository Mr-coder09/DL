
#Bubble Sort
score=[99.89,75.78,50.80,45,35,88.67,67.80,58,20,19,91.33,95.80,82.78,72.88,62.80]
def bubble_sort():
    size=15
    for i in range (size):
        for j in range (size-1):
            if (score[j]>score[j+1]):
                temp=score[j]
                score[j]=score[j+1]
                score[j+1]=temp
bubble_sort()
print("Score of students calculated using bubble sort is: ")
print(score)

#Selection sort
def selection_sort():
    size=15
    for i in range (size):
        min=i
        for j in range (size-1):
            if (score[j]>score[min]):
                min=j;
                temp=score[i]
                score[i]=score[min]
                score[min]=temp
selection_sort()
print("Score of students calculated using selection sort is : ")
print(score)

print("Top 5 scores of students are: ")
def top5():
    size=15
    for i in range(size):
        flag=0
        for j in range(size-1):
            if (score[j]<score[j+1]):
                
                temp=score[j]
                score[j]=score[j+1]
                score[j+1]=temp
                flag=1
    for k in range(5):
        print(score[k])
top5()
#time complexity of bubble sort
#  o(n^2) average and worst
#   o(n) best case
# it is stable ,space= o(1)
#selection =in all case o(n^2)