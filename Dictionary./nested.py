#nested dict

student={
    "name":"balwinder kaur",
    "subject":{
        "physics":"56",
        "chemis":"78"
    }
}
print(student)
print(type(student))
print(student["name"])
print(student["subject"]["chemis"])
print(len(student))
