from ToDoTracker import ToDo

my_list = ToDo()

my_list.add_item("Go to Supermarket")
my_list.add_item("Finish grading")
my_list.add_item("Get haircut")
my_list.add_item("Pick up dress")
my_list.add_item("Fix sink")

print(f"Total items in my ToDo list: {len(my_list)}")
print (my_list)
print("="*50)
print(my_list.search("Paint room"))
print(my_list.search("Get haircut"))
print("@"*50)
my_list.remove("Call Cable company")
my_list.remove("Go to Supermarket")
my_list.remove("Pick up dress")
my_list.remove("Fix sink")
print(f"Total items in my ToDo list: {len(my_list)}")
print(my_list)
