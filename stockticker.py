#dictionary of stocks with prices
stocks_dict = {
	"DIS": "34.22",
	"NFLX" : "27.22",
	"SONY" : "25.15",
	"AMZN" : "32.44",
	"TM" : "19.60",
	"AAPL" : "50.15",
	"PETM" : "28.67",
	"ABC" : "64.99",
	"C" : "15.09",
	"COST" : "32.99"
}
x = input("Please enter your stock symbol: ") #collects value from user
stock_result = stocks_dict.get(x.upper()) #defines result from user as needed to search dictionary and capitalizes result so it matches dictionary
if stock_result is not None: #tells program what to print with a valid input from user
	print(f"The value of {x.upper()} is {stock_result} USD.")
else: #tells program what to print with invalid input from user
	print(f" {x} is not found.")