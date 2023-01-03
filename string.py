#AIM {a} Program to display word with longest length
def longestword():
    str=input("Enter a string to find longest word in it:")
    long = ""
    i = 0
    while(i<len(str)):
        str1 = ""
        if(i != len(str)):
            while(str[i] == " "):
                i=i+1
        while(str[i] != " "):
                str1 = str1 + str[i]
                i=i+1
                if(i == len(str)):
                    break
        if(len(str1)>len(long)):
                long = str1
    print("Longest word is:",long)
longestword()

#AIM{b} Python program to find occurance of particular character in a string
my_string = input("Enter a String: ")
my_char = input("Enter a Character: ")
count = 0
for temp in my_string:
    if my_char == temp:
        count = count + 1
print("Number of Occurrence of Character is: ", count)


#AIM{C} To check palindrome

def palindrome():
    str2= input("Enter string to know whether it is palindrome or not: ")
    lenstr2= len(str2)
    j = lenstr2 - 1
    flag = 0
    for i in range(int(lenstr2 / 2 + 1)):
        if (str2[1] == str2[1]):
            j -= 1
            flag = 1
        else:
            flag=0 
            break
    if (flag== 1):
        print("Entered string is Palindrome")
    else:
        print("Entered string is not Palindrome")
palindrome()

#AIM{d} Program to display index of first apperance of the substring 
main = input("The main string is : ")
sub = input("The substring to be searched is :")
count = 0
for i in range (0,len(main)):
   match = True
   if sub[0]==main[i]:
     j=0
     for j in range(0,len(sub)):
         if sub[j]!=main[i+j]:
             match = False
             print("No substring")
             break
         else:
             count=count+1
             if match == True and count == len(sub):
                 print("Substring")
                 print("Position start:",i)

# AIM{e} To determine frequency of occurance of each word in string
str = input("Enter the string to find occurance each character in it: ")
str=str.split()
i=0

while (i<len(str)):
    count = 0
    for j in str:
        if (str[i]==j):
            count += 1
    print(str[i],"is repeated", count)
    i+=1