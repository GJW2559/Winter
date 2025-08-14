from tqdm import tqdm  
import time  
import os  
  
# 创建文件保存目录  
if not os.path.exists('winter_system'):  
    os.makedirs('winter_system')  
  
# 定义各个模块的代码  
notepad = [  
    "def main():",  
    '    print("======请输入记的内容=====")',  
    "    note = input()",  
    '    print("请输入你的文件路径(分隔符用\\)")',  
    "    file_path = input()",  
    '    with open(file_path,"w",encoding = "utf-8") as file:',  
    "        file.write(note)"  
]  
  
Imports = [  
    "def give_imports():",  
    "    ",  
    "    try:",  
    "        import cnd",  
    "        import notepad",  
    "        import oobe",  
    "        import Users",  
    "        import C",  
    "    except ImportError:",  
    "        try:",  
    "            import cnd",  
    "        except:",  
    "            return \"cnd\"",  
    "        try:",  
    "            import notepad",  
    "        except:",  
    "            return \"notepad\"",  
    "        try:",  
    "            import oobe",  
    "        except:",  
    "            return \"oobe\"",  
    "        try:",  
    "            import oobe",  
    "        except:",  
    "            import Users",  
    "        try:",  
    "            import C",  
    "        except:",  
    "            return \"Users\"",  
    "    else:",  
    "        return \"OK\""  
]  
  
user_txt = [  
    "no"  
]  
  
Winter_Update = [  
    "import oobe",  
    "from oobe import time",  
    "v_num = [1.0,2.0,3.1,4.2,4.7,5.0,6.1,6.7,9.0]",  
    "update = [\"插件包\",'(系统升级)系统更新包','Setup','记事本功能更新']",  
    "up_ths = [\"用于修补bug,修补远程代码等等\",'接收到最新系统','提供多种设置','记事本文件读写更好']",  
    "def jiancha_update():",  
    '    print("正在检查更新File....")',  
    "    print('正在连接Interest')",  
    "    time.sleep(1)",  
    "    print('正在连接更新中心')",  
    "    time.sleep(1)",  
    "    print('正在加载更新项目和用途，首次运行需要很多时间，请耐心等待')",  
    "    time.sleep(1)",  
    "    if update == []:",  
    '        print("没有更新")',  
    "        return None",  
    "    else:",  
    "        print(\"检测到\",len(update),'个更新',',分别是:')",  
    "    up_len = len(update)",  
    "    for i in range(up_len):",  
    "        print('更新项目:',update[i],'适用于',up_ths[i])",  
    "def progress_bar(current, total, bar_length=50):",  
    "    fraction = current / total",  
    "    arrow = int(fraction * bar_length) * \"ᐅ\"",  
    "    padding = (bar_length - len(arrow)) * \" \"",  
    "    percent = int(fraction * 100)",  
    "    print(f\"\\r进度: [{arrow}{padding}] {percent}%\", end=\"\", flush=True)",  
    "def genxin():",  
    '    print("正在更新......")',  
    "    for i in range(101):",  
    "        progress_bar(i, 100)",  
    "        time.sleep(0.05)  # 模拟耗时操作",  
    '    print("\\n完成！")',  
    "    update.clear()",  
    "    update = []",  
    "    up_ths.clear()",  
    "    up_ths = []"  
]  
  
Lock = [  
    "import hashlib",  
    "import base64",  
    "",  
    "def ruterr(data: str) -> str:",  
    "    # 1. 计算SHA-256哈希（二进制）",  
    "    sha256 = hashlib.sha256(data.encode()).digest()",  
    "    # 2. 用Base85编码哈希值",  
    "    return base64.b85encode(sha256).decode()",  
    "def hashas(data: str, salt: str, iterations=1000) -> str:",  
    "    combined = (data + salt).encode()",  
    "    for _ in range(iterations):",  
    "        combined = hashlib.sha256(combined).digest()",  
    "    return base64.b85encode(combined).decode()"  
]  
  
__init__ = [  
    "from notepad import main",  
    "from Users import hard",  
    "from Users import init",  
    "from Users import user",  
    "from Main import main",  
    "from cnd import main",  
    "from oobe import Setup_exe",  
    "from oobe import Setup_interet",  
    "from oobe import Setup_say",  
    "from oobe import Setup_users",  
    "from Winter_Update import jiancha_update",  
    "from Lock import hashas",  
    "from Lock import ruterr",  
    "#共11个函数，7个文件(不包含__init__.py)",  
    "v_num = [2.0]",  
    "update = {",  
    "    \"插件包\":\"自带修复和缓存\",",  
    "    \"设置\":\"提供各种设置\"",  
    "}"  
]  
  
Users = [  
    "def init():",  
    "    input_name = 0",  
    "    input_password = 0",  
    "def hard(username1,password1):",  
    "    input_name = input(\"用户:\")",  
    "    input_password = input(\"密码:\")",  
    "    if input_name == username1 and input_password == password1:",  
    "        print(f\"Hi,Administrator {username1}\")",  
    "        return \"Administrator\"",  
    "    else:",  
    "        return None",  
    "def user():",  
    "    #with open('')",  
    "    with open('username.txt',\"r\",encoding=\"utf-8\") as user:",  
    "        return user.read()"  
]  
  
oobe = [  
    "import random",  
    "import Imports",  
    "import time",  
    "my_gg_id = \"osta1266\"",  
    "try:",  
    "    def jindutiao(ints,sleep):",  
    "        for i in range(ints):",  
    "            time.sleep(sleep)",  
    "            print(\"[\",\"#\"*i,\"]\")",  
    "    def Setup_exe():",  
    "        print(\"正在打开setup.exe\")",  
    "    def Setup_say():  ",  
    "        # 语言/键盘布局选择  ",  
    "        print(\"正在加载地区语言\")",  
    "        time.sleep(0.5)",  
    "        print(\"China,Chinese\")",  
    "    def give_text():  ",  
    "        # 类似微软EULA阅读  ",  
    "        time.sleep(0.5)",  
    "        print(\"EULA:请您阅读welcome.winter.zoz.la/index.html/eula.txt\")",  
    "        time.sleep(0.5)",  
    "    def Setup_interet():",  
    "        print(\"正在连接专用ChinaNet……\")",  
    "        time.sleep(1)",  
    "        for i in range(100):",  
    "            print(\"Say:C/oobe/Setup_interet().mas ChinaNet_Codemao\",\",\",str(random.randint(100,200)))",  
    "    def Setup_users():  ",  
    "        # 本地账户创建逻辑  ",  
    "        username = input(\"谁会使用这台电脑？\") ",  
    "        password = input(\"让使用电脑的人设置密码\")",  
    "        jindutiao(20,0.5)",  
    "        with open(r\"./password.txt\",\"w\",encoding = \"utf-8\")as go_file:",  
    "            go_file.write(password)",  
    "        with open(r\"./username.txt\",\"w\",encoding=\"utf-8\")as files:",  
    "            files.write(username)",  
    "        # 诊 ",  
    "        importren = Imports.give_imports()",  
    "        if importren != \"OK\":",  
    "            print(\"PyError:No_find OS Need tkings C/Winter\",importren)",  
    "        print(\"你的广告ID:\",\"ggdd18181\"+username)",  
    "except:",  
    "    print(\"程序中断或程序错误,联系开发者\")"  
]  
  
Main = [  
    "import cnd  ",  
    "import Users  ",  
    "import oobe  ",  
    "import time  ",  
    "  ",  
    "# 常量定义  ",  
    "USER_FILE = r\"user.txt\"  ",  
    "PASSWORD_FILE = r\"password.txt\"  ",  
    "USERNAME_FILE = r\"username.txt\"  ",  
    "  ",  
    "def load_user_data():  ",  
    "    \"\"\"加载用户数据\"\"\"  ",  
    "    with open(USER_FILE,\'a+') as f:  ",  
    "        return f.read().strip()  ",  
    "  ",  
    "def setup_new_user():  ",  
    "    \"\"\"设置新用户\"\"\"  ",  
    "    oobe.Setup_exe()  ",  
    "    oobe.Setup_say()  ",  
    "    oobe.Setup_interet()  ",  
    "    oobe.Setup_users()  ",  
    "      ",  
    "    with open(USER_FILE, 'w', encoding='utf-8') as f:  ",  
    "        f.write('hasoobe')  ",  
    "      ",  
    "    # 显示设置进度信息  ",  
    "    messages = [  ",  
    "        \"Hi，安然无恙啊\",  ",  
    "        \"这可能要等几分钟\",  ",  
    "        \"请勿切断电源\"  ",  
    "    ]  ",  
    "    for msg in messages:  ",  
    "        print(msg)  ",  
    "        time.sleep(1)  ",  
    "  ",  
    "def main():  ",  
    "    try:  ",  
    "        user_status = load_user_data()  ",  
    "          ",  
    "        if user_status == \"hasoobe\":  ",  
    "            with open(PASSWORD_FILE, 'r', encoding='utf-8') as f:  ",  
    "                password = f.read()  ",  
    "              ",  
    "            Users.init()  ",  
    "              ",  
    "            with open(USERNAME_FILE, 'r', encoding='utf-8') as f:  ",  
    "                username = f.read()  ",  
    "                  ",  
    "            user_class = Users.hard(username, password)  ",  
    "              ",  
    "            if user_class:  ",  
    "                print(f\"你的用户是{user_class}\")  ",   
    "                while True:  ",  
    "                    cnd.main()  ",  
    "            else:  ",  
    "                print(\"你没有用户，请尝试用访客用户登录\")  ",  
    "        else:  ",  
    "            print(\"you are no oobe\")  ",  
    "              ",  
    "    except FileNotFoundError as err:  ",  
    "        print(\"程序错误:\", err)  ",  
    "    except Exception as err:  ",  
    "        print(\"运行失败，程序错误,请联系开发者远程修复(90%的错误可以重启)\", err)  ",  
    "  ",  
    "if __name__ == \"__main__\":  ",  
    "    if load_user_data() == \"no\":  ",  
    "        setup_new_user()  ",  
    "    main()"  
]  
  
cnd = [  
    "import Users",  
    "import notepad",  
    "import Winter_Update",  
    "openq = 0",  
    "def main():",  
    "    print('Winter Python团队保留原有权利')",  
    "    print(\"版本号:2.0.0 zh-en\")",  
    "    how = input(\"Winter\\System＞\")",  
    "    if \"net user\" in how :",  
    "        if Users.user() in how:",  
    "            openq = how[23:]",  
    "            print('OK')",  
    "            with open('password',\"w\",encoding = \"utf-8\") as on_password:",  
    "                on_password.write(openq)",  
    "    elif how == \"dir\":",  
    "        print(dir(oobe))",  
    "        print(dir())",  
    "    elif how == \"notepad\":",  
    "        notepad.main()",  
    "    elif how == \"Winter_Update\":",  
    "        has_update = Winter_Update.jiancha_update()",  
    "        if has_update == None:",  
    "            print('不可更新')",  
    "        else:",  
    "            updaten = input(\"是否要更新,break is say 'no,tkanks'\")",  
    "            ",  
    "    elif how == \"break\":",  
    "        try:",  
    "            while True:                ",  
    "                break",  
    "        except SyntaxError:",  
    "            print(\"Can't break\")",  
    "    else:",  
    "      print(f\"'{how}'不是内部指令，也不是可执行的文件或批处理文件\")"  
]  
  
menu = [__init__,  
        cnd,  
        Imports,  
        Main,  
        notepad,  
        oobe,  
        Users,  
        Winter_Update  
       ]  
menu_fileName = ['__init__.py',  
                 'cnd.py',  
                 'Imports.py',  
                 'Main.py',  
                 'notepad.py',  
                 'oobe.py',  
                 'Users.py',  
                 'Winter_update.py'  
                ]  
  
if __name__ == "__main__":  
    print("要安装winter系统配置最少要1GB储存和1GB运行内存,否则蓝屏死机")  
    a = input("确定要安装么(T/F): ")  
    if a == "T":  
        try:  
            print("好的，正在安装...")  
            for code_list, filename in zip(menu, menu_fileName):  
                file_path = os.path.join('winter_system', filename)  
                with open(file_path, 'w', encoding='utf-8') as f:  
                    for line in code_list:  
                        f.write(line + '\n')  
                print(f"已生成: {file_path}")  
              
            print("\n安装完成！所有文件已保存在 winter_system 文件夹中。")  
            print("你可以运行 `python winter_system/Main.py` 启动系统。")  
              
        except Exception as e:  
            print(f"安装失败: {e}")  
    elif a == "F":  
        print("安装取消。")  
    elif a == 'nn123525':  
        print("value:None\nv2.0")  
    else:  
        print("无效输入，安装取消。")  
