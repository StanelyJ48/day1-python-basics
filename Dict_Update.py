employee ={
    "name": "Stanely",
    "age": 25,
    "role": "Technical Support Engineer",
    "Salary": 50000
}

employee["role"] = "AI Engineer"
employee["Salary"] = 60000
employee["location"] = "Vijayawada"
employee["experience"] = 5

print(employee["name"] + " is an " + employee["role"]+" and he is living in "+employee["location"]+". He has "+str(employee["experience"])+" years of experience and his salary is "+str(employee["Salary"]))