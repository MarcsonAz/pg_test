import urllib.parse as up
import psycopg2

DATABASE_URL = "postgres://hlmnkwzs:3fpr0W89DAFULiuX9BeGfS-aUWA0vuM8@motty.db.elephantsql.com:5432/hlmnkwzs"

url = up.urlparse(DATABASE_URL)
conn = psycopg2.connect(database=url.path[1:],
user=url.username,
password=url.password,
host=url.hostname,
port=url.port
)

