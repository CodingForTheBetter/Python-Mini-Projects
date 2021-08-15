#Two ways you can approach this!

#Method 1:

email = input("Enter Your Email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your username is '{username}' and your domain is '{domain_name}'")
print(format_)

#Method 2 (You can try this out yourself!):

#email = input("Enter Your Email: ").strip()
#username = email[:email.index('@')]
#domain = email[email.index('@') + 1:]
#print(f"Your username is {username} & domain is {domain}")



#Let's break this down!


#email = input("Enter Your Email: ").strip()

#Here, as usual, we are making use of input() function to get the input from the user in the form of string. We will store this input in the email variable.
#Also notice how we are making use of a strip() function. strip() function will remove any additional & unwanted spacing on both sides of strings. So that we can make sure that we have only the email in the input and not any unwanted spaces.


#username = email[:email.index('@')]
#domain = email[email.index('@') + 1:]

#Here we are slicing the user input to obtain the username and domain and ignore the rest.
#Let's see how it works.
#In case of username variable we only want to keep the part of the string which comes before @ and ignore the rest.
#Here we are making use of slicing operator : and index() function. index() function searches for the particular element or character within the string and lists it is associated with and return its index number.
#Let's consider the input is rishabh.singh@gmail.com, so when we write email[:email.index('@')]i, our index() function will interpret it as email[:13] as our @ is located at index 13. Now email[:13] knows that @ is located at index 13, so now it will keep the part before index 13 and discard the rest.
#This exact same process is followed for domain also.
#And now finally, let's print our output.


#print(f"Your username is {username} & domain is {domain}")

#We are making use of f-string, a new addition to Python 3 which allows us to directly place our variables in the output string. Feel free to make use of format() or old school + or , operators if you don't want to use f-string.