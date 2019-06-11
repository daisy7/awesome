import sys
import base64
def ToBase64(file, txt):
    with open(file, 'rb') as fileObj:
        image_data = fileObj.read()
        base64_data = base64.b64encode(image_data)
        fout = open(txt, 'w')
        fout.write(base64_data.decode())
        fout.close()


def ToFile(txt, file):
    with open(txt, 'r') as fileObj:
        base64_data = fileObj.read()
        ori_image_data = base64.b64decode(base64_data)
        fout = open(file, 'wb')
        fout.write(ori_image_data)
        fout.close()

lens=len(sys.argv)
if lens==2:
    input=sys.argv[1]
    output=input+'2base64.txt'
    ToBase64(input,output)  # base64编码转换为二进制文件
    print("convert %s > %s success "%(input,output))
elif lens==3:
    input=sys.argv[1]
    output=sys.argv[2]
    ToFile(input,output)  # 文件转换为base64
    print("convert %s > %s success "%(output,input))
else:
    print("params length(%s) error"%(lens-1))
