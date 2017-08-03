 #This will help calculate how much it will cost to paint a wall.
 #practice/wall-painting.py
 #Ochsenbein, Alexis

# Setup
sqft_Per_Gallon = 400

#Input

print(" Hello, please tell me the width of the wall in feet.")
wall_Width = int(input())
print(" Great, now tell me the height of the wall in feet.")
wall_Height = int(input())
print("Perfect, now tell me how much one gallon of paint costs.")
paint_Cost_Per_Gallon = int(input())

# Transform
wall_Size = wall_Width * wall_Height
gallons_of_paint = float(wall_Size / sqft_Per_Gallon)
price_total = gallons_of_paint * paint_Cost_Per_Gallon

#output
print( "It will cost $" + str(price_total) + " and you will need " + str(gallons_of_paint) + " gallons of paint" "")
