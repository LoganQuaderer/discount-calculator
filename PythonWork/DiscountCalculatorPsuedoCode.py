## I need to ask the user for the price of a item as well as the discount amount and figure out what the price comes out to as well as show how much they saved
# Step 1: Get the original price from the user
original_price = input("Enter the original price of the item: ")

# Step 2: Get the discount percentage from the user
discount_percentage = input("Enter the discount percentage: ")

# Step 3: Calculate the amount saved
amount_saved = (original_price * (discount_percentage / 100))

# Step 4: Calculate the discounted price
discounted_price = original_price - amount_saved

# Step 5: Display the results
print("Original Price: ", original_price)
print("Discount Amount: ", amount_saved)
print("Price After Discount: ", discounted_price)
