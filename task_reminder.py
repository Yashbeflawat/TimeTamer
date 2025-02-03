import schedule
import time
from datetime import datetime
from plyer import notification

# Define your tasks (customize this as needed)
def wake_up():
    send_notification("Reminder", "⏰ Time to wake up and start your day!")

def hydrate():
    send_notification("Reminder", "💧 Drink water to hydrate.")

def exercise():
    send_notification("Reminder", "🏃‍♂️ Time for some exercise!")

def work_on_tasks():
    send_notification("Reminder", "💻 Focus on important work tasks.")

def take_break():
    send_notification("Reminder", "☕ Take a short break. Relax for 10 minutes.")

def wind_down():
    send_notification("Reminder", "🛋 Start winding down for the night.")

def sleep():
    send_notification("Reminder", "🌙 Time to sleep. Rest well!")

# Function to send notifications
def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Time the notification stays on screen (in seconds)
    )

# Define a function to schedule tasks
def create_schedule():
    schedule.every().day.at("07:00").do(wake_up)
    schedule.every().day.at("07:30").do(hydrate)
    schedule.every().day.at("08:00").do(exercise)
    schedule.every().day.at("09:00").do(work_on_tasks)
    schedule.every().day.at("12:00").do(take_break)
    schedule.every().day.at("13:00").do(work_on_tasks)
    schedule.every().day.at("18:00").do(take_break)
    schedule.every().day.at("20:00").do(wind_down)
    schedule.every().day.at("22:00").do(sleep)

# Run the scheduler continuously
def run_scheduler():
    create_schedule()
    while True:
        schedule.run_pending()  # Check for pending tasks and run them
        time.sleep(60)  # Wait for a minute before checking again

# Start the program
if __name__ == "__main__":
    print(f"Program started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    run_scheduler()
