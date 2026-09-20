from data_base import db


class Users:

    def __init__(self):
        pass

    def get_all(self):
        return db.Data

    def get_user_by_name(self, name):
        for user in db.Data:
            if user["User"] == name:
                return user

        return {"message": "Not Found!"}