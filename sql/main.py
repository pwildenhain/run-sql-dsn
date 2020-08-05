from pathlib import Path

import pyodbc
from tabulate import tabulate
import typer

from args_help import AppArgs

app = typer.Typer()

command_args = AppArgs()


@app.command()
def run(
    sql: str = command_args.sql,
    dsn: str = command_args.dsn,
    display_column_limit: int = command_args.display_column_limit,
    display_row_limit: int = command_args.display_row_limit,
    display_format: str = command_args.display_format,
):
    """Run a SQL query using an ODBC data source name (dsn)"""
    conn = pyodbc.connect(f"dsn={dsn}")
    cursor = conn.cursor()
    result = cursor.execute(sql).fetchall()
    conn.close()

    col_names = [
        typer.style(column[0], bold=True)
        for column in cursor.description[:display_column_limit]
    ]
    result = [row[:display_column_limit] for row in result[:display_row_limit]]
    tablular_data = tabulate(result, headers=col_names, tablefmt=display_format)

    typer.echo(tablular_data)


@app.command()
def run_file(
    sql_file: Path = command_args.sql_file,
    dsn: str = command_args.dsn,
    display_column_limit: int = command_args.display_column_limit,
    display_row_limit: int = command_args.display_row_limit,
    display_format: str = command_args.display_format,
):
    """Run a SQL file using an ODBC data source name (dsn)"""
    with open(sql_file) as sql_file_io:
        sql = sql_file_io.read()

    run(
        sql=sql,
        dsn=dsn,
        display_column_limit=display_column_limit,
        display_row_limit=display_row_limit,
        display_format=display_format,
    )


if __name__ == "__main__":
    app()
