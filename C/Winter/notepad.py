def main():
    print("======请输入记的内容=====")
    note = input()
    print("请输入你的文件路径(分隔符用\)")
    file_path = input()
    with open(file_path,"w",encoding = "utf-8") as file:
        file.write(note)
