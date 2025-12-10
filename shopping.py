print("-----------=4% Discount on Shopping of Rs.10000=-----------")

name = input("Enter Your Good Name: ")

print("-----------=Wellcome to Our Shop=-----------" , name)

items = {
    "flour": {
        "white": {
            "maida": {"small": 140, "medium": 280, "large": 550},
            "fine_aata": {"small": 130, "medium": 260, "large": 520}
        },
        "chaki": {
            "aata": {"small": 120, "medium": 240, "large": 480},
            "multigrain": {"small": 160, "medium": 310, "large": 600}
        },
        "gram": {
            "besan": {"small": 150, "medium": 300, "large": 580},
            "sughar_free_besan": {"small": 170, "medium": 330, "large": 620}
        }
    },

    "milk": {
        "fresh": {
            "cow": {"small": 60, "medium": 110, "large": 160},
            "buffalo": {"small": 70, "medium": 130, "large": 180}
        },
        "powder": {
            "olpers": {"small": 80, "medium": 150, "large": 250},
            "nestle_nido": {"small": 100, "medium": 180, "large": 300}
        }
    },

    "bread": {
        "white": {
            "dawn": {"small": 40, "medium": 70, "large": 100},
            "british": {"small": 45, "medium": 75, "large": 105}
        },
        "brown": {
            "dawn_brown": {"small": 50, "medium": 80, "large": 120},
            "british_brown": {"small": 52, "medium": 85, "large": 125}
        }
    },

    "rice": {
        "basmati": {
            "super_karachi": {"small": 120, "medium": 230, "large": 350},
            "trophy": {"small": 140, "medium": 250, "large": 380}
        },
        "sela": {
            "guard_sela": {"small": 130, "medium": 220, "large": 360},
            "shahenshah": {"small": 135, "medium": 230, "large": 370}
        }
    },

    "oil": {
        "cooking_oil": {
            "dalda": {"small": 380, "medium": 820, "large": 1490},
            "habib": {"small": 370, "medium": 780, "large": 1420}
        },
        "ghee": {
            "dalda_ghee": {"small": 380, "medium": 750, "large": 1350},
            "ss_ghee": {"small": 350, "medium": 700, "large": 1300}
        }
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
