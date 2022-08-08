import psycopg2
import json
import sauce

DB_HOST = sauce.DB_HOST
DB_NAME = sauce.DB_NAME
DB_PASS = sauce.DB_PASS
DB_USER = sauce.DB_USER


def convertTime(dateTime, category) :
    time_format = "%m/%d/%Y" 
    if category == 'last_updated' :
        period = 'am' if dateTime.hour < 12 else 'pm'
        time_format += ", %I:%M " + period 
    return dateTime.strftime(time_format)


def convertToDict(user, keys) :
    dict_of_info = {}
    for i in range(0, len(keys)) :
        value = user[i]    
        if keys[i] == 'last_updated' or keys[i] == 'date_created' : 
            value = convertTime(user[i], keys[i])
        dict_of_info[keys[i]] = value
            
    return dict_of_info


# returns id
def sqlAddName(name) :
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
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
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
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
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
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
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
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


def sqlDeleteRecord(userID) : 
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        cur = conn.cursor()
        cur.execute('''
                DELETE from reg_users 
                where id = {}; 
        '''.format(userID))
        conn.commit()
        cur.close()
        conn.close()


def sqlGetMP3Name(userID) : 
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
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
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
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
    conn = psycopg2.connect(dbname=DB_NAME, user= DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor()
    cur.execute('''
            select img_enc_fn from reg_users 
            where id = {};
    '''.format(userID))
    img_enc_fn = cur.fetchall()[0][0]
    cur.close()
    conn.close()
    return img_enc_fn


def sqlGetImgEncs () :
    conn = psycopg2.connect(dbname=DB_NAME, user= DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor()
    cur.execute('''
            select name, img_enc_fn, id from reg_users
    ''')
    list_encs = cur.fetchall()
    cur.close()
    conn.close()
    return list_encs


def sqlGetAllUsers() :
    conn = psycopg2.connect(dbname=DB_NAME, user= DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor()
    cur.execute('''
            select id, 
            name, song_title, 
            youtube_url, img_fn, 
            last_updated, date_created 
            from reg_users
            order by last_updated desc
    ''')
    list_users = cur.fetchall()
    cur.close()
    conn.close()
    keys = ['id', 'name', 'song_title', 'youtube_url', 
           'img_fn', 'last_updated', 'date_created']
    dict_of_users = []
    for user in list_users :
        dict_of_users.append(convertToDict(user, keys))

    return json.dumps(dict_of_users) 
    

def sqlGetUser(userID) :
    conn = psycopg2.connect(dbname=DB_NAME, user= DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor()
    cur.execute('''
            select id, 
            name, song_title, 
            youtube_url, img_fn, 
            last_updated, date_created 
            from reg_users 
            where id = {}
    '''.format(userID))
    user = cur.fetchall()[0]
    cur.close()
    conn.close()
    keys = ['id', 'name', 'song_title', 'youtube_url', 
           'img_fn', 'last_updated', 'date_created']
    dict_of_users = []
    dict_of_users.append(convertToDict(user, keys))

    return json.dumps(dict_of_users) 
