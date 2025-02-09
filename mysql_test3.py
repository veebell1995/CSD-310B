import mysql.connector
from mysql.connector import errorcode
import dotenv
from dotenv import dotenv_values

# Load the environment variables from the .env file
dotenv.load_dotenv()

# Read the environment variables from the .env file
secrets = dotenv_values(".env")

# Check if secrets are being loaded correctly (print them out)
print(secrets)

# Database config object
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print(f"\n  Database user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}")
    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
