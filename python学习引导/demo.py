from PIL import Image
import sys

def pi_to_char(pi):
    chars = [' ',',','1','n','*','#','@','M']
    for k in range(0,8):
        if pi < (k+1)*32:
            return chars[7-k]
            break

def write_file(file_name,data):
    f = open(file_name + '.txt','w')
    for d in data:
        print(d,file = f)
    f.close()

def chars_image(num):
    image_name = sys.argv[num]
    img = Image.open(image_name)
    img = img.convert('L')
    w,h = img.size
    if w>100:
        h = int((100/w)*h/2)
        w = 100
    img = img.resize((w,h))
    chars = [' ',',','1','n','*','#','@','M']
    data = []
    for i in range(0,h):
        line = ""
        for j in range(0,w):
            pi = img.getpixel((j,i))
            line += pi_to_char(pi)
        data.append(line)
    write_file(image_name,data)
    img.close
    print(image_name + '完成')

if __name__ == "__main__":
    i = 0
    for arg in sys.argv:
        i += 1 
    if i < 2:
        print('请输入参数')
        exit()
    while i > 1:
        i -= 1
        chars_image(i)
