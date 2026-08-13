customer_name=input("Enter customer name:".capitalize())
product_name=input("Enter product name:".capitalize())
feedback=input("Enter your feedback:".capitalize())



print("========using different function============".upper())
customer_name=customer_name.strip().title()
product_name=product_name.strip().title()
feedback=feedback.capitalize().strip()
print("split function:",customer_name.split())
print("count function:",feedback.count("f"))
print("replace function:",feedback.replace("good","bad"))
print("ljust function:",feedback.ljust(20))
print("rjust function:",feedback.rjust(20))


print("================feedback=================".center(50).upper())
print("Customer Name:",customer_name.upper())
print("Product Name:",product_name.upper())
print("Feedback:",feedback.upper())

print("=========thankyou for your feedback=======".center(50).upper())