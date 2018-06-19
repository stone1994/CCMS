# 配置文件
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
# session必须要设置key
SECRET_KEY = 'Q29sbGVnZUN1cnJpY3VsdW1NYW5hZ2VtZW50U3lzdGVt'

# mysql数据库连接信息,这里改为自己的账号
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1111@localhost:3306/ccms?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS = True

