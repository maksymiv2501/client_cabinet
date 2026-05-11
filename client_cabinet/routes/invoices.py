from flask import Blueprint, render_template, session, redirect, url_for

from client_cabinet.services.user_service import get_invoices_data

invoices_bp = Blueprint("invoices", __name__)


@invoices_bp.route("/invoices")
def invoices():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    data = get_invoices_data()

    return render_template(
        "invoices.html",
        data=data,
    )