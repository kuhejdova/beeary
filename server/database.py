import sqlite3


def create_connection():
    con = sqlite3.connect('beeary.db')
    cur = con.cursor()
    return con, cur


def create_tables():
    con = sqlite3.connect('beeary.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE sites (site_id INTEGER PRIMARY KEY, site_name text, uid text, location text)''')
    cur.execute('''CREATE TABLE hives (hive_id INTEGER PRIMARY KEY, hive_name text, sid integer)''')
    cur.execute('''CREATE TABLE data (hid integer, date text, value real)''')
    cur.execute('''CREATE TABLE notes (hid integer, note_text text)''')
    con.commit()
    con.close()


def insert_sites(name, uid, location):
    con = sqlite3.connect('beeary.db')
    cur = con.cursor()
    sql = '''INSERT INTO sites(site_name, uid, location) VALUES (?, ?, ?)'''
    cur.execute(sql, (name, uid, location))
    con.commit()
    con.close()


def select_sites(uid):
    con = sqlite3.connect('beeary.db')
    cur = con.cursor()
    sql = '''SELECT site_id, site_name, location FROM sites WHERE uid = ?'''
    cur.execute(sql, (uid, ))
    # con.commit()
    res = cur.fetchall()
    con.close()
    return res


def sites_to_jsonify(sites):
    res_list = []
    for site in sites:
        site_dict = {'id': site[0], 'name': site[1], 'location': site[2], 'event': 'Žádná nová událost'}
        res_list.append(site_dict)
    return res_list


if __name__ == '__main__':
    # create_tables()
    uid = "gXifKfOg06XvU9NewGfqiFwasE12"
    # insert_sites('Stanoviste1', uid, 'Ostrava')
    # insert_sites('Bees', uid, 'Metylovice')
    # insert_sites('Something', uid, 'Brno')
    result = select_sites(uid)
    # con.close()

