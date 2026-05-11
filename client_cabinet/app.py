from flask import Flask, redirect, url_for

from client_cabinet.config import Config
from client_cabinet.database.db import init_db
from client_cabinet.services.user_service import create_test_admin

from client_cabinet.routes.auth import auth_bp
from client_cabinet.routes.dashboard import dashboard_bp
from client_cabinet.routes.my_data import my_data_bp
from client_cabinet.routes.analytics import analytics_bp
from client_cabinet.routes.invoices import invoices_bp
from client_cabinet.routes.payments import payments_bp
from client_cabinet.routes.forecast import forecast_bp
from client_cabinet.routes.feedback import feedback_bp
from client_cabinet.routes.contacts import contacts_bp
from client_cabinet.routes.documents import documents_bp

app = Flask(__name__)
app.config.from_object(Config)
@app.route("/favicon.ico")
def favicon():
    return "", 204

app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(my_data_bp)
app.register_blueprint(analytics_bp)
app.register_blueprint(invoices_bp)
app.register_blueprint(payments_bp)
app.register_blueprint(forecast_bp)
app.register_blueprint(feedback_bp)
app.register_blueprint(contacts_bp)
app.register_blueprint(documents_bp)


@app.route("/")
def home():
    return redirect(url_for("auth.login"))


if __name__ == "__main__":
    init_db()
    create_test_admin()
    app.run(debug=True)