def swapData():
    f1 = "code/file1.txt"
    f2 = "code/file2.txt"
    with open(f1, 'r') as a:
        read1 = a.read()
    with open(f2, 'r') as b:
        read2 = b.read()
    with open(f1, 'w') as a:
        a.write(read2)
    with open(f2, 'w') as b:
        b.write(read1)

    print("Data Swapped Successfully")
swapData()

