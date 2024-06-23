from pynotifier import Notification
import psutil
import time

while True:
    battery = psutil.sensors_battery()
    percent = battery.percent

    print(percent)

    Notification(
        title="Battery Percentage",
        description=f"{percent}% Percent Remaining",
        duration=10
    ).send()

    time.sleep(20)
