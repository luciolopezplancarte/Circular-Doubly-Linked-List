from CDLinkedList import CDLL

num_list = CDLL()
print(num_list)
print(num_list.isEmpty())
print(len(num_list))
num_list.append(1)
num_list.append(2)
num_list.append(3)
num_list.append(4)
num_list.prepend(5)

print(f"Length: {len(num_list)}")
print(num_list)
print("-"*50)

