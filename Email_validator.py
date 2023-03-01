'''Email Error 101 = Email length should be greater than 6'''
'''Email Error 102 = First Character of Email should be Alphabet'''
'''Email Error 103 = @ should be present in Email, only 1 @ should be there in a complete string'''
'''Email Error 104 = position of Dot "." should be -3 or -4. 
means either it could be .in or .com or .org, 
so in python if we check the indexing in reverse order it starts from -1 so in that case it could be either -3 or -4.'''
'''Email Error 105 = there should be no space in the email string, 
email should be in lower case, there can be a possibility of having a digit, 
there could be a possibility of having special character like "." or "_"."'''

email = input("Enter your Email: ")
j, k, l = 0, 0, 0
if len(email)>= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1): #we have used "and" operator here because "and" operator only returns the value if both the condition are TRUE. if condition become false it"ll give an Error. 
            if (email[-4]==".") ^ (email[-3]=="."): #we are using XOR "^" operator here because XOR operator returns the value even if one of the condition is TRUE. 
                for i in email:
                    if i==i.isspace():
                        j=1
                    elif i.isalpha(): # we using elif here because if space is not found in the string it'll check the next condition oe else it'll revert back.
                        if i==i.upper():
                            k=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        l = 1 
                if j==1 or k==1 or l==1:
                    print("Email Error 105")
                else:
                    print("Proper Email Format")
            else:
                print("Email Error 104")
        else:
            print("Email Error 103")
    else:
        print("Email Error 102")
    
else:
    print("Email Error 101")