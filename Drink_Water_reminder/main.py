import time

from plyer import notification

while True:
    print("Drink Water Reminder")

    notification.notify(title = "It's time to drink water!", message = "Stay hydrated and healthy!", app_icon = r"C:\Users\HP\OneDrive\Documents\GitHub\Games-of-python\Drink_Water_reminder\favicon.ico", timeout = 10, toast= False)

    time.sleep(60*60) 