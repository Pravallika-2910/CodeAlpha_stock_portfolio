#dictionary of stock names and stock prices
stock_prices={"AAPL":180,   #apple
              "TSLA":250,   #tesla
              "GOOG":140,   #alphabet
              "MSFT":300,   #microsoft
              "AMZN":130,   #amazon
              "NFLX":420,   #netflix
              "META":350,   #meta (facebook)
              "NVDA":480,   #nvidia
              "PYPL":65,    #paypal
              "V":240,      #visa
              "ORCL":115,   #oracle
              "MA":400,     #mastercard
              "ADBE":550    #adobe
              }

#reading no of stocks from the user
no_of_stocks=int(input("enter no of stocks:"))
total_value=0
stock_portfolio=[]

#loop to read stock_name , quantity and calculating total value
for i in range(no_of_stocks):
    stock_name=input("enter stock name:").upper()
    quantity=int(input(f"enter quantity of {stock_name}:"))
    if stock_name in stock_prices:
        stock_value=stock_prices[stock_name]*quantity
        total_value+=stock_value
        stock_portfolio.append((stock_name,quantity,stock_value))
    else:
        print(f"price for {stock_name} not found in dictionary")

#printing the result
print("--:portfolio result:--")
print("stock\tquantity\tvalue")
for stk,qty,value in stock_portfolio:
    print(f"{stk}\t{qty}\t\t{value}")
print(f"total investment:{total_value}")

#storing the result into a file name portfolio.csv
choice=input("do you want to store the result yes/no:").lower()
if choice=="yes":
    with open("portfolio.csv","w") as file:
        file.write("stock,quantity,value\n")
        for stk,qty,value in stock_portfolio:
            file.write(f"{stk},{qty},{value}\n")
        file.write(f"total investment,{total_value}\n")
    print("data saved to portfolio.csv")
