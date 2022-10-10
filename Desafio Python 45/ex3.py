tab = int(input("Tabuada de qual número você deseja? "))

for num in range(10):
    print("%d * %d = %d" %(tab, num+1, tab*(num+1)))