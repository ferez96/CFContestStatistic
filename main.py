#!/usr/bin/env python3
"""
Chuong trinh thong ke ket qua thi Codeforces

Cau lac bo giai thuat truong Dai hoc Bach Khoa TPHCM
"""
__authors__ = ("Duong Thai Minh", "Nguyen Ho Minh Phuoc")
__version__ = '0.0.2'

import config  # this must be imported very first of the project
import click
import commands.server
import crawling


def init_cli():
    @click.group(help=__doc__)
    def cli():
        pass

    @cli.command()
    def ping():
        assert crawling.CodeForcesHTTPClient().ping(), "Ping"

    @cli.command("user-info")
    @click.argument("handle")
    def get_user_info(handle):
        user_info = crawling.CodeForcesHTTPClient().send_request("user.info", dict(handles=handle))
        print(user_info)

    # add commands
    cli.add_command(commands.server.cmd)

    return cli


def main():
    cli = init_cli()
    cli()


if __name__ == "__main__":
    main()

_ = config  # to keep import config
