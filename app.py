from flask import Flask, Blueprint

import views


def create_dashboard_blueprint() -> Blueprint:
    dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")
    dashboard_bp.add_url_rule("/contests/<contest_id>", view_func=views.contest_details_view)
    return dashboard_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(create_dashboard_blueprint())

    @app.route("/")
    def index_view():
        return "OK"

    from commands.server import cron_cli
    app.cli.add_command(cron_cli)

    return app
