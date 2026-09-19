#simple calculetor
a = int(input("Enter valev a : "))
b = int(input("Enter valeu b : "))
c =input("Enter what you want to do ex.+-÷× : ")
if  c =="+" :
    print(f" {a + b} ")
elif c == "-":
    print(f"{a-b}")
elif c =="÷":
    print(f"{a/b}")
elif c == "×":
    print(f"{a*b}")
else :
    print("invlid oprator")
