import psycopg2
import sauce

# def createNewUser(name, img_fn, img_enc_fn, song_title, mp3_fn, yt_url) :
#     conn = psycopg2.connect(dbname=sauce.DB_NAME, user= sauce.DB_USER, password=sauce.DB_PASS, host=sauce.DB_HOST)
#     cur = conn.cursor()
#     cur.execute(sauce.insert(name, img_fn, img_enc_fn, song_title, mp3_fn, yt_url))


conn = psycopg2.connect(dbname=sauce.DB_NAME, user= sauce.DB_USER, password=sauce.DB_PASS, host=sauce.DB_HOST)

cur = conn.cursor()

cur.execute("SELECT CURRENT_TIMESTAMP(0) AT TIME ZONE 'America/Chicago'")


#cur.execute("SELECT CURRENT_DATE")
print(cur.fetchall())
# cur.execute("SELECT * FROM reg_users")
# print(cur.fetchall())

cur.close()

conn.close()