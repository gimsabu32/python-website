print('hello world')



try:
    myName , myAddress = input("Please your name and address:").split()



    myAge = int(input("Please enter your Age:"))
    x = "Hello" + 5
    print("Your name is: ", myName)
    print("Your age is: ", myAge)
    print("Your address is: ", myAddress)


    print("*************************") 
    print("*************************")

except ValueError:
    print("Ages should only in number. Please try again.")
    
    myAge = input("Please enter your Age:")


    print("Your age is: ", myAge)


    print("Your name is: ", myName)
    print("Your age is: ", myAge)
    print("Your address is: ", myAddress)
    
except TypeError:
        print("You Can't add a word to number")

        print(x)
except:
    print("Please Enter Your Name and Your Address again")
    myName , myAddress = input("Please your name and address:").split()
    
    myAge = input("Please enter your Age:")


    print("Your name is: ", myName)
    print("Your age is: ", myAge)
    print("Your address is: ", myAddress)
    
    
    
    
    