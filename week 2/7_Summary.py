#exercise answer : 
def ex1():
    database = [
        "dan"
        "daniel"
    ]

    def get_database():
        return database

    def add_user_to_database(username : str):
        database.append(username)

    def password_generator(username : str):
        return f"{username}{username.upper()}{'X' * len(username)}"

    def validate_credentials(username : str, password : str):
        bank_users = get_database()
        return username in bank_users and password == password_generator(username)

    def handle_login():
        print("\n\ntry to login")
        username = input("enter username : ")
        password = input("enter password : ")

        if(validate_credentials(username, password)):
            print(f"welcome {username}")
            return True
        else:
            print("wrong password or username")
            return False

    def handle_withdraw():
        amout = int(input("how much would you like to withdraw?\n"))
        if(amout > 500 or amout <= 0):
            print("withdraw denied")
        else:
            print(f"take your {amout} shekels")
            print(f"your balance is {500 - amout}")
    
    #test print :
    username = input("enter your username : ").strip()
    password = password_generator(username).strip()
    print(f"your password is : {password}")
    add_user_to_database(username)


    #login + withdraw part
    response = handle_login()
    if(response):
        handle_withdraw()

#ex1()


#exercise answer : 
def ex2():
    def time_shift(time : str, offset : int):
        hours = int(time.split(":")[0])
        minutes = int(time.split(":")[1])
        hours += offset
        return f"{(hours % 24):02d}:{minutes:02d}" #add 2 leading zeros

    def convert_to_timezone(time : str, zone : str):
        """conver current local time to another time zone

        Args:
            time (str): current time
            zone (str): new time zone from following list :
            ["TLV" "LDN" "NYC" "TYO"]

        Returns:
            str : current time in new timezone
        """

        if zone == "TLV":
            return time_shift(time, 3)
        elif zone == "NYC":
            return time_shift(time, -4)
        elif zone == "TYO":
            return time_shift(time, 9)
        return time

    time = input("enter current time in HH:MM format : ")
    zone = input("enter a timezone : ")
    print(f"time at timezone {zone} is {convert_to_timezone(time,zone)}")

#ex2()


#exercise answer : 
def ex3():
    def check_str_length(a : str, b : str):
        if len(a) == 0 or len(b) == 0:
            return "one one the string is empty"
        elif len(a) == len(b):
            return "same len"
        else: 
            return "not same len"

    a = input("enter str1 : ")
    b = input("enter str2 : ")
    print(check_str_length(a, b))

    