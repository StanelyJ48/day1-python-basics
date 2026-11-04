# name = "Stanely"
# target_role = "AI Engineer"
# current_skill = "Python"
# age = 29
# study_days=42
# daily_hours = 3.4
# isLearning_python=True

# # print("Welcome to my AI journey")
# # print("My target role:", name)
# # print("I am learning:", current_skill)
# # print("Daily study hours", daily_hours)

# print (name, type(name))
# print (age, type(age))
# print (study_days, type(study_days))
# print (isLearning_python, type(isLearning_python))
# print (daily_hours, type(daily_hours))


escalation_priority = {"P1":"Urgent", "P2":"High", "P3":"Medium", "P4":"Low"}

ticket_priority = "P5"

if ticket_priority == "P1":
    print(escalation_priority[ticket_priority],":", "Prority 1 - Escalate Immediately")
elif ticket_priority == "P2":
    print(escalation_priority[ticket_priority],":", "Priority 2 - Resolve within SLA timeline")
elif ticket_priority == "P3":
    print(escalation_priority[ticket_priority],":", "Priority 3 - Resolve within the working hours")
elif ticket_priority == "P4":
    print(escalation_priority[ticket_priority],":", "Priority 4 - Handle this when available")

else:
    print("Invalid Ticket Property")

