import oobe
from oobe import time
v_num = [1.0,2.0,3.1,4.2,4.7,5.0,6.1,6.7,9.0]
update = ["插件包",'(系统升级)系统更新包','Setup','记事本功能更新']
up_ths = ["用于修补bug,修补远程代码等等",'接收到最新系统','提供多种设置','记事本文件读写更好']
def jiancha_update():
    print("正在检查更新File....")
    print('正在连接Interest')
    time.sleep(1)
    print('正在连接更新中心')
    time.sleep(1)
    print('正在加载更新项目和用途，首次运行需要很多时间，请耐心等待')
    time.sleep(1)
    if update == []:
        print("没有更新")
        return None
    else:
        print("检测到",len(update),'个更新',',分别是:')
    up_len = len(update)
    for i in range(up_len):
        print('更新项目:',update[i],'适用于',up_ths[i])
def progress_bar(current, total, bar_length=50):
    fraction = current / total
    arrow = int(fraction * bar_length) * "ᐅ"
    padding = (bar_length - len(arrow)) * " "
    percent = int(fraction * 100)
    print(f"\r进度: [{arrow}{padding}] {percent}%", end="", flush=True)
def genxin():
    print("正在更新......")
    for i in range(101):
        progress_bar(i, 100)
        time.sleep(0.05)  # 模拟耗时操作
    print("\n完成！")
    update.clear()
    update = []
    up_ths.clear()
    up_ths = []
    