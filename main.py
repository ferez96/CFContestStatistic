#!/usr/bin/env python3
"""
Chuong trinh thong ke ket qua thi Codeforces

Cau lac bo giai thuat truong Dai hoc Bach Khoa TPHCM
"""
__authors__ = ("Duong Thai Minh", "Nguyen Ho Minh Phuoc")
__version__ = '0.0.2'

import logging

import click

import crawling

# config logging
LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=LOGGING_FORMAT)
logging.getLogger(__name__).info("Logging configured")


@click.group(help=__doc__)
def cli():
    pass


@cli.command()
def ping():
    assert crawling.CodeForceHTTPClient().ping(), "Ping"


@cli.command("user-info")
@click.argument("handle")
def get_user_info(handle):
    user_info = crawling.CodeForceHTTPClient().send_request("user.info", dict(handles=handle))
    print(user_info)


def main():
    cli()


if __name__ == "__main__":
    main()
