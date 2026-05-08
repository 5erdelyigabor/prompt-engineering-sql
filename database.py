import sqlite3

conn = sqlite3.connect("stocks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS investors(
    id INTEGER PRIMARY KEY,
    name TEXT,
    country TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS stocks(
    id INTEGER PRIMARY KEY,
    ticker TEXT,
    company_name TEXT,
    sector TEXT,
    price REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS portfolios(
    investor_id INTEGER,
    stock_id INTEGER,
    shares INTEGER,
    purchase_date TEXT
)
""")

cursor.executemany(
    "INSERT INTO investors(name, country) VALUES (?, ?)",
    [
        ("Alice", "USA"),
        ("Bob", "Germany"),
        ("Charlie", "Hungary")
    ]
)

cursor.executemany(
    "INSERT INTO stocks(ticker, company_name, sector, price) VALUES (?, ?, ?, ?)",
    [
        ("AAPL", "Apple", "Technology", 210),
        ("TSLA", "Tesla", "Automotive", 180),
        ("NVDA", "NVIDIA", "Technology", 950)
    ]
)

cursor.executemany(
    "INSERT INTO portfolios(investor_id, stock_id, shares, purchase_date) VALUES (?, ?, ?, ?)",
    [
        (1, 1, 10, "2024-01-10"),
        (1, 3, 5, "2024-03-15"),
        (2, 2, 20, "2023-11-20"),
        (3, 1, 7, "2025-01-01")
    ]
)

conn.commit()
conn.close()

print("Database created.")