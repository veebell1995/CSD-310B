import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Fizzliving4!",
    database="movies"
)

# Create a cursor object
cursor = db.cursor()

# Query 1: Select all fields from the studio table
cursor.execute("SELECT * FROM studio;")
studios = cursor.fetchall()
print("All Studio Details:")
for studio in studios:
    print(studio)
print("\n")

# Query 2: Select all fields from the genre table
cursor.execute("SELECT * FROM genre;")
genres = cursor.fetchall()
print("All Genre Details:")
for genre in genres:
    print(genre)
print("\n")

# Query 3: Select movie names with a runtime of less than two hours (120 minutes)
cursor.execute("SELECT film_name FROM film WHERE film_runtime < 120;")
short_films = cursor.fetchall()
print("Movies with Runtime Less Than 2 Hours:")
for film in short_films:
    print(film[0])
print("\n")

# Query 4: List film names and directors grouped by director
cursor.execute("SELECT film_director, GROUP_CONCAT(film_name) FROM film GROUP BY film_director;")
directors = cursor.fetchall()
print("Films Grouped by Director:")
for director in directors:
    print(f"Director: {director[0]}\nMovies: {director[1]}\n")

# Close the cursor and connection
cursor.close()
db.close()

