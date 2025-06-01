# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task using match-case based on priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Reminder: '{task}' has an unknown priority level"

# Check if the task is time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority in ["low", "medium", "high"]:
        message += ". Consider completing it when you have free time."

# Display the customized reminder
print("\n" + message)
