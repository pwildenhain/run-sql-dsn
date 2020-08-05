from pathlib import Path
import typer


class AppArgs:
    sql: str = typer.Argument(..., help="SQL string to execute")
    sql_file: Path = typer.Argument(
        ...,
        help="SQL file to execute. Must contain a single SELECT statement",
        exists=True,
        readable=True,
    )
    dsn: str = typer.Argument(
        "",
        help="ODBC dsn to connect to through pyodbc.connect()",
        envvar="RUN_SQL_DSN",
        show_default=False,
    )
    display_column_limit: int = typer.Option(
        10, min=1, help="Number of columns to display in output"
    )
    display_row_limit: int = typer.Option(
        10, min=1, help="Number of rows to display in output"
    )
    display_format: str = typer.Option(
        "grid",
        help="Display style for output. See the tabulate package for more details",
    )
