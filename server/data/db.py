import sqlite3
import click
from flask import current_app


def init_app(app):
    app.teardown_context(close_db)
    app.cli.add_command(init_db_command)
    return


def init_db():
    db = sqlite3.get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode('utf8'))

    return


@click.command("init-db")
def init_db_command():
    init_db()
    click.echo("Initialized the database.")
    return


def close_db():
    # TODO
    return
