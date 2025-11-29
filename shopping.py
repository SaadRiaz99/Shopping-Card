print("-----------=4% Discount on Shopping of Rs.10000=-----------")

name = input("Enter Your Good Name: ")

print("-----------=Wellcome to Our Shop=-----------" , name)

items = {
    "flour": {
        "white": {"small": 250, "medium": 700, "large": 1200},
        "chaki": {"small": 360, "medium": 800, "large": 1300}
    },
    "milk": {
        "fresh": {"small": 60, "medium": 110, "large": 160},
        "powder": {"small": 80, "medium": 130, "large": 180}
    },
    "bread": {
        "white": {"small": 40, "medium": 70, "large": 100},
        "brown": {"small": 50, "medium": 80, "large": 120}
    },
    "rice": {
        "basmati": {"small": 120, "medium": 220, "large": 320},
        "sela": {"small": 130, "medium": 210, "large": 360}
    },
    "oil": {
        "Olivia": {"small": 400, "medium": 890, "large": 1560},
        "Eva": {"small": 355, "medium": 505, "large": 765}
    }
}

def show_items(items):
    print("\n Available Main Items:")
    for item in items.keys():
        print("-", item.title())

def add_to_cart(items, cart):
    while True:
        a = input("\nEnter item name (or 'done' to finish): ").lower()
        if a == "done":
            break
        if a not in items:
            print(" Item not found! Try again.")
            continue

        
        print(f"\nAvailable sub-types for {a.title()}:")
        for sub, sizes in items[a].items():
            size_prices = " | ".join([f"{sz}: Rs.{pr}" for sz, pr in sizes.items()])
            print(f" {sub.title()} → {size_prices}")

        sub = input("Enter sub-type: ").lower()
        if sub not in items[a]:
            print(" Invalid sub-type! Try again.")
            continue

        size = input("Enter size (small/medium/large): ").lower()
        if size not in items[a][sub]:
            print(" Invalid size! Try again.")
            continue

        try:
            qty = int(input("Enter quantity: "))
        except ValueError:
            print(" Quantity must be a number!")
            continue

        price = items[a][sub][size] * qty
        cart.append({
            "item": a,
            "sub": sub,
            "size": size,
            "quantity": qty,
            "price": price
        })

        print(f" Added {qty} x {size} {sub.title()} {a.title()} = Rs.{price}")

cart = []
show_items(items)
add_to_cart(items, cart)


print("\n Your Cart:")
total = 0
for i in cart:
    print(f"{i['quantity']} x {i['size']} {i['sub'].title()} {i['item'].title()} = Rs.{i['price']}")
    total += i['price']

if total >= 10000:
    dis = total * 0.04
else:
    dis = 0

final_total = total - dis

print("\n----------------------------")
print(f"Total = Rs.{total}")
print(f"Discount = Rs.{dis}")
print(f"Sub Total = Rs.{final_total}")
print("----------------------------")
print(f"Total Bill = Rs.{final_total}")
print("Thank You ", name , "For Your Shopping")
