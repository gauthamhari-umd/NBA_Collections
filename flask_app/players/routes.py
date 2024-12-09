import base64,io
from io import BytesIO
from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user

from .. import player_client
from ..forms import  SearchForm,ChooseCollectionForm
from ..models import User, Review,Collection
from ..utils import current_time

players = Blueprint("players", __name__)



# """ ************ Helper for pictures uses username to get their profile picture************ """
# def get_b64_img(username):
#     user = User.objects(username=username).first()
#     bytes_im = io.BytesIO(user.profile_pic.read())
#     image = base64.b64encode(bytes_im.getvalue()).decode()
#     return image

# """ ************ View functions ************ """


@players.route("/", methods=["GET", "POST"])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for("players.query_results", query=form.search_query.data))

    return render_template("index.html", form=form)


@players.route("/search-results/<query>", methods=["GET"])
def query_results(query):
    try:
        results = player_client.search(query)
    except ValueError as e:
        return render_template("query.html", error_msg=str(e))
    
    return render_template("query.html", results=results)


@players.route("/players/<player_id>/<player_name>", methods=["GET","POST"])
def player_detail(player_id,player_name):
    try:
        result = player_client.retrieve_player_by_id(player_id,player_name)
        # result={"player_latest_season":"2024"}
        form=None
        if current_user.is_authenticated:
            form = ChooseCollectionForm()

            collections = Collection.objects(user=current_user._get_current_object())
            form.collection.choices = [(collection.collection_name, collection.collection_name) for collection in collections]
            if form.validate_on_submit():
                selected_choice = form.collection.data
                collection = Collection.objects.get(collection_name=selected_choice)
            
                if len(collection.list_of_players)<int(collection.size) and result not in collection.list_of_players:
                        collection.list_of_players.append(result)
                        collection.save()
                return redirect(url_for("players.index"))
        return render_template(
        "player_detail.html", player=result,form=form
    )
    except Exception as e:
        return render_template("404.html", error_msg=str(e))

        # selected_collection = form.collection.data
        # collections.update_one(
        #     {"name": selected_collection},
        #     {"$addToSet": result}  # Add player without duplication
        # )
        # return redirect(url_for("view_collection", collection_name=selected_collection))
  

   

   


@players.route("/user/<username>")
def user_detail(username):
    user= User.objects(username=username).first()
    reviews=Review.objects(commenter=user)
    for review in reviews:
        print(review.content)
    print(reviews)
    img = get_b64_img(user.username)
    if user:
        error=None
    else:
        error="ERROR"
    return render_template("user_detail.html", error=error, image=img, username=username,reviews=reviews)
    #uncomment to get review image
    #user = find first match in db
    #img = get_b64_img(user.username) use their username for helper function
  
