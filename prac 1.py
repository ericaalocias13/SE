list_1 = []
list_2 = []
 
n = 1
a=1

for i in range(0, n):
    print("marks of chef-1 presentation:")
    ele = int(input())
    if ele <= 100 and 0 <= ele:
     list_1.append(ele)
    else:
        print("Marks should be between 1-100")
        print("marks of chef-1 presentation ",a,":")
        ele = int(input())
        list_1.append(ele)
    print("marks of chef-1 taste:")
    ele = int(input())
    if ele <= 100 and 0 <= ele:
     list_1.append(ele)
    else:
        print("Marks between 1-100")
        print("marks of chef-1 taste",a,":")
        ele = int(input())
        list_1.append(ele)
    
    print("marks of chef-1 hygiene:")
    ele = int(input())
    if ele <= 100 and 0 <= ele:
     list_1.append(ele)
    else:
        print("Marks between 1-100")
        print("marks of chef-1 hygiene",a,":")
        ele = int(input())
        list_1.append(ele)
    
a=a+1

for i in range(0, n):
    print("marks of chef-2 presentation:")
    ele = int(input())
    if ele <= 100 and 0 <= ele:
     list_2.append(ele)
    else:
        print("Marks should be between 1-100")
        print("marks of chef-2 presentation",a,":")
        ele = int(input())
        list_2.append(ele)
    print("Enter marks of chef-2 taste:")
    ele = int(input())
    if ele <= 100 and 0 <= ele:
     list_2.append(ele)
    else:
        print("Marks should be between 1-100")
        print("marks of chef-2 taste",a,":")
        ele = int(input())
        list_2.append(ele)
   
    print("marks of chef-2 hygiene:")
    ele = int(input())
    if ele <= 100 and 0 <= ele:
     list_2.append(ele)
    else:
        print("Marks should be between 1-100")
        print("marks of chef-2 hygiene",a,":")
        ele = int(input())
        list_2.append(ele)
    
print(list_1)
print(list_2)

c=0
d=0
x=[]
for i in range(0, len(list_1)):
    if list_1[i] > list_2[i]:
        c=c+1
        x.append(c)
    elif list_1[i]==list_2[i]:
        c=d=0
    else:
        d=d+1
        x.append(c)


print("Chef-1 score:",c,"Chef-2 score:",d)
d=[c,d]
print(d)
