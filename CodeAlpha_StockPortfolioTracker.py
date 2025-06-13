import matplotlib.pyplot as plt
# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 310
}
# Get user input
portfolio = {}
while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found. Available options:", ", ".join(stock_prices.keys()))
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")
# Calculate total investment and prepare for chart
total_value = 0
values = []
labels = []

print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")
    values.append(value)
    labels.append(stock)
print(f"\nTotal Investment Value: ${total_value}")
# Optional: Show Pie Chart
show_chart = input("Would you like to see a portfolio chart? (yes/no): ").lower()
if show_chart == "yes":
    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Stock Portfolio Distribution")
    plt.axis("equal")
    plt.show()
