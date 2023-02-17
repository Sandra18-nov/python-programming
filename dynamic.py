#profile={}
# profile["username"] = "user123"
# profile["age"] = "20"
# profile["email"] = "user123@gmail"
# print(profile)



profile={}
def register():
    username= input("enter username:")
    email=input("enter email:")
    password=input("enter password:")


    #store in a dictionary
    profile["username"] = "username"
    profile["email"] = "email"
    profile["password"] = "password"

    print(profile)

def get_profile():
    #print the user profile
    print(profile)

def change_username():
    new_name = input("Enter new username")
    profile["username"] = new_name

register()
get_profile()

change_username()
get_profile()






    
