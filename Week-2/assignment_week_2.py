#################################################
#1.create an empty list called my_list
my_list = []

#2.Append the elements to the list:10,20,30,40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)#output: [10,20,30,40]

#3.Insert 15 at the second position in the list
my_list.insert(1,15)
print(my_list)#output: [10,15,20,30,40]

#4.Extend my_list with another list:[50,60,70]
my_list.extend([50,60,70])
print(my_list)#output:[10,15,20,30,40,50,60,70]

#5.Remove the last element from the list
my_list.pop()
print(my_list)#output:[10,15,20,30,40,50,60]

#6.sort my_list in ascending order
my_list.sort()
print(my_list)#output:[10,15,20,30,40,50,60]

#7.Find and print the index of 30 in the list
print(my_list.index(30))#output:3

