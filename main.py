# 1
number = int(input("yosh kiriting: "))
if number  <= 0 :
    print("bu yosh yo'q")
elif number  < 18:
    print("voyaga yetmagan")

elif number <=  110 :
    print("voyaga yetgan")
else:
    print("bunday  yosh yoq")


# 2
tez = int(input("tezlik kirit: " ))

if tez  <= 0 :
    print("bunday tezlik yoq")
elif tez <= 70:
        print("jarima yo'q")
elif tez <= 100 :
    print("2x million jarima")
elif tez <= 200:
    print("5x million jarima")
else:
    print("yoq")




# 3
yosh = int(input("yosh kirit: "))

if yosh <= 0:
    print("bunday yosh yo'q")
elif yosh < 7:
    print("bog'cha o'quvchisi")
elif yosh < 18:
    print("m")
elif yosh < 110:
    print("nafaqa")
else:
    print("bunday yosh yo'q")
