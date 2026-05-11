from flask import Blueprint, render_template, session, redirect, url_for

contacts_bp = Blueprint(
    "contacts",
    __name__
)


@contacts_bp.route("/contacts")
def contacts():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    return render_template("contacts.html")