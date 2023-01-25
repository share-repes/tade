from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Create the "trading_view" database
db = client["trading_view"]

# Create the "users" collection
users = db["users"]

# Insert a sample user into the "users" collection
users.insert_one({
    "name": "John Smith",
    "email": "john.smith@example.com",
    "password": "password123",
    "date_created": "2022-01-01"
})

# Create the "symbols" collection
symbols = db["symbols"]

# Insert a sample symbol into the "symbols" collection
symbols.insert_one({
    "symbol": "AAPL",
    "name": "Apple Inc.",
    "exchange": "NASDAQ",
    "type": "stock",
    "industry": "Technology"
})

# Create the "charts" collection
charts = db["charts"]

# Insert a sample chart into the "charts" collection
charts.insert_one({
    "symbol_id": "AAPL",
    "time_frame": "1min",
    "data": [
        {
            "date": "2022-01-01",
            "open": 100,
            "high": 110,
            "low": 90,
            "close": 105,
            "volume": 10000
        },
        {
            "date": "2022-01-02",
            "open": 110,
            "high": 120,
            "low": 105,
            "close": 115,
            "volume": 12000
        }
    ],
    "date_created": "2022-01-01"
})

# Create the "indicators" collection
indicators = db["indicators"]

# Insert a sample indicator into the "indicators" collection
indicators.insert_one({
    "chart_id": "AAPL",
    "name": "RSI",
    "data": [
        {
            "date": "2022-01-01",
            "value": 70
        },
        {
            "date": "2022-01-02",
            "value": 75
        }
    ],
    "date_created": "2022-01-01"
})

# Create the "studies" collection
studies = db["studies"]

# Insert a sample study into the "studies" collection
studies.insert_one({
    "chart_id": "AAPL",
    "name": "Fibonacci Retracement",
    "data": [
        {
            "date": "2022-01-01",
            "value": 0.382
        },
        {
            "date": "2022-01-02",
            "value": 0.5
        }
    ],
    "date_created": "2022-01-01"
})

# Create the "watchlists" collection
watchlists = db["watchlists"]

# Insert
