def Convert(i):
    if ((i//2) != 0):
        Convert(i//2)
        print(i%2, end=""),
    else:
        print(i % 2, end=""),
        
Convert(1024)