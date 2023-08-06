import datetime
import time


def get(obj):

    if type(obj) != str:
        print("Error: get() requires a string as input.")
        return None

    obj = obj.lower()

    if obj == "second" or obj == "sec":
        return datetime.datetime.now().second
    elif obj == "minute" or obj == "min":
        return datetime.datetime.now().minute
    elif obj == "hour" or obj == "hr":
        return datetime.datetime.now().hour
    elif obj == "day" or obj == "d":
        return datetime.datetime.now().day
    elif obj == "month" or obj == "m":
        return datetime.datetime.now().month
    elif obj == "year" or obj == "yr":
        return datetime.datetime.now().year
    elif obj == "date":
        return datetime.datetime.now().strftime("%d/%m/%Y")
    elif obj == "time":
        return datetime.datetime.now().strftime("%H:%M:%S")
    elif obj == "datetime" or obj == "dt":
        return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    elif obj == "timestamp" or obj == "ts":
        return time.time()
    elif obj == "millisecond" or obj == "ms":
        return datetime.datetime.now().microsecond / 1000
    elif obj == "microsecond" or obj == "us":
        return datetime.datetime.now().microsecond
    else:
        return "Invalid input for get function from SimpleTime module."
