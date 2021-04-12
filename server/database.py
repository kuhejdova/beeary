import sqlite3
from datetime import datetime


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
    cur.execute('''CREATE TABLE temperature (hid integer, date text, year integer, month integer, value real)''')
    cur.execute('''CREATE TABLE weight (hid integer, date text, year integer, month integer, value real)''')
    cur.execute('''CREATE TABLE humidity (hid integer, date text, year integer, month integer, value real)''')
    cur.execute('''CREATE TABLE flow (hid integer, date text, year integer, month integer, value real)''')
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


def insert_hive(name, sid):
    con = sqlite3.connect('beeary.db')
    cur = con.cursor()
    sql = '''INSERT INTO hives(hive_name, sid) VALUES (?, ?)'''
    cur.execute(sql, (name, sid))
    con.commit()
    con.close()


def select_hives(sid):
    con = sqlite3.connect('beeary.db')
    cur = con.cursor()

    sql = '''SELECT hive_id, hive_name FROM hives WHERE sid = ?'''
    cur.execute(sql, (sid,))
    res = cur.fetchall()
    con.close()
    return res


def select_data_graph():
    curr_month = datetime.today().month
    con = sqlite3.connect('beeary.db')
    cur = con.cursor()

    sql = '''SELECT date, value FROM humidity WHERE month = ?'''
    cur.execute(sql, (curr_month,))
    res = cur.fetchall()
    con.close()
    return res


def graph_data_to_jsonify(graphdata):
    data_list = []
    for row in graphdata:
        line_dict = {'date': row[0], 'value': row[1]}
        data_list.append(line_dict)
    return data_list


def hives_to_jsonify(hives):
    res_list = []
    data = select_data_graph()
    for hive in hives:
        hive_dict = {'id': hive[0], 'name': hive[1], 'graph': graph_data_to_jsonify(data)}
        res_list.append(hive_dict)
    return res_list


def insert_notes(note_text, hid):
    con = sqlite3.connect('beeary.db')
    cur = con.cursor()
    sql = '''INSERT INTO notes(note_text, hid) VALUES (?, ?)'''
    cur.execute(sql, (note_text, hid))
    con.commit()
    con.close()


def select_notes(hid):
    con = sqlite3.connect('beeary.db')
    cur = con.cursor()

    sql = '''SELECT note_id, note_text FROM notes WHERE hid = ?'''
    cur.execute(sql, (hid,))
    res = cur.fetchall()
    con.close()
    return res


if __name__ == '__main__':
    # create_tables()
    uid = "gXifKfOg06XvU9NewGfqiFwasE12"
    # insert_sites('Stanoviste1', uid, 'Ostrava')
    # insert_sites('Bees', uid, 'Metylovice')
    # insert_sites('Something', uid, 'Brno')

    # insert_hive('ul1', 1)
    # insert_hive('ul2', 1)
    # insert_hive('ul3', 1)
    #
    # insert_hive('ul1', 3)
    # insert_hive('ul2', 3)
    result = select_hives(2)
    print(result)

