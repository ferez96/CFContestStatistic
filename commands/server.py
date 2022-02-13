import click
from flask.cli import AppGroup
import app

cmd = click.Group("server", help="HTTP Server")
cron_cli = AppGroup("cron", help="Cronjob")


@cmd.command()
def start():
    """command to start http web server"""
    app.create_app().run()


@cron_cli.command("update")
def cronjob_update():
    print("Done!")
