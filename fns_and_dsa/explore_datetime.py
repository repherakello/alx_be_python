from datetime import datetime, timedelta

def display_current_datetime():

    current_date = datetime.now()

    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Current date and time: {formatted_date}")


def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))

    current_date = datetime.now()

    future_date = current_date + timedelta(days=days_to_add)

    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")


if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date