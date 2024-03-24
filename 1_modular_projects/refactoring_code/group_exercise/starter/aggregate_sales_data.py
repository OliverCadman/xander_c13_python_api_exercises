import csv

data = []
total_sales = {}
total_revenue = {}

if __name__ == "__main__":

    with open("./sales_data_sample.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    # Calculate total quantity of sales
    for row in data:
        product = row["product_line"]
        quantity_sales = row["quantity_ordered"]
        total_sales[product] = total_sales.get(product, 0) + int(quantity_sales)

    # Calculate total revenue per product
    for row in data:
        product = row["product_line"]
        revenue = row["sales"]
        total_revenue[product] = total_revenue.get(product, 0) + float(revenue)
        total_revenue[product] = round(total_revenue[product], 2)

    # Write to CSV
    with open("./amount_sales_per_product.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Product", "Amount of Sales"])
        for product, sales in total_sales.items():
            writer.writerow([product, sales])

    with open("./amount_revenue_per_product.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Product", "Amount of Revenue"])
        for product, sales in total_revenue.items():
            writer.writerow([product, sales])
