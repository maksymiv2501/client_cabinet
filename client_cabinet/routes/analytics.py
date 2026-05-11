from flask import Blueprint, render_template, session, redirect, url_for

from client_cabinet.services.user_service import get_analytics_data

analytics_bp = Blueprint("analytics", __name__)


@analytics_bp.route("/analytics")
def analytics():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    data = get_analytics_data()

    return render_template(
        "analytics.html",
        data=data,
    )