from flask import Blueprint, render_template, redirect, url_for

from services.forecast_service import (
    get_current_correction_data,
    get_next_month_plan_data,
    get_next_year_plan_data,
)

forecast_bp = Blueprint("forecast", __name__)


@forecast_bp.route("/forecast")
def forecast():
    return redirect(url_for("forecast.current_correction"))


@forecast_bp.route("/forecast/current-correction")
def current_correction():
    return render_template(
        "forecast/current_correction.html",
        data=get_current_correction_data(),
    )


@forecast_bp.route("/forecast/next-month")
def next_month():
    return render_template(
        "forecast/next_month.html",
        data=get_next_month_plan_data(),
    )


@forecast_bp.route("/forecast/next-year")
def next_year():
    return render_template(
        "forecast/next_year.html",
        data=get_next_year_plan_data(),
    )