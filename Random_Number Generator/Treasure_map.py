# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# row = [int(a) for a in str(position)]
# k = row[0]
# l = row[1]
# map[l-1][k-1] = "x"
# ************** or we write like this**********
row = int(position[0])
column =int(position[1])
#** position are string so we have to make integer here**
selected_column = map[column-1]
selected_column[row-1]='x'



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")