task = input("Enter your task:")
priority =input("high/medium/low").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task "
    case "medium":
        reminder = f"'{task}' is a medium priority task "
    case "low":
        reminder = f"'{task}' is a low priority task "
    case _:
        reminder = f"'{task}' has an unknown priority "


if time_bound == "yes":
    reminder += "that requires immediate attention today!"
else:
    reminder += "consider completeing it when you have free time."


print(f"Reminder: {reminder}")