def calculate_electronics_gst(a, b):
    return (a + b) * 1.18


def calculate_fashion_gst(c, d):
    return (c + d) * 1.13


def calculate_food_gst(e):
    return e * 1.07


def total_bill(a, b, c, d, e):
    electronics_total = calculate_electronics_gst(a, b)
    fashion_total = calculate_fashion_gst(c, d)
    food_total = calculate_food_gst(e)

    return electronics_total + fashion_total + food_total


def calculate_discounted_bill(a, b, c, d, e):
    total = total_bill(a, b, c, d, e)
    discount = total * 0.20

    return total - discount


if __name__ == "__main__":
    def read_number(prompt):
        while True:
            try:
                value = float(input(prompt))
                if value < 0:
                    print("Please enter a non-negative value.")
                    continue
                return value
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    a = read_number("Enter electronics item 1 price: ")
    b = read_number("Enter electronics item 2 price: ")
    c = read_number("Enter fashion item 1 price: ")
    d = read_number("Enter fashion item 2 price: ")
    e = read_number("Enter food item price: ")

    total = total_bill(a, b, c, d, e)
    discount = total * 0.20
    final_payable = calculate_discounted_bill(a, b, c, d, e)

    print(f"Total after GST = {total:.2f}")
    print(f"Discount = {discount:.2f}")
    print(f"Final payable amount = {final_payable:.2f}")