# run-sql-dsn

## Installation

Install from GitHub:

```
$ pip install --user git+https://github.com/pwildenhain/run-sql-dsn#egg=run-sql-dsn
```

Install shell completion

```
$ sql --install-completion
```

_Note: Windows users may need to manually modify paths in shell config files_

## Usage

Create an ODBC data source name (DSN). The setup will be OS dependent. Google is your friend :nerd_face:

Run a sql query:

```
$ sql run "select * from my_table" MY_DSN
+----------+----------+
| column_1 | column_2 |
+==========+==========+
| a        | 1        |
+----------+----------+
| b        | 2        |
+----------+----------+
| c        | 3        |
+----------+----------+
```

Or a sql file:

```
$ sql run-file test.sql MY_DSN
+----------+----------+
| column_1 | column_2 |
+==========+==========+
| a        | 1        |
+----------+----------+
| b        | 2        |
+----------+----------+
| c        | 3        |
+----------+----------+
```

Set a default DSN with the `RUN_SQL_DSN` environment variable:

```
$ export RUN_SQL_DSN=MY_DSN
$ sql run-file test.sql
+----------+----------+
| column_1 | column_2 |
+==========+==========+
| a        | 1        |
+----------+----------+
| b        | 2        |
+----------+----------+
| c        | 3        |
+----------+----------+
```

See `sql run --help` and `sql run-file --help` for a full list of CLI options.
