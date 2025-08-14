import Users
import notepad
import Winter_Update
openq = 0
def main():
    print('Winter Python团队保留原有权利')
    print("版本号:1.2.0 zh-en")
    how = input("Winter\System＞")
    if "net user" in how :
        if Users.user() in how:
            openq = how[23:]
            print('OK')
            with open('password',"w",encoding = "utf-8") as on_password:
                on_password.write(openq)
    elif how == "dir":
        print(dir(oobe))
        print(dir())
    elif how == "notepad":
        notepad.main()
    elif how == "Winter_Update":
        has_update = Winter_Update.jiancha_update()
        if has_update == None:
            print('不可更新')
        else:
            updaten = input("是否要更新,break is say 'no,tkanks'")
            
    elif how == "break":
        try:
            while True:                
                break
        except SyntaxError:
            print("Can't break")
    else:
      print(f"'{how}'不是内部指令，也不是可执行的文件或批处理文件")  

