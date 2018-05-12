## Install

### 简介

API主要使用：

- [Flask](http://flask.pocoo.org/)
- [Flask-Security](https://flask-security.readthedocs.io/en/latest/)
- [Flask-MongoEngine](http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/)
- [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
- [Flask-Restful](https://flask-restful.readthedocs.io/en/latest/)
- [Arrow](http://arrow.readthedocs.io/en/latest/)

### 本地测试环境搭建

```
搭建python环境, 以及安装mongodb
```

#### 配置开发测试环境配置文件

```
export FLASK_ENV=DEVELOPMENT # 指定使用development的配置
cp api/config/development.py_sample api/config/development.py
(编辑api/config/development.py 更改mongo的配置, 任意配置SECRET_KEY和SECURITY_PASSWORD_SALT)
```