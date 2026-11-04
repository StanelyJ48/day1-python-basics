ticket_priority = "P3"
server_status = "Running"

if ticket_priority == "P1":
    if server_status == "Down":
        print("Escalate Immediately - Server is Down")
        print("Priority 1 - Escalate Immediately to L2 / L3 Support Teams")
    else:
        print("Escalate Immediately - Server is Running, Investigate the issue")

elif ticket_priority == "P2":
    if server_status == "Down":
        print("Escalate Immediately - Server is Down")
        print("Priority 2 - Escalate to L2 Support Team")
    else:
        print("Priority 2 - Resolve within SLA timeline")
    

else:
    print("Follow Standard SLA Process - No Escalation Required")
 