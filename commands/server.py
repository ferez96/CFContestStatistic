import click
import pandas as pd
from flask import Flask, Blueprint, render_template

import crawling

cmd = click.Group("server", help="HTTP Server")


@cmd.command()
def start():
    """command to start http web server"""
    app = Flask(__name__, template_folder="../templates")

    @app.route("/")
    def index_view():
        return "OK"

    dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

    @dashboard_bp.route("/contests/<contest_id>")
    def contest_details_view(contest_id):
        data = crawling.CodeForcesHTTPClient().send_request("contest.standings",
                                                            dict(contestId=contest_id))

        d = [
            {
                "Members": ",".join([x["handle"] for x in u["party"]["members"]]),
                "Penalty": u["penalty"],
                "Points": u["points"],
            } for u in data["rows"]
        ]
        df = pd.DataFrame(d)

        return render_template("contest_details.html", standings=df.style.render())

    app.register_blueprint(dashboard_bp)
    app.run()
