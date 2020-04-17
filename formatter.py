import os
import sys
from utils import translate_and_compose

def check(file_path):
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
                if i != len(lines)-1:
                    output.append("\n")
    else:
        for i in range(len(lines)):
            output.append(lines[i])
            if i != len(lines)-1:
                output.append("\n")
    
    f = open(file_path, "w")
    f.writelines(output)
    f.close()


def translate(pathname, filename):
    translate_and_compose(os.path.join(pathname,filename), os.path.join(pathname,"ja_" + filename), 'en', 'ja')


def file_check(path):
    for pathname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.srt'):
                print("Checking : ", pathname, filename)
                check(os.path.join(pathname,filename))
    
    for pathname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.srt'):
                print("Translating : ", pathname, filename)
                translate(pathname, filename)

    print("finished")


def main():
    # Use like [python formatter.py "file_path"]
    ROOT_PATH = str(sys.argv[1])
    file_check(ROOT_PATH)


if __name__ == "__main__":
    main()