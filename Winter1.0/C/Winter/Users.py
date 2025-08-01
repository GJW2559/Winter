def init():
    input_name = 0
    input_password = 0
def hard(username1,password1):
    input_name = input("用户:")
    input_password = input("密码:")
    if input_name == username1 and input_password == password1:
        print(f"Hi,Administrator {username1}")
        return "Administrator"
    else:
        return None