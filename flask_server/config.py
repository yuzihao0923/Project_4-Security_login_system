DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'Project_4'
PASSWORD = 'Yuzihao09231835'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'project_4'

#mysql 不会认识utf-8,而需要直接写成utf8
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
