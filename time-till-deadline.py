from datetime import datetime

user_input = input("Enter your goal a deadline separated by colon.\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]


#while user_input != "exit" :

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
time_till = deadline_date - today_date
print(f"dear user! Time Remaining For your goal: {goal} is {time_till.days}")


