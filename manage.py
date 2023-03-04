#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import threading
import datetime
import csv
from colorama import Fore, Style
from apscheduler.schedulers.background import BackgroundScheduler


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

jsondata = {}

def store():
    global jsondata
    now = datetime.datetime.now()
    filename = now.strftime("%d-%m-%Y") + ".csv"
    if not os.path.isfile(filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            temp=["Time","tempin", "tempout", "humidity", "windspeed", "winddir", "rainrate", "dew", "uv", "heat", "icon", "desc"]
            writer.writerow(temp)
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([now.strftime("%H:%M:%S")] + list(jsondata.values()))
    print(Fore.GREEN+"Saved tempin value at "+now.strftime("%d/%m/%Y %H:%M:%S")+Style.RESET_ALL)

scheduler = BackgroundScheduler()
scheduler.add_job(store, 'interval', seconds=1)

if __name__ == '__main__':
    scheduler.start()
    main()
