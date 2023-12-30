# 1. Expected output: 
# result = [10, 501, 22, 37, 100, 999, 87, 351]

#3. Fibonacci series 1 to 50:

def fibonacci(n):
    f1 = 0
    f2 = 1
    
    for i in range(1, n+1):
        yield f1
        f1 , f2 = f2 , f1+f2

for i in fibonacci(50):
    print(i)


#4. Regular Expression:

# a. Email address:


# 4.a. Validate email address:

import re

def Validate_email(email):

    pattern = "^[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z]{2,4}"

    output = re.search(pattern, email)

    if output is not None:
        return True
    
    else:
        return False

print(Validate_email("abcd567@gmail.com"))

# 4. b. Mobile numbers of Bangladesh:

import re

def Bangladesh_mobileNum(mobile_num):

    pattern = "^01[0-9]{9}"

    result = re.search(pattern,mobile_num)

    if result is not None:
        return True
    else:
        return False

print(Bangladesh_mobileNum("01123456789"))
print(Bangladesh_mobileNum("0112345678"))
print(Bangladesh_mobileNum("08123456789"))


# 4. c. Telephone numbers of USA assuming country code as +1 and then ten digits:

import re

def USA_TelephoneNum(Tele_num):

    pattern = "^[+1]+[0-9]{10}"

    result = re.search(pattern,Tele_num)

    if result is not None:
        return True
    else:
        return False

print(USA_TelephoneNum("+11234567890"))
print(USA_TelephoneNum("01123456789"))

#4.c. 16 digit password:

import re

def validate_password(password):

    pattern = "[\a-zA-Z0-9]{16}"
    output = re.search(pattern,password)

    if output is not None:
        return True
    else:
        return False

print(validate_password("abc123_@np09uASF"))
print(validate_password("abc123&%np09uASF"))



    

















    


    


