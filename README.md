# design-content-analysis

A simple Python tool for analyzing text content stored inside database tables.

It connects to a MySQL database, extracts values from `field_data_` tables, removes HTML tags, and generates basic statistics about text length.

---

## What it does

- Connects to a MySQL database
- Reads tables starting with `field_data_`
- Extracts text content from fields
- Removes HTML from values
- Analyzes:
  - character length
  - word length
- Provides simple CLI commands to explore data

---

## Commands

After running the tool:

- `search <keyword>` → find tables containing keyword
- `display <table>` → show table data
- `stats <table>` → show statistics for a table
- `all` → list all loaded tables
- `help` → show available commands
- `quit` → exit the program

---

## How to run

Make sure MySQL is running, then:

```bash id="run1"
python main.py

```

You will be asked for:


```
host
user
password
database name

```
Requirements
```
Python 2.x (original version) or compatible MySQL Python driver
MySQL server
mysql-python library
```
Install dependency:
```
pip install MySQL-python
```

Notes: Designed mainly for Drupal-style databases 
       Only works with tables starting with field_data_
       Not optimized for large datasets
       Built for quick content length analysis, not production analytics

File structure
```
main.py → CLI entry point
core.py → core logic (analysis + DB helpers)
```
other files → optional modular structure (helpers, utilities)
