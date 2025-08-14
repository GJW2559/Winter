import cnd
import Users
import oobe
import time
what_class = "0"
def main():
    try:
        open_k = "0"
        password = "None"
        with open(r"C:\Users\Lenovo\Downloads\C\Winter\user.txt")as usertxtnoterr:
            usergoode = usertxtnoterr.read()
        if usergoode == "hasoobe":
            with open(r"C:\Users\Lenovo\Downloads\C\Winter\password.txt","r",encoding="utf-8") as file2:
                password = file2.read()
            Users.init()
            with open(r"C:\Users\Lenovo\Downloads\C\Winter\username.txt","r",encoding="utf-8") as userna:
                open_k = userna.read()
        else:
            print("you are no oobe")
            what_class = Users.hard(open_k,password)
    except FileNotFoundError as err:
        print("程序",err)
    def what_class_this():
        return what_class
    try:
        if what_class != None:
            print(f"你的用户是{what_class}")
            while True:
                cnd.main()
        else:
            print("你没有用户，请尝试用访客用户登录")
                
    except Exception as errors:
        print("运行失败，程序错误,请联系开发者远程修复(90%的错误可以重启)",errors)
if __name__ == "__main__":
    with open(r'C:\Users\Lenovo\Downloads\C\Winter\user.txt', 'r', encoding='utf-8') as f:
        read = f.read()
    if read == "no":
        oobe.Setup_exe()
        oobe.Setup_say()
        oobe.Setup_interet()
        oobe.Setup_users()
        with open('user.txt','w',encoding = 'utf-8') as files:
            files.write('hasoobe')
        print("Hi，安然无恙啊")
        time.sleep(1)
        print("这可能要等几分钟")
        time.sleep(1)
        print("请勿切断电源")
        time.sleep(1)
        main()
    else:
        main()