import psycopg2

conn = psycopg2.connect(
    host= "localhost",
    database="rapidapi_heroku",
    user="postgres",
    password="Aguiainteligente"
)

cur = conn.cursor()


cur.execute("insert into covid19beta (country,confirmed,deaths,recovered,datetime_data) values(%s, %s, %s, %s, %s)",
("Brasil",1,0,0,"2020-02-28T00:00:00Z"))

cur.execute("select * from covid19beta")

rows = cur.fetchall()

for r in rows:
    print(r)

# enviar pro server    
conn.commit()
# fechar cursor
cur.close()
# fechar conexao
conn.close()