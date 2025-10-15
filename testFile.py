from CDLinkedList import CDLL

num_list = CDLL()
print(num_list)
print(num_list.isEmpty())
print(len(num_list))
num_list.append(1)
num_list.append(2)
num_list.append(3)
print(f"Length: {len(num_list)}")
print(num_list)
print("-"*50)
num_list.remove_by_index(4)
print(num_list)
num_list.remove_by_index(-1)
num_list.remove_by_index(1)
print(num_list)
num_list.prepend(4)
print(num_list)
print(len(num_list))

num_list.insert_after(1,5) #4 1 5 3
print(num_list)
print(len(num_list))
num_list.remove(3)
print(len(num_list))
print(num_list)
print("#"*50)

#num_list.reverse()
print(num_list)
num_list.insert_before(5,6)
print(num_list)
print(len(num_list))
print("=" *50)
#print(f"Position of 5: {num_list.search(5)}") #1
#print(f"Position of 10: {num_list.search(10)}") #-1

#num_list.remove_before(4) 
print(num_list)
print(len(num_list))

#num_list.remove_after(6)
print(num_list)
print(len(num_list))
#num_list.remove_after(5)
#num_list.remove_after(4)
print(num_list)
print(len(num_list))

