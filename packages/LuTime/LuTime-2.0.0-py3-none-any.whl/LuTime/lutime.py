"""
The EZTime module is an easy-to-use module for getting something related to the current time.
The only function in this module is the get() function!
"""

import datetime
import time


def get(obj):

    """
    The get function takes a string as an argument and checks if it is a valid time object and returns the value of the object.

    Parameters:
        obj/object: The object which should be one of the following:
            - "time"
            - "date"
            - "day/d"
            - "month/m"
            - "year/yr"
            - "hour/hr"
            - "minute/min"
            - "second/sec"
            - "microsecond/us"
            - "timestamp/ts"
            - "millisecond/ms"
            - "datetime/dt"

    Returns: A datetime/time object. For example: if you put time as an argument, it will return the current time as
    a datetime/time object.

    """

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

