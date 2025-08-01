import cnd
import Users
import oobe
import os
def main():
    try:
        
        Users.init()
        EOFError = "gjw123456"
        what_class = Users.hard("gjw",EOFError)
    
    except KeyboardInterrupt:
        print("程序中断")
    def what_class_this():
        return what_class
    try:
        if what_class != None:
            print(f"你的用户是{what_class}")
        else:
            print("你没有用户，请尝试用访客用户登录")
            while True:
                break
        while True:
            cnd.main()
            cnd.jiance()
    
    except:
        print("运行失败，程序错误,请联系开发者远程修复(90%的错误可以重启)")
if __name__ == "__main__":
    with open(r'C:\Users\Public\TurtleWorkspace\Winter\user.txt', 'r', encoding='utf-8') as f:
        read = f.read()
    if read == "no":
        oobe.Setup_exe()
        oobe.Setup_say()
        oobe.Setup_interet()
        oobe.Setup_users()
        with open('user.txt','w',encoding = 'utf-8') as files:
            files.write('hasoobe')
        main()
    else:
        main()