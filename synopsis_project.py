from datetime import datetime

TIME_FORMAT = "%H:%M"

meetings = []

def parse_time(time_str):
    return datetime.strptime(time_str, TIME_FORMAT)

def is_valid_time(time_str):
    try:
        parse_time(time_str)
        return True
    except ValueError:
        return False 

# Function to check if two meetings overlap
def check_overlap(new_start, new_end, existing_start, existing_end):
    new_start_dt = parse_time(new_start)
    new_end_dt = parse_time(new_end)
    existing_start_dt = parse_time(existing_start)
    existing_end_dt = parse_time(existing_end)

    return new_start_dt < existing_end_dt and new_end_dt > existing_start_dt

def add_meeting():
    title = input("What is the title of your meeting ?: ")

    while True:
        start_time = input("Enter the time the meeting starts (HH:MM): ")
        end_time = input("Enter the time it ends (HH:MM): ")

        if not (is_valid_time(start_time) and is_valid_time(end_time)):
            print("Auch , wrog format , please use the format HH:MM.")
            continue

        if parse_time(start_time) >= parse_time(end_time):
            print("Please make sure the start time is before the end time.")
            continue

        for meeting in meetings:
            if check_overlap(start_time, end_time, meeting['start_time'], meeting['end_time']):
                print(f"This meeting overlaps with '{meeting['title']}'. Please choose a different time.")
                break
        else:
           
            meetings.append({'title': title, 'start_time': start_time, 'end_time': end_time})
            print("Your meeting has been added successfully!")
            break
def display_meetings():
    print("\nHere are your scheduled meetings:")
    if not meetings:
        print("Nothing schedualed ")
    else:
        for m in sorted(meetings, key=lambda x: x['start_time']):
            print(f"{m['title']} | {m['start_time']} - {m['end_time']}")

# Main loop to run the program
def main():
    print("Welcome to the Meeting Scheduler! Let's get started.")
    while True:
        action = input("\nType 'add' to schedule a new meeting, or 'quit' to exit the program: ").lower()
        if action == 'add':
            add_meeting()
        elif action == 'quit':
            print("Thx for using the Meeting Scheduler. Here are your meetings listed:")
            display_meetings()
            break
        else:
            print(" Try again . Type 'add' to schedule a meeting or 'quit' to exit.")

if __name__ == "__main__":
    main()
