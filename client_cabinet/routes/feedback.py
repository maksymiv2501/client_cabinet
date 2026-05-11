from flask import Blueprint, render_template, session, redirect, url_for

from client_cabinet.services.feedback_service import get_feedback_data

feedback_bp = Blueprint("feedback", __name__)


@feedback_bp.route("/feedback")
def feedback():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    data = get_feedback_data()

    return render_template(
        "feedback.html",
        data=data,
    )