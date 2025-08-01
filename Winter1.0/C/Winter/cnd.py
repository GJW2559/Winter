import Users
import notepad
openq = 0
def main():
    print('Winter Python团队保留原有权利')
    print("版本号:1.1.0 zh-en")
    how = input("Winter\System＞")
    if "net user" in how :
        if Users.cnd_how_user() in how:
            openq = how[23:]
            print('OK')
            return openq
    elif how == "dir":
        print(dir(notepad))
        print(dir(Users))
        print(dir())
    elif how == "notepad":
        notepad.main()
    elif how == "break":
        try:
            while True:                
                break
        except SyntaxError:
            print("Can't break")
    else:
        return "no"

