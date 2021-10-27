import json
import csv
import urllib.request

# Ask user for an api endpoint to recieve the json data
user_url = input ('Enter the url endpoint of an api: ')

# Ask user to enter the local path where the CSV file will be saved at
user_local_path = input ('Enter the local path you would like the csv file to be saved at: ')

# Ask user to enter the name of the file that is going to be created
file_name = input ('Enter the name for the new file that is going to be created: ')

# urllib gets the json from the url and stores it in the response variable
response = urllib.request.urlopen(user_url)

# loading/reading the json and stroing in it in data var
data = json.loads(response.read())


#Open a local file and write as a csv file
with open(f"{user_local_path}/{file_name}.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    for key, value in data.items():
        writer.writerow([key, value])

print("The csv file has been saved at the location you provided!")

