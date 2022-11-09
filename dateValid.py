# dateValid.py
# Colleen Westerhaus
# This program will ask the user for a date and return if it is valid or not

def main():
    date = input("Enter the date as (x)x/x/xx")
    date = date.split("/")
    if int(date[1]) <= 0 or int(date[1]) > 31 or int(date[0]) <= 0 or int(date[0]) > 12:
        print("This date in invalid because there is no such thing as this date.")
    elif int(date[1]) <= 28:
        print("This date is valid because all months have dates 1-28")
    elif int(date[1]) <= 30 and int(date[0]) == (1,3,4,5,6,7,8,9,10,11,12):
        print("This date is valid because it isn't in February.")
    elif int(date[1]) <=31 and int(date[0]) == (1,3,5,7,8,10,12):
        print("This date is valid because it is in a month that has 31 days.")
    else:
        print("This date is invalid because the day exists in some months but not the month you chose.")
main()
