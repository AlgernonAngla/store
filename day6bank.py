import random ,sys

print("====================================")
print("|-------中国工商银行账户管理系统-------|")
print("|-------1、开户              -------|")
print("|-------2、存钱              -------|")
print("|-------3、取钱              -------|")
print("|-------4、转账              -------|")
print("|-------5、查询              -------|")
print("|-------6、退出              -------|")
print("====================================")


brankUser = {'中国工商银行':[{"账户":"2222","姓名":"昕泽","密码":"2222","存款余额为":666},{"账户":"3333","姓名":"Algernon","密码":"3333","存款":520}]}
userlist = {'2222':[{'国家':'中国','省份':'河北','城市':'唐山','街道':'中山路','门牌号':'010'}],'3333':[{'国家':'中国','省份':'河北','城市':'唐山','街道':'中山路','门牌号':'011'}]}
bank={}
def bank_adduser(account,username,password,country,province,street,door):
    if len(bank) > 100:
        # 超出了银行上限
        return 3
    if username in bank :
        #如果名字  在    bank  执行下面的代码
        return 2
    bank[username]={
        "account":"account",
        #键一个名字       ：值来自传入的参数:account
        "password":"password",
        "country":"country",
        "province":"province",
        "street":"street",
        "door":"door",
        "money":0,
        "brnk_name":bank_name # 直接调用全局参数
    }
    return 1

bank_name= "中国工商银行起码路支行"#写死的银行地址
def useradd():
    username=input("请输入您的用户名")
    password=input("请输入您的密码")
    print("请输入您的详细信息")
    country=input("请输入您国家")
    province = input("请输入您省份")
    street = input("请输入您街道")
    door=input("请输入您的门牌号")
    account=random.randint(10000000,99999999) #随机生成8位账号
    status=bank_adduser(account,username,password,country,province,street,door)
    if status == 3:
        print("对不起，改银行的用户已满，请到其他银行办理")
    if status == 2:
        print("对不起，改用户已经开户，不要重复")
    if status == 1:
        print("恭喜你正常开户，以下是您的信息")
        info ='''
          ------------个人信息------------
            用户名:%s
            账号：%s
            密码：*****
            国籍：%s
            省份：%s
            街道：%s
            门牌号：%s
            余额：%s
            开户行名称：%s
        '''
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))



#5.查询账户功能（传入值：账号，账号密码，返回值：空）
def selectUser():
    code = input('请输入账户:')
    pwd = input('请输入密码:')
    for i in range(0, len(brankUser['中国工商银行'])):
        if code == brankUser['中国工商银行'][i]['账户'] and pwd == brankUser['中国工商银行'][i]['密码']:
            print(brankUser['中国工商银行'][i])
            for j in range(0, len(userlist[code])):
                print(userlist[code][j])
                print("当前账户的开户行:中国工商银行起码路支行")
            return

  #退出
    else:
        print('该用户不存在！')

        def exit():
            print("感谢你的使用，下次再见")
            sys.exit()




# #存款
def bank_savemoney(account, smoney):
    if account in bank:
        bank[account]["money"] = bank[account]["money"] + smoney
        return 4
    else:
        return 5
def savemoney():
    print("......")
    account = int(input("请输入你的存款账号: "))
    smoney = int(input("请输入你的存款金额: "))
    status = bank_savemoney(account, smoney)
    if status == 4:
        print("++++++")
        print("存款成功，您的账户余额是：{}".format(bank[account]["money"]))
    if status == 5:
        print("False")





#转账
bank = {"username1": {"account_chu": "1", "password": "123456", "money": 100},
        "username2": {"account_ru": "2"}
        }
def user(account_chu, account_ru):
    if account_chu == bank["username1"]["account_chu"] and account_ru == bank["username2"]["account_ru"]:
        # if all([account_chu == bank["username1"]["account_chu"], account_ru == bank["username1"]["account_ru"]]):
        return 0
    else:
        return 1

def mm(password):
    if password == bank["username1"]["password"]:
        return 0
    else:
        return 2

def rmb(money_chu):
    if money_chu > bank["username1"]["money"]:  # 转出去的钱大于账户余额，返回值3
        return 3
    else:
        bank["username1"]["money"] = bank["username1"]["money"] - int(money_chu)
        return 0

def zhuanzhang():
    account_chu = input("请输入您的账号：")
    account_ru = input("请输入转入账号：")
    name = user(account_chu, account_ru)
    if name == 0:
        print("账号正确，请进行下一步")
        password = input("请输入密码：")
        name2 = mm(password)
        if name2 == 0:
            print("密码正确，进行下一步")
            money_chu = int(input("请输入转账金额："))
            name3 = rmb(money_chu)
            if name3 == 0:
                print("转账成功！账户余额", bank["username1"]["money"], "元")
            else:
                print("账户余额不足")
        else:
            print("密码错误，请重新输入")
    else:
        print("账号不存在")


#取钱
bank = {"name":{"account":"1","password":"123","money":10}}
def bank_adduser(account):
    if account in bank["name"]["account"]:
        return 0
    else:
        return 2

def useradd():
        account = input("请输入您得账号")
        start = bank_adduser(account)
        if start == 0:
            print("可以转账")
            password = input("请输入你的密码")
            if password == bank["name"]["password"]:
                print("密码输入正确")
                money = int(input("请输入交易金额"))
                if money <= bank["name"]["money"]:
                    bank["name"]["money"] -= money
                    print((bank["name"]["money"]))
                else:
                    return 3


while True:
    num=input("请输入您要办的业务：")
    if num  == "1":
        useradd()
    elif num == "2":
        savemoney()
    elif num == "3":
        useradd()
    elif num == "4":
        zhuanzhang()
    elif num == "5":
        selectUser()
    elif num == "6":
        exit()
    else:
        print("别瞎搞")
        break









