from flask import Blueprint, render_template, session, redirect, url_for

from client_cabinet.services.user_service import get_documents_data

documents_bp = Blueprint(
    "documents",
    __name__
)


@documents_bp.route("/documents")
def documents():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    data = get_documents_data()

    return render_template(
        "documents.html",
        data=data
    )