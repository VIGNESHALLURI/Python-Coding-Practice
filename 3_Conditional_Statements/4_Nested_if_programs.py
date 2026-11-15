#Write a Python program to check username and password using nested if.
username = "admin"
password = "12345"
if username == "admin":
    if password == "12345":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")

#Write a Python program to check ATM withdrawal eligibility using nested if.
balance = 10000
amount = 5000
if amount > 0:
    if amount <= balance:
        print("Withdrawal successful")
    else:
        print("Insufficient balance")
else:
    print("Invalid withdrawal amount")

#Write a Python program to check job eligibility using nested if.
age = 24
degree = True
if age >= 21:
    if degree == True:
        print("Eligible for job")
    else:
        print("Degree is required")
else:
    print("Age requirement not satisfied")

#Write a Python program to check examination eligibility using nested if.
attendance = 85
fee_paid = True
if attendance >= 75:
    if fee_paid == True:
        print("Eligible for examination")
    else:
        print("Please pay examination fee")
else:
    print("Insufficient attendance")

#Write a Python program to check shopping discount using nested if.
amount = 6000
membership = True
if amount >= 5000:
    if membership == True:
        print("You received 20% discount")
    else:
        print("You received 10% discount")
else:
    print("No discount")

#Write a Python program to check driving licence eligibility using nested if.
age = 22
test_passed = True
if age >= 18:
    if test_passed == True:
        print("Licence approved")
    else:
        print("Driving test not passed")
else:
    print("Not eligible due to age")

#Write a Python program to check bank loan eligibility using nested if.
salary = 40000
credit_score = 750
if salary >= 25000:
    if credit_score >= 700:
        print("Loan eligible")
    else:
        print("Low credit score")
else:
    print("Salary requirement not satisfied")

#Write a Python program to check mobile unlocking using nested if.
pin = 1234
fingerprint = True
if pin == 1234:
    if fingerprint == True:
        print("Mobile unlocked")
    else:
        print("Fingerprint not matched")
else:
    print("Incorrect PIN")

#Write a Python program to confirm an online order using nested if.
stock = 10
payment = True
if stock > 0:
    if payment == True:
        print("Order confirmed")
    else:
        print("Payment pending")
else:
    print("Product out of stock")

#Write a Python program to check employee promotion using nested if.
experience = 5
performance = 90
if experience >= 3:
    if performance >= 80:
        print("Eligible for promotion")
    else:
        print("Performance score is insufficient")
else:
    print("Experience is insufficient")