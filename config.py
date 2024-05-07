class Config:
    SECRET_KEY='ibrahimbougaillou'

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD='root'
    MYSQL_PORT="3306"
    MYSQL_DB='flask_login'

config={
    'development': DevelopmentConfig
}