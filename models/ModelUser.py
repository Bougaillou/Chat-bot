from .entities.User import User

class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor=db.connection.cursor()
            cursor.execute("USE flask_login;")
            sql="SELECT id, username, password, fullname FROM flask_login WHERE username='{}';".format(user.username)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                user=User(row[0], row[1], User.check_password(row[2],user.password), row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor=db.connection.cursor()
            cursor.execute("USE flask_login;")
            sql="SELECT id, username, fullname FROM flask_login WHERE id={};".format(id)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                return User(row[0], row[1], None, row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def sign(self, db, user):
        try:
            cursor=db.connection.cursor()
            cursor.execute("USE flask_login;")
            username=user.username
            fullname=user.fullname
            password=User.create_password(user.password)
            sql="INSERT INTO `flask_login` (`id`, `username`, `password`, `fullname`) VALUES (NULL, '{}', '{}', '{}');".format(username,password,fullname)   
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def check_exist(self, db, user):
        try:
            cursor=db.connection.cursor()
            cursor.execute("USE flask_login;")
            sql="SELECT id, username, password, fullname FROM flask_login WHERE username='{}';".format(user.username)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                return False
            else:
                return True
        except Exception as ex:
            raise Exception(ex)