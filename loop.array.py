# Function for question one
def create_array():
    user_array = []
    size = int(input("Enter the size of the array: "))
    print("Enter the element of the array:")
    for i in range(size):
        element = int(input(f"Enter element {i + 1}: "))
        user_array.append(element)
    return user_array

def index_array(arr):
    print("\n---Indexing Array---")
    if len(arr) > 0:
        print("First Element:", arr[0])    
        print("Last Element:", arr[-1])
    else:
        print("Array is empty")
        
def loop_array(arr):
    print("\n---Looping Array---")
    for num in arr:
        print(num)
 
def append_array(arr):
    append_element = int(input("\nEnter an element to append to the array:"))
    arr.append(append_element)
    print("Array after appending:", arr)
    
def extend_array(arr):
    additional_nmbers_str = input("Enter additional elements to extend the array(separated by spaces): ").split()
    additional_nmbers =[int(num) for num in additional_nmbers_str]
    arr.extend(additional_nmbers)
    print("Array after extending:", arr)
        
if __name__ == "__main__":
    my_array = create_array()
    
    index_array(my_array)
    
    loop_array(my_array)
    
    append_array(my_array)
    
    extend_array(my_array)

    
    


'''user_array = []
size = int(input("Enter the size of the array: "))
print("Enter the element of the array:")
for i in range(size):
    element = int(input(f"Enter element {i + 1}: "))
    user_array.append(element)
print("\n---Indexing Array---")
if len(arr) > 0:
    print("First Element:", user_array[0])    
    print("Last Element:", user_array[-1])
else:
#     print("Array is empty")

# print("\n---Looping Array---")
# for num in user_array:
#     print(num)

# append_element = int(input("\nEntr an element to append to the array:"))
# user_array.append(append_element)
# print("Array after appendin:", user_array)
    
# additional_nmbers_str = input("Enter additional elements to extend the array(separated by spaces): ").split()
# additional_nmbers =[int(num) for num in additional_nmbers_str]
# user_array.extend(additional_nmbers)
# print("Array after extending:", arr)'''