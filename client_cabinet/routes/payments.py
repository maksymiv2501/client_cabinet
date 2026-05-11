from flask import Blueprint, render_template, session, redirect, url_for

from client_cabinet.services.user_service import get_payments_data

payments_bp = Blueprint("payments", __name__)


@payments_bp.route("/payments")
def payments():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    data = get_payments_data()

    return render_template(
        "payments.html",
        data=data,
    )