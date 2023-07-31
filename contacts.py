contacts = {
    "number": 4,
    "students": [
        {"name": "Dheeraj", "email": "emailoneexample.com"},
        {"name": "Harry Potter", "email": "email2example.com"},
        {"name": "Mounika", "email": "email3example.com"},
        {"name": "Dheera", "email": "email4example.com"},
    ]
}

print("Student Emails:")
for student in contacts["students"]:
    print(student["email"])
