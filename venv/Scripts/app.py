from users import User

my_user = User("Pamela_carloss01@yahoo.com","sPamela","one", None)

#print(my_user)

my_user.save_to_db()

my_user = User.load_from_db_by_email("Pamela_carlos01@yahoo.com")

my_user.save_to_db()

print(my_user)