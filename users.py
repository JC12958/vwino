
from database import ConnectionFromPool

class User:
    def __init__(self, email, FirstName, LastName, id):
        self.email = email
        self.FirstName = FirstName
        self.LastName = LastName
        self.id = id

    def __repr__(self):
        return "User: {} Email: {}".format(self.FirstName,self.email)

    def save_to_db(self):
        with ConnectionFromPool() as conn:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO users (email,FirstName,LastName) VALUES (%s, %s, %s)",
                            (self.email,self.FirstName,self.LastName))



    @classmethod
    def load_from_db_by_email(cls, VarEmail):
        with ConnectionFromPool() as conn:
            with conn.cursor() as cursor:
                cursor.execute("Select * from users WHERE email =%s", (VarEmail,))

                user_data = cursor.fetchone()
                #for user_data in cursor.fetchone():
                return cls(email=user_data[1], FirstName=user_data[2], LastName=user_data[3], id=user_data[0],)



