from datetime import datetime, timedelta

def calculate_time_since_quit(quit_date):
    # Current date and time
    current_time = datetime.now()

    # Time since you quit
    time_since_quit = current_time - quit_date

    # Calculate days, hours, minutes, and seconds
    days = time_since_quit.days
    hours, remainder = divmod(time_since_quit.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return days, hours, minutes, seconds

if __name__ == "__main__":
    # Your quit date (Year, Month, Day)
    quit_date = datetime(2023, 9, 1)

    days, hours, minutes, seconds = calculate_time_since_quit(quit_date)

    print(f"Time since you quit smoking: {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")

