row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

i = 0
column_selector = map[ ( int( position[i + 1] ) ) -1 ]
column_selector[ ( int( position[i] ) ) -1 ] = 'X'
          
print(f"{row1}\n{row2}\n{row3}")