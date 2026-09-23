snack_item = "Chocolate" # str is string
quantity = 50
price = 1.50
is_available = True

print(f"Variable: snack_item, Value: {snack_item}, Data Type: {type(snack_item)}")
print(f"Variable: quantity, Value: {quantity}, Data Type: {type(quantity)}")
print(f"Variable: price, Value: {price}, Data Type: {type(price)}")
print(f"Variable: is_available, Value: {is_available}, Data Type: {type(is_available)}")

topping = None 
print(type(topping))


total_bill = quantity * price
print("Total Bill: ", total_bill)
print("Sale Price: ", type(price - 1))

# floor division
print(100 // 3)

# exponentiation operator (power operator)
print(15 ** 5)

# Remainder operator (percentage)
print(type(10 % 4))


print("Is the price below 200 ?", price < 200)
print("More than 10 in stock ?", quantity > 10)
print("Price is exactly 1.5 ?", price != 1.5)

print(1 == "1")


shop_name = "Quick" + " " + "Bites"
print(shop_name)

shop_name = f"Quick Bites ({snack_item}) available here !"
print(shop_name)

print(len(shop_name))

print(shop_name[0:11]) #last index is not included :)

s = "Roll No: 59"
print(f"{s[9:11]}")
print(s[-2:])

a = 7
b = 10
temp = a
a = b
b = temp 
print(a,b)