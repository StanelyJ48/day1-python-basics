ticket_priority = "P2"
server_status = "Running"

if ticket_priority == "P1":
    if server_status == "Down":
        print("Escalate Immediately - Server is Down")
        print("Priority 1 - Escalate Immediately to L2 / L3 Support Teams")
    else:
        print("Escalate Immediately - Server is Running, Investigate the issue")

else:
    print("Follow Standard SLA Process - No Escalation Required")
 