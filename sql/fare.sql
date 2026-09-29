import sqlite3 -- import library for SQLite database operations

connection = sqlite3.connect('fare.db') -- connect to the database (or create it if it doesn't exist)
print("Database connection established.")
cursor = connection.cursor() -- create a cursor object to execute SQL commands
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tblBookings ( 
        fare_id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique fare rate ID 
        initial_rate INTEGER NOT NULL, -- Initial rate for the tax 
        fare_rate TEXT NOT NULL, -- Fare rate for the tax per minute
        surge_rate TEXT NOT NULL, -- Surge rate for the tax per minute
        
        
        FOREIGN KEY (trip_id) 
            REFERENCES tblBookings(trip_id) -- Foreign key constraint referencing the trips table
        )


    )



""") -- create the bookings table if it doesn't exist


