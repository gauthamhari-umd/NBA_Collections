import base64,io
from io import BytesIO
from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user

from .. import player_client
from ..forms import  SearchForm,CreateCollectionForm,ChooseCollectionForm
from ..models import User, Review,Collection
from ..utils import current_time


collections = Blueprint("collections", __name__)



# """ ************ Helper for pictures uses username to get their profile picture************ """
# def get_b64_img(username):
#     user = User.objects(username=username).first()
#     bytes_im = io.BytesIO(user.profile_pic.read())
#     image = base64.b64encode(bytes_im.getvalue()).decode()
#     return image

# """ ************ View functions ************ """



@collections.route("/view-collections/", methods=["GET", "POST"])
def index():

    collections=Collection.objects(user=current_user._get_current_object())
    return render_template("collections.html",collections=collections)

@collections.route("/view-collections/<collection_name>", methods=["GET", "POST"])
def collection_view(collection_name):
   current_collection=Collection.objects(user=current_user._get_current_object(),collection_name=collection_name).first()
   results=current_collection.list_of_players
   return render_template("collection_view.html",results=results)


@collections.route("/create-collection/", methods=["GET", "POST"])
def create_collection():
    form=CreateCollectionForm()
    if form.validate_on_submit():
        collection_name = form.name.data
        collection_size=str(form.size.data)

        new_collection = Collection(
            collection_name=collection_name,
            user=current_user,  
            size=collection_size 
        )
        
        new_collection.save()
        return redirect(url_for('players.index'))
    return render_template("create_collection.html",form=form)
 
@collections.route("/delete-collection/", methods=["GET", "POST"])
def delete_collection():
    form=ChooseCollectionForm()
    collections = Collection.objects(user=current_user._get_current_object())
    form.collection.choices = [(collection.collection_name, collection.collection_name) for collection in collections]
    if form.validate_on_submit():
        collection_name = form.collection.data
        selected_collection=Collection.objects(user=current_user._get_current_object(),collection_name=collection_name).first()
        selected_collection.delete()
        return redirect(url_for('collections.index'))
    return render_template("delete-collection.html",form=form)
