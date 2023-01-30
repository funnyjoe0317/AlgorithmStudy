def move(no:int, x:int, y:int):
    if no>1:
        move(no-1,x,6-x-y)

    print()