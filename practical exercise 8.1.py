def sanitize_name(first_name, last_name):
    first_name = first_name.strip().title()
    last_name = last_name.strip().title()
    return f"{first_name} {last_name}"


first = input("Enter your first name: ")
last = input("Enter your last name: ")

full_name = sanitize_name(first, last)
print("Clean name:", full_name)