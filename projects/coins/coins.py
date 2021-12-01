import json
from urllib.request import Request, urlopen
import urllib.error

#url that gets a list of all available symbols in Binance.com

coinstxt = "http://api.binance.com/api/v3/ticker/price"

# urllib gets the json from the url and stores it in the webpage variable

symbolReq = Request(coinstxt, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(symbolReq).read()

# loading/reading the json and stroing in it in symbolsJson var

symbolsJson = json.loads(webpage)

# Write/rewrite the coins.txt file everytime this app is run (This makes sure all the new currencies are also included)

with open("./coins.txt", 'w') as outfile:
    for coin in symbolsJson:
        outfile.write(coin['symbol'] + '\n')

# Prompt the user with info about the app

print("Welcome to Coins! Here you can check prices and information about your favourite digital currency with Binance's APIs")

while True:

    # Ask the user what coin they'd like to lookup.
    symbol = input ('Enter the Symbol of the currency you would like to check: ')

    # priceUrl gets the price of the coin the user had provided
    priceUrl = f"http://api.binance.com/api/v3/ticker/price?symbol={symbol}"

    # priceChnageUrl gets the price change and the price change percent of the coin
    priceChangeUrl = f"http://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"

    # urllib gets the json from the url and stores it in both of the variable below

    priceReq = Request(priceUrl, headers={'User-Agent': 'Mozilla/5.0'})
    priceChangeReq = Request(priceChangeUrl, headers={'User-Agent': 'Mozilla/5.0'})

    # try and parse through the json to get the info needed

    try: 
        prices = urlopen(priceReq).read()

        priceJson = json.loads(prices)

        priceChanges = urlopen(priceChangeReq).read()

        priceChangeJson = json.loads(priceChanges)

        print('The price of ' + symbol + ' is: ' + priceJson['price'])

        print('Price change of  ' + symbol + ' is: ' + priceChangeJson['priceChange'] + ', ' + 'with price change percent of: ' + priceChangeJson['priceChangePercent'])

        # After getting the info, prompt the user if they'd like to try again or if they're done.
        retry = input('Would you like to lookup another currency? (y/n) ')

        if (retry == "no" or retry == "n"):
            print('thank you for trying out Coins!')
            break
        elif (retry == "yes" or retry == "y"):
            continue


    # Exception handling if the user inputs a symbol that does not exist or if it's in lowercase.
    except urllib.error.URLError as e: print('Please check the symbol and try again.' +'\nThe symbol must be in UPPERCASE letters. You can check the list of availabe Symbols by viewing the "coins.txt" file located in the same folder')
    continue