mysql_host = "127.0.0.1"  # 表示本地的地址
mysql_port = 3306    # 端口号
mysql_user = "root"   # mysql用户名
mysql_ps = "123456"  # mysql密码
mysql_database = "zhichong"  # mysql中创建的数据库名称


class Config():
    """工程配置信息"""
    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}".format(mysql_user, mysql_ps, mysql_host, mysql_port,
                                                                      mysql_database)
    SQLALCHEMY_TRACK_MODIFICATIONS = False