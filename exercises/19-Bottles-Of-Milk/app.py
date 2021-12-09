def number_of_bottles():
    k=99
    while k>2:
        print(str(k)+ " bottles of milk on the wall, " +str(k)+" bottles of milk.")
        print("Take one down and pass it around, " +str(k-1)+" bottles of milk on the wall.")
        k=k-1
    print("2 bottle of milk on the wall, 2 bottles of milk.")
    print("Take one down and pass it around, 1 bottle of milk on the wall.")
    print("1 bottle of milk on the wall, 1 bottle of milk.")
    print("Take one down and pass it around, no more bottles of milk on the wall.")
    print("No more bottles of milk on the wall, no more bottles of milk.")
    print("Go to the store and buy some more, 99 bottles of milk on the wall.")

number_of_bottles()