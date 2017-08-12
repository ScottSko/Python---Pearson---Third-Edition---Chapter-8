def main():

    user_date = input("Please enter the date in the form of mm/dd/yyyy: ")

    date_list = user_date.split("/")

    month = ""

    if date_list[0] == "01":
        month = "January"
    if date_list[0] == "02":
        month = "February"
    if date_list[0] == "03":
        month = "March"
    if date_list[0] == "04":
        month = "April"
    if date_list[0] == "05":
        month = "May"
    if date_list[0] == "06":
        month = "June"
    if date_list[0] == "07":
        month = "July"
    if date_list[0] == "08":
        month = "August"
    if date_list[0] == "09":
        month = "September"
    if date_list[0] == "10":
        month = "October"
    if date_list[0] == "11":
        month = "November"
    if date_list[0] == "12":
        month = "December"

    print("The date is", month + " " + date_list[1] + ", " + date_list[2])

main()