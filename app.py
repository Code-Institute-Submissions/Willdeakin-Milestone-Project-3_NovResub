import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("recipes", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "recipes", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")



@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        is_veggie = "on" if request.form.get("is_veggie") else "off"
        is_vegan = "on" if request.form.get("is_vegan") else "off"
        recipe = {
            "recipe_name": request.form.get("recipe_name").lower(),
            "cooking_method": request.form.get("cooking_method"),
            "cooking_tool": request.form.get("cooking_tool"),
            "TTC": request.form.get("TTC").lower(),
            "website_link": request.form.get("website_link").lower(),
            "country_name": request.form.get("country_name"),
            "created_by": session["user"]
        }
        mongo.db.recipe.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("recipes"))

    methods = mongo.db.methods.find()
    tools = mongo.db.tools.find()
    countries = mongo.db.countries.find()
    return render_template("add.html", methods=methods, tools=tools, 
    countries=countries)



@app.route("/recipes")
def recipes():
    recipes = list(mongo.db.recipe.find())
    return render_template("recipes.html", recipes=recipes)



@app.route("/edit/<recipe_id>", methods=["GET", "POST"])
def edit(recipe_id):
    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    methods = mongo.db.methods.find()
    tools = mongo.db.tools.find()
    countries = mongo.db.countries.find()
    return render_template("edit.html", methods=methods, tools=tools, countries=countries, recipe=recipe)

@app.route("/delete/<recipe_id>")
def delete(recipe_id):
    mongo.db.recipe.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("recipes"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)