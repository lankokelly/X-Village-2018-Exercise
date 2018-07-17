import time
from datetime import date
from datetime import timedelta

def print_next_day():
    today = date.today()
    add_day = timedelta(days=1)  
    tomorrow = today + add_day
    print(tomorrow)
    
print_next_day()