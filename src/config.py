class DevelopmentConfig():
    DEBUG= True
    MYSQL_HOST='us-cdbr-east-04.cleardb.com'
    MYSQL_USER='b928d8a6c28e81'
    MYSQL_PASSWORD='0d14d704'
    MYSQL_DB='heroku_5ac5dbad874fd18'

config= {
    'development': DevelopmentConfig
}
#mysql://b928d8a6c28e81:0d14d704@us-cdbr-east-04.cleardb.com/heroku_5ac5dbad874fd18?reconnect=true