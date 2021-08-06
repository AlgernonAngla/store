



#三层词典
dict={"01":{"01","去2号地铁线"},"02":{"02","流行花园小区"},"03":{"03","门牌号是8888"}}
name1=input("去几号地铁线:")
if name1=="01":
        print(dict["01"])
        name2=input("请问去哪个小区")
if name2=="02":
      print(dict["02"])
      name3 = input("请问是哪个门牌号")
if name3 == "03":
    print(dict["03"])





#输入数字打印乘法表
j=int(input("请输入一个数字:"))
for i in range(1,j+1):
       for j in range(1,i+1):
           print(j,"*",i,"=",i*j, end=" ")
           print()