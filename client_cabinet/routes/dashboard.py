from flask import Blueprint, render_template, redirect, url_for, session

from client_cabinet.services.dashboard_service import get_dashboard_data

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    data = get_dashboard_data()

    return render_template(
        "dashboard.html",
        name=session["user_name"],
        data=data,
    )