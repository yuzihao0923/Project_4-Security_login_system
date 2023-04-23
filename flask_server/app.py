from flask import Flask, request, jsonify
from flask_cors import CORS
# 引用数据库启动文件
from exts import db
# 引用数据库配置文件
import config
# 引用数据库
from user.index import *
import cv2


def compareImages(username, comparename):
    # 读取两张图片
    img1 = cv2.imread('E:/Project_4/picture/{0}/{1}.jpg'.format(username, username))
    img2 = cv2.imread('E:/second/{}.jpg'.format(username))
    # print(len(img2))
    # img2 = cv2.imread('E:/Project_4/picture/first.jpg')
    # img2 = cv2.imread('E:/Project_4/picture/2.name.jpg')

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
    print("similarity：{:.2f}%".format(similarity_percent))
    return similarity_percent


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
# //引用模型
app.register_blueprint(user, url_prefix="/user")


@app.route("/")
def query_example():
    name = request.args.get('user')
    img_path = request.args.get('path')

    prediction = compareImages(name, img_path)

    data = {'prediction': prediction}
    response = jsonify(data)
    return response

    # return jsonify(
    #     prediction=str(prediction)
    # )
    # return 'hello' + str(prediction)


if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)
CORS(app)