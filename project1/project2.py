import json
from urllib.request import Request, urlopen


print("Welcome! If you're wondering what happened on a specific day every year, you're in the right place!")

# Ask user to enter the local path where the CSV file will be saved at
user_local_path = input ('Enter the local path you would like the csv file to be saved at: ')

# Ask user to enter the name of the file that is going to be created
file_name = input ('Enter the name for the new file that is going to be created: ')

# Three different types of inforamtion can be requested: 
types = {"1": "events", "2": "births", "3": "deaths"}

#Asking users what type of request they want
while True:
    option = input(""" Choose the type of your request,
     option 1 - Events
     option 2 - Births
     option 3 - Deaths
     type the number of the option above please > """)
     
    if option not in types:
         print("invalid option please choose again")
         continue

    chosen_type = types[option]
    break


# Asking users for the day and month of hte request
while True:
    try:
        day = int(input('Enter the day in numbers and between 1 - 31: '))

        if day <= 0 or day >=32:
            print("Please enter a day between 1 and 31")
            continue
        else:
            break
        
    except ValueError:
        print("Please input a valid number")

while True:
    try:    
        month = int(input('Enter the month in numbers between 1 - 12: '))

        if month <= 0 or month >=13:
            print("Please enter a month between 1 and 12")
            continue
        else:
            break

    except ValueError:
        print("Please input a valid number")

url = f"https://byabbe.se/on-this-day/{day}/{month}/{chosen_type}.json"

# urllib gets the json from the url and stores it in the webpage variable

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

# loading/reading the json and stroing in it in data var

prettyJSON = json.loads(webpage)

# Print the json in a readable format
print(json.dumps(prettyJSON, indent=4, sort_keys=True))

# Create a new txt file with all the info for easier reads
with open(f"{user_local_path}/{file_name}.txt", 'w') as outfile:
    json.dump(prettyJSON, outfile, indent=4, sort_keys=True)


print("The txt file has been saved at the location you provided!")



