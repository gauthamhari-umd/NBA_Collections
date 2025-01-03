from flask_login import UserMixin
from datetime import datetime
from . import db, login_manager


# TODO: implement
@login_manager.user_loader
def load_user(user_id):
    return User.objects(username=user_id).first()

# TODO: implement fields
class User(db.Document, UserMixin):
    email = db.EmailField(unique=True, required=True,min_length=1,max_length=40)
    username = db.StringField(unique=True, required=True)
    password = db.StringField()
    profile_pic=db.ImageField()
    def get_id(self):
        return self.username


# TODO: implement fields
class Review(db.Document):
    commenter = db.ReferenceField('User')
    content = db.StringField(required=True,min_length=1,max_length=500)
    date = db.StringField(required=True)
    imdb_id = db.StringField(required=True,min_length=9,max_length=9)
    player_title = db.StringField(required=True,min_length=1,max_length=100)
    #image = db.StringField()
    #Uncomment when other fields are ready for review pictures

class Collection(db.Document):
    user=db.ReferenceField('User',required=True)
    collection_name = db.StringField(required=True,min_length=1,max_length=500)
    list_of_players=db.ListField()
    size=db.StringField(required=True)
