import csv

# Hardcoded stock prices (per share)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330,
    "AMZN": 125,
}


def get_portfolio():
    """Ask the user for stock names and quantities until they type 'done'."""
    portfolio = {}  # stock name -> quantity

    print("Available stocks and prices:")
    for name, price in STOCK_PRICES.items():
        print("  " + name + ": $" + str(price))
    print("\nEnter a stock name and quantity. Type 'done' when finished.")

    while True:
        name = input("\nStock name: ").upper().strip()

        if name == "DONE":
            break

        if name not in STOCK_PRICES:
            print("Sorry, '" + name + "' is not in the price list.")
            continue

        qty_text = input("Quantity of " + name + ": ").strip()
        if not qty_text.isdigit() or int(qty_text) <= 0:
            print("Please enter a whole number greater than 0.")
            continue

        # Add to existing quantity if the stock was already entered
        portfolio[name] = portfolio.get(name, 0) + int(qty_text)
        print("Added " + qty_text + " share(s) of " + name + ".")

    return portfolio


def show_summary(portfolio):
    """Print each holding and the total investment. Returns (rows, total)."""
    rows = []
    total = 0

    print("\n=== Investment Summary ===")
    print("{:<8}{:>10}{:>10}{:>14}".format("Stock", "Price", "Qty", "Value"))
    for name, qty in portfolio.items():
        price = STOCK_PRICES[name]
        value = price * qty
        total += value
        rows.append([name, price, qty, value])
        print("{:<8}{:>10}{:>10}{:>14}".format(name, "$" + str(price), qty, "$" + str(value)))

    print("-" * 42)
    print("Total investment: $" + str(total))
    return rows, total


def save_to_csv(rows, total, filename="portfolio.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Price", "Quantity", "Value"])
        writer.writerows(rows)
        writer.writerow(["TOTAL", "", "", total])
    print("Saved to " + filename)


def main():
    print("=== STOCK TRACKER ===")
    portfolio = get_portfolio()

    if not portfolio:
        print("\nNo stocks entered. Goodbye!")
        return

    rows, total = show_summary(portfolio)

    save = input("\nSave result to portfolio.csv? (y/n): ").lower().strip()
    if save == "y":
        save_to_csv(rows, total)


if __name__ == "__main__":
    main()
