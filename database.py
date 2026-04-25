import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="weather_db"
    )

def insert_data(data):
    conn = connect_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO weather_data 
    (city, temperature, feels_like, humidity, pressure, weather, wind_speed, timestamp)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        data["city"],
        data["temperature"],
        data["feels_like"],
        data["humidity"],
        data["pressure"],
        data["weather"],
        data["wind_speed"],
        data["timestamp"]
    )

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()