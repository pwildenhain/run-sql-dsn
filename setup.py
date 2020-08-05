from setuptools import setup

setup(
    name="run-sql-dsn",
    version="0.1",
    install_requires=["pyodbc", "tabulate", "typer[all]"],
    packages=["sql"],
    entry_points={"console_scripts": ["sql = sql.main:app",],},
)
