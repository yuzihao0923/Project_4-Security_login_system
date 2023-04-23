import cv2

# 读取两张图片
username='first'
img1 = cv2.imread('E:/Project_4/picture/{0}/{1}.jpg'.format(username, username))
#img1 = cv2.imread('E:/Project_4/picture/photo2.jpg')
img2 = cv2.imread('E:/Project_4/picture/photo.jpg')

# 将图片转换为灰度图像
gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 计算灰度图像的直方图
hist1 = cv2.calcHist([gray_img1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([gray_img2], [0], None, [256], [0, 256])

# 计算两张图片的相似度
similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

# 将相似度指标转换为百分比形式
similarity_percent = similarity * 100

# 打印相似度百分比
print("similarity:{:.2f}%".format(similarity_percent))

# print("hello world")