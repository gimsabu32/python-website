#1. Write a program in python to display the first 10 natural numbers. Expected Output : 1 2 3 4 5 6 7 8 9 10
print("******Ans. no. 1 *************")  
Natural = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(Natural)):
    print(Natural[i], end=" ")
print()


    
print("******Ans. no. 2 *************")    
#2. Write a python program to find the sum of first 10 natural numbers. Expected Output : The first 10 natural number is : 1 2 3 4 5 6 7 8 9 10 The Sum is : 55
print(sum(Natural))

print("******Ans. no. 3 *************") 
#3. Write a program in python to display n terms of natural number and their sum. Test Data : 7 Expected Output : The first 7 natural number is :1 2 3 4 5 6 7. The Sum of Natural Number upto 7 terms : 28
print("The First Natural Numbers are: ")
for i in range(Natural[6]):
    print(Natural[i], end=" ")
print()
print("The sum of the first natural numbers upto 7 terms: ", sum(Natural[:7]))

print("******Ans. no. 4 *************")  
#4. Write a program in python to read 10 numbers from keyboard and find their sum and average. Test Data : Input the 10 numbers : Number-1 :2 ... Number-10 :2 Expected Output : The sum of 10 no is : 51 The Average is : 5.100000
Nums = float(input("Enter 10 numbers: ").split())


print(sum(Nums))

print("******Ans. no. 5 *************")  
#5. Write a program in python to display the cube of the number upto given an integer. Test Data : Input number of terms : 5 Expected Output : Number is : 1 and cube of the 1 is :1 Number is : 2 and cube of the 2 is :8 Number is : 3 and cube of the 3 is :27 Number is : 4 and cube of the 4 is :64 Number is : 5 and cube of the 5 is :125 
