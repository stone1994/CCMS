from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

# 加载配置文件
app.config.from_object('ccms.setting')

# 配置flask配置对象中键：SQLALCHEMY_DATABASE_URI

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://username:password@hostname/database"

# 配置flask配置对象中键：SQLALCHEMY_COMMIT_TEARDOWN,设置为True,应用会自动在每次请求结束后提交数据库中变动

# app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# 创建数据库对象
db = SQLAlchemy(app)

from ccms.model import Teacher