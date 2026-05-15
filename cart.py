cart =[]
while True:
    item = input("add item (or type quit):")
    if item == "quit":
        break
    cart.append(item)

print("your cart:")

for item in cart:
    print(item)
print("total items",len(cart))
