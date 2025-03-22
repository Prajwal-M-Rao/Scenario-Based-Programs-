#Scenario 1: Texting msg to your BF/GF
# user I/P: ask user the what's app "online"/"offline"
#
#   "online:" && and the tick status:
#       double tick grey--> Ignoring your msg
#       double tick blue--> seen your msg
#
#  "offline"
#       single tick --> Msg sent
#
# you will call

line=input("Enter the input\nonline\noffline\n")
if line=='online':
    tick=int(input("Enter the tick status \n1.grey\n2.blue\n"))
    if tick==1:
        print("Ignoring your message")
    else:
        print("Seen your message")
else:
    print("Offline\n Message sent")
print("Make a call")