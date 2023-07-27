# Program Description: One  Stop Insurance  Company

# Author: Oleksandr Dmitriiev

# Date Written: July 16th - July 26th 2023

import matplotlib.pyplot as plt

def get_sales_data():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sales_data = []

    for month in months:
        while True:
            try:
                sales = float(input(f"Enter total sales for {month}: $"))
                if sales >= 0:
                    sales_data.append(sales)
                    break
                else:
                    print("Sales amount cannot be negative. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid sales amount.")

    return months, sales_data

def plot_sales_graph(months, sales_data):
    plt.figure(figsize=(10, 6))
    plt.bar(months, sales_data, color='skyblue', edgecolor='black', linewidth=1)
    plt.xlabel("Months")
    plt.ylabel("Total Sales ($)")
    plt.title("Total Sales by Month")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    print("Enter total sales for each month:")
    months, sales_data = get_sales_data()
    plot_sales_graph(months, sales_data)

if __name__ == "__main__":
    main()
