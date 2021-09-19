from win10toast import ToastNotifier
import schedule
import time

def job():
    toast = ToastNotifier()
    toast.show_toast("The Handy Meal", "It is time for you to go cooking", duration=20)

a = input('When do you want to be reminded to start cooking the lunch? ')

schedule.every().day.at(str(a)).do(job)

b = input ('When do you want to be reminded to start cooking dinner? ')

schedule.every().day.at(str(b)).do(job)

while True:
    schedule.run_pending()
    time.sleep(1)