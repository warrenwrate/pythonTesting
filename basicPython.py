

# basic loops
def basicloops():
    print("Hello World")

    mylist = [1, 2, 3, 4, 5]

    print("slice: ", mylist[1:4])

    for i in mylist:
        print("This is value of i", i)

    for j in range(0, len(mylist)):
        print("This is another but of the index:", j)

def basicString():
    myString = "hello world"
    print("Third index in myString", myString[3])
    for char in myString:
        print("looping through chars:", char)

def basicDictionary():
    myDictionary = dict()
    myDictionary[0] = "Warren"
    myDictionary[2] = "Wrate"

    print("my dictionary count",len(myDictionary))

    for key in myDictionary:
        print(f"{key} and {myDictionary[key]}")

    for i in range(0, 3):
        if i in myDictionary:
            print(f"found key:{i}, data:{myDictionary[i]}")
        else:
            print(f"could not find key:{i}")

basicloops()
basicString()
basicDictionary()
