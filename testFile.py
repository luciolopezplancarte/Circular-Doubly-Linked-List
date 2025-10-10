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


