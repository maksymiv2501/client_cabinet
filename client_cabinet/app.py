from flask import Flask, render_template
from flask import Flask, redirect, url_for 

from config import Config
from database.db import init_db
from services.user_service import create_test_admin

from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.my_data import my_data_bp
from routes.analytics import analytics_bp
from routes.invoices import invoices_bp
from routes.payments import payments_bp
from routes.forecast import forecast_bp
from routes.feedback import feedback_bp
from routes.contacts import contacts_bp
from routes.documents import documents_bp

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