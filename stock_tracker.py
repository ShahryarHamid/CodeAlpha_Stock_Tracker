stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "MSFT": 300,
    "AMZN": 140,
    "META": 310,
    "NFLX": 440,
    "NVDA": 700
}
portfolio={}
print("Welcome to the Stock Portfolio Tracker! ")
print("Available Stocks:",", ".join(stock_prices))
print("Type 'done' when finished.")
while True:
    stock=input("Enter Stock Name: ").upper()
    if stock=="DONE":
        break
    if stock in stock_prices:
        try:
            share=int(input(f"How many shares of {stock}? "))
            portfolio[stock]=share
        except ValueError:
            print("Invalid Quantity.Enter a number")
    elif stock not in stock_prices:
        print("Stock not available.Choose from available stocks ")
print("\nInvestemnt Summary:")
total=0
for stock,shares in portfolio.items():
    price = stock_prices[stock]
    value = price * shares
    total += value
    print(f"{stock}: {shares} shares x ${price} = ${value}")
print(f"\n Total Investment = ${total}")
with open("portfolio_summary.txt","w") as file:
    file.write("Investment Summary:\n")
    for stock,shares in portfolio.items():
        price = stock_prices[stock]
        value = price * shares
        file.write(f"{stock}:{shares} shares x ${price} = ${value}\n")
    file.write(f"\n Total Investment = ${total}\n")