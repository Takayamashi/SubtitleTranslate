import os

def main():
    ROOT_PATH = "file_path"
    file_check(ROOT_PATH)

def check(file_path, filename):
    # 処理を記述
    f = open(file_path)
    data = f.read()  # ファイル終端まで全て読んだデータを返す
    f.close()
    lines = data.split('\n')
    output = []
    # print(lines[0])
    if lines[0] == "0" or lines[0] == "":
        for i in range(len(lines)):
            if (i - 4) % 5 != 0 and i != 0:
                output.append(lines[i])
                output.append("\n")
    else:
        for i in range(len(lines)):
            output.append(lines[i])
            output.append("\n")
    
    f = open(file_path, "w")
    f.writelines(output)
    f.close()



def file_check(path):
    for pathname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.srt'):
                print("Checking : ", pathname, filename)
                check(os.path.join(pathname,filename), filename)
    print("finished")


if __name__ == "__main__":
    main()