import random
import Imports
import time
my_gg_id = "osta1266"
try:
    def jindutiao(ints,sleep):
        for i in range(ints):
            time.sleep(sleep)
            print("[","#"*i,"]")
    def Setup_exe():
        print("正在打开setup.exe")
    def Setup_say():  
        # 语言/键盘布局选择  
        print("正在加载地区语言")
        time.sleep(0.5)
        print("China,Chinese")
    def give_text():  
        # 类似微软EULA阅读  
        time.sleep(0.5)
        print("EULA:请您阅读welcome.winter.zoz.la/index.html/eula.txt")
        time.sleep(0.5)
    def Setup_interet():
        print("正在连接专用ChinaNet……")
        time.sleep(1)
        for i in range(100):
            print("Say:C/oobe/Setup_interet().mas ChinaNet_Codemao",",",str(random.randint(100,200)))
    def Setup_users():  
        # 本地账户创建逻辑  
        username = input("谁会使用这台电脑？") 
        password = input("让使用电脑的人设置密码")
        jindutiao(20,0.5)
        with open(r"./password.txt","w",encoding = "utf-8")as go_file:
            go_file.write(password)
        with open(r"./username.txt","w",encoding="utf-8")as files:
            files.write(username)
        # 诊 
        importren = Imports.give_imports()
        if importren != "OK":
            print("PyError:No_find OS Need tkings C/Winter",importren)
        print("你的广告ID:","ggdd18181"+username)
except:
    print("程序中断或程序错误,联系开发者")
