

#
myShoppingitems = ["Banana", "Oninon", 3, 1, 3, 4, 5, 6, 2, 7, 7, 8,  9, 34, 65, 35]
nums = [3, 1, 3, 4, 5, 6, 2, 7, 7, 8,  9, 34, 65, 35]
nums.sort()
#to sort the numbers orderly use the .sort()
#to know the maximum number use the print(max(nums()))
#for the minimum use print(min(nums))
#to fin the sum/ the addition of the total numbers use print(sum(nums))
print(nums)

    
myShoppingitems.append("Apple")
    
myShoppingitems.insert(2, "Orange")
    
myShoppingitems.remove("Orange")
myShoppingitems.remove(3)

    
print(len(myShoppingitems))

for i in range(len(myShoppingitems)):
    print(myShoppingitems[i])
    
    
x = 0
while x < len(myShoppingitems):
    print(myShoppingitems[x])
    x = x + 2