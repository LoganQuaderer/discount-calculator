# Getting the original price from the user, using a float
original_price = float(input("Please enter the original price of the item: "))
# determine the discount percentage from the user.
discount_percentage = float(input("Enter the discount percentage: "))
# now we have to do the math and calculate the discount using the percentage 
amount_saved = original_price * (discount_percentage / 100)
# above is the formula to solve for the amount saved given the orginal price and discount percentage
# i made a new function to determine the new price from the original price and amount saved
new_price = {original_price - amount_saved}
print(f"Original Price: {original_price}")
print(f"Discount Percentage: {discount_percentage}")
print(f"Amount Saved: {amount_saved}")
print(f"New Price: {new_price}")