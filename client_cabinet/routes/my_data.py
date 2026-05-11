from flask import Blueprint, render_template, session, redirect, url_for

from client_cabinet.services.user_service import get_my_data

my_data_bp = Blueprint("my_data", __name__)


@my_data_bp.route("/my-data")
def my_data():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    data = get_my_data()

    return render_template(
        "my_data.html",
        data=data
    )