import click
import app

cmd = click.Group("server", help="HTTP Server")


@cmd.command()
def start():
    """command to start http web server"""
    app.create_app().run()
