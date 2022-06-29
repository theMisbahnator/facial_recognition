import psycopg2
import sauce


# returns id
def sqlAddName(name) :
    conn = psycopg2.connect(dbname=sauce.DB_NAME, user= sauce.DB_USER, password=sauce.DB_PASS, host=sauce.DB_HOST)
    cur = conn.cursor()
    cur.execute('''
            INSERT INTO reg_users (name, last_updated, date_created)
            VALUES ('{}', CURRENT_TIMESTAMP(0) AT TIME ZONE 'America/Chicago', current_date AT TIME ZONE 'America/Chicago');
    '''.format(name))
    conn.commit()
    cur.execute('''
            select id from reg_users
            where name = '{}'
            ORDER BY last_updated DESC
            LIMIT 1
    '''.format(name))
    userId = cur.fetchall()[0][0]
    cur.close()
    conn.close()
    return userId


def sqlAddUser(userId, name, yt_url, mp3_fn, song_title, img_fn, img_enc_fn) : 
    conn = psycopg2.connect(dbname=sauce.DB_NAME, user= sauce.DB_USER, password=sauce.DB_PASS, host=sauce.DB_HOST)
    cur = conn.cursor()
    cur.execute('''
            UPDATE reg_users
            SET img_fn = '{}', 
            img_enc_fn = '{}',
            song_title = '{}',
            mp3_fn = '{}',
            youtube_url = '{}'
            WHERE id = {};
    '''.format(img_fn, img_enc_fn, song_title, mp3_fn, yt_url, userId))
    conn.commit()
    cur.close()
    conn.close()


def sqlModifySong(userID, mp3_fn, song_title, yt_url) : 
    conn = psycopg2.connect(dbname=sauce.DB_NAME, user= sauce.DB_USER, password=sauce.DB_PASS, host=sauce.DB_HOST)
    cur = conn.cursor()
    cur.execute('''
            UPDATE reg_users
            SET mp3_fn = '{}', 
            song_title = '{}',
            youtube_url = '{}',
            last_updated = CURRENT_TIMESTAMP(0) AT TIME ZONE 'America/Chicago'
            WHERE id = {};
    '''.format(mp3_fn, song_title, yt_url, userID))
    conn.commit()
    cur.close()
    conn.close()
    

def sqlModifyFaceImg(userID, img_fn, img_enc_fn) :
        conn = psycopg2.connect(dbname=sauce.DB_NAME, user= sauce.DB_USER, password=sauce.DB_PASS, host=sauce.DB_HOST)
        cur = conn.cursor()
        cur.execute('''
                UPDATE reg_users
                SET img_fn = '{}', 
                img_enc_fn = '{}',
                last_updated = CURRENT_TIMESTAMP(0) AT TIME ZONE 'America/Chicago'
                WHERE id = {};
        '''.format(img_fn, img_enc_fn, userID))
        conn.commit()
        cur.close()
        conn.close()


def sqlGetMP3Name(userID) : 
    conn = psycopg2.connect(dbname=sauce.DB_NAME, user= sauce.DB_USER, password=sauce.DB_PASS, host=sauce.DB_HOST)
    cur = conn.cursor()
    cur.execute('''
            select mp3_fn from reg_users 
            where id = {};
    '''.format(userID))
    mp3_fn = cur.fetchall()[0][0]
    cur.close()
    conn.close()
    return mp3_fn


def sqlGetImgName(userID) : 
    conn = psycopg2.connect(dbname=sauce.DB_NAME, user= sauce.DB_USER, password=sauce.DB_PASS, host=sauce.DB_HOST)
    cur = conn.cursor()
    cur.execute('''
            select img_fn from reg_users 
            where id = {};
    '''.format(userID))
    img_fn = cur.fetchall()[0][0]
    cur.close()
    conn.close()
    return img_fn


def sqlGetImgEncName(userID) : 
    conn = psycopg2.connect(dbname=sauce.DB_NAME, user= sauce.DB_USER, password=sauce.DB_PASS, host=sauce.DB_HOST)
    cur = conn.cursor()
    cur.execute('''
            select img_enc_fn from reg_users 
            where id = {};
    '''.format(userID))
    img_enc_fn = cur.fetchall()[0][0]
    cur.close()
    conn.close()
    return img_enc_fn



    
