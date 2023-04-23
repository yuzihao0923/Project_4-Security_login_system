import six
from PIL import Image
Path = 'F:\picture5.jpg'
# 将图片转成bytes字节型
with open(Path, 'rb') as f:
    imageBin = f.read()
# 很多时候，数据读写不一定是文件，也可以在内存中读写。
# BytesIO实现了在内存中读写bytes，创建一个BytesIO，然后写入一些bytes：
buf = six.BytesIO()
buf.write(imageBin)
buf.seek(0)
# 利用PIL打开图片文件
img = Image.open(buf)
print(type(imageBin))  # 查看imagBin的类型
print(imageBin)  # 查看imageBin的内容
img.show()  # 打开图片