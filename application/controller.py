from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask import Blueprint
from application.model import User

root = Blueprint("root", __name__, template_folder="templates/root")

@root.route("/",methods=["GET","POST"])
def dashboard():
    if request.method == "GET":
        if "user_info" not in session:
            return render_template("login.html")
        
