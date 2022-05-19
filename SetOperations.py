# to create ADT that emplement set operations ADD,Remove,Present,size
# ,Return,union,difference,subset

listsize=int(input("Enter list size : "))
a = set([input(f"Enter element {i+1} of a : ")for i in range(listsize)])
b = set([input(f"Enter element {i+1} of b : ")for i in range(listsize)])

def add():
    n=int(input("Enter number to add : "))
    ch1=int(input("[1] Add element in a\n[2] add element in b\n"))
    if ch1==1:
        a.add(n)
        print(f"a after adding {n} is {a}")
    elif ch1==2:
        b.add(n)
        print(f"b after adding {n} is {b}")

def rem():
    n=int(input("Enter element to remove : "))
    ch1=int(input("[1] remove from a\n[2] remove from b\n"))
    if ch1==1:
        a.remove(n)
        print(f"a after removing {n} is : {a}")
    elif ch1==2:
        b.remove(n)
        print(f"b after removing {n} is : {b}")

def pres():
    n=input("Enter number to check : ")
    print(f"{n} present in a :",n in a)
    print(f"{n} present in b :",n in b)

def length():
    print(f"Lenth of a : {len(a)}")
    print(f"Lenth of b : {len(b)}")

def union():
    print(f"Union of sets : {a | b}")

def inter():
    print(f"Intersection of sets : {a & b}")

def diff():
    print(f"Difference of sets : {a-b} & {b-a}")

def subset():
    print(f"Subset of set : {a^b}")
run=True
while run:
    print("-----menu-----")
    print("[1] Add Element")
    print("[2] Remove element")
    print("[3] Check present or not")
    print("[4] Size of list")
    print("[5] Union")
    print("[6] Intersaction")
    print("[7] Difference")
    print("[8] subset")
    print("[9] Exit")
    print("")
    ch=int(input("Enter your choice : "))
    if ch==1:
        add()

    elif ch==2:
        rem()

    elif ch==3:
        pres()

    elif ch==4:
        length()

    elif ch==5:
        union()

    elif ch==6:
        inter()

    elif ch==7:
        diff()

    elif ch==8:
        subset()

    elif ch==9:
        run=False

    else :
        print("Invalid Choice")
