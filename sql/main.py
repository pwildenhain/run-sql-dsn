import pyodbc
from tabulate import tabulate
import typer

app = typer.Typer()


@app.command()
def run(
    sql: str = typer.Argument(..., help="SQL string to execute"),
    dsn: str = typer.Argument(
        "",
        help="ODBC dsn to connect to through pyodbc.connect()",
        envvar="RUN_SQL_DSN",
        show_default=False,
    ),
    column_limit: int = typer.Option(10, help="Number of columns to display in output"),
    row_limit: int = typer.Option(10, help="Number of rows to display in output"),
    display_format: str = typer.Option(
        "grid",
        help="Display style for output. See the tabulate package for more details",
    ),
):
    """Run a SQL query using and ODBC data source name (dsn)"""
    conn = pyodbc.connect(f"dsn={dsn}")
    cursor = conn.cursor()
    cursor.arraysize = row_limit
    result = cursor.execute(sql).fetchmany()
    conn.close()

    col_names = [typer.style(column[0], bold=True) for column in cursor.description]
    tablular_data = tabulate(result, headers=col_names, tablefmt=display_format)

    typer.echo(tablular_data)


if __name__ == "__main__":
    app()
