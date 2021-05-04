import sqlite3
from datetime import datetime, timedelta


def create_connection():
    con = sqlite3.connect('beeary.db')
    cur = con.cursor()
    return con, cur


def create_tables():
    con = sqlite3.connect('beeary.db')
    cur = con.cursor()
    # cur.execute('''CREATE TABLE sites (site_id INTEGER PRIMARY KEY, site_name text, uid text, location text)''')
    # cur.execute('''CREATE TABLE hives (hive_id INTEGER PRIMARY KEY, hive_name text, sid integer)''')
    # cur.execute('''CREATE TABLE notes (note_id integer primary key, hid integer, note_text text, note_date text)''')
    # cur.execute('''CREATE TABLE temperature (hid integer, date text, year integer, month integer, value real)''')
    # cur.execute('''CREATE TABLE weight (hid integer, date text, year integer, month integer, value real)''')
    # cur.execute('''CREATE TABLE humidity (hid integer, date text, year integer, month integer, value real)''')
    # cur.execute('''CREATE TABLE months (id integer primary key, month_id integer, description text, pictogram integer)''')
    # cur.execute('''CREATE TABLE warnings (warning_id integer primary key, hid integer, sid integer, warning_text text, warning_date text)''')
    cur.execute(
        '''CREATE TABLE warnings_temperature (warning_id integer primary key, hid integer, sid integer, warning_text text, warning_date text)''')
    cur.execute(
        '''CREATE TABLE warnings_weight (warning_id integer primary key, hid integer, sid integer, warning_text text, warning_date text)''')
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


def select_humidity_graph():
    # curr_month = datetime.today().month
    con = sqlite3.connect('beeary.db')
    cur = con.cursor()

    sql = '''SELECT date, value FROM humidity'''
    cur.execute(sql)
    res = cur.fetchall()
    con.close()
    return res


def select_temperature_graph():
    # curr_month = datetime.today().month
    con = sqlite3.connect('beeary.db')
    cur = con.cursor()

    sql = '''SELECT date, value FROM temperature'''
    cur.execute(sql)
    res = cur.fetchall()
    con.close()
    return res


def select_weight_graph():
    # curr_month = datetime.today().month
    con = sqlite3.connect('beeary.db')
    cur = con.cursor()

    sql = '''SELECT date, value FROM weight'''
    cur.execute(sql)
    res = cur.fetchall()
    con.close()
    return res


def graph_data_to_jsonify(graphdata):
    data_list = []
    now = datetime.today()
    fake_now = now
    week_back = fake_now - timedelta(days=7)
    for row in graphdata:
        dt = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
        if week_back <= dt <= fake_now:
            line_dict = {'date': row[0], 'value': row[1]}
            data_list.append(line_dict)
    return data_list


def graph_data_by_date_to_jsonify(graphdata, date_from, date_to):
    data_list = []
    now = datetime.today()
    # fake_now = now - timedelta(days=2*366-1)
    date_from_date = datetime.strptime(date_from, '%d.%m.%Y')
    date_to_date = datetime.strptime(date_to, '%d.%m.%Y')
    # week_back = fake_now - timedelta(days=7)
    for row in graphdata:
        dt = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
        if date_from_date <= dt <= date_to_date:
            line_dict = {'date': row[0], 'value': row[1]}
            data_list.append(line_dict)
    return data_list


def generate_warnings_humidity(graphdata):
    con = sqlite3.connect('beeary.db')
    cur = con.cursor()
    dates_list = []
    for row in graphdata:
        if 0 <= row[1] < 95:
            continue
        dt = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
        only_date = datetime.strftime(dt, '%Y-%m-%d')
        if only_date in dates_list:
            continue
        dates_list.append(only_date)
        sql = '''INSERT INTO warnings(hid, sid, warning_text, warning_date) VALUES (?, ?, ?, ?)'''
        cur.execute(sql, (1, 1, "Příliš vysoká vlhkost (nad 95%)" if row[1] >= 95 else "Problém se senzorem, zkontroluje baterie", only_date))
        con.commit()
    con.close()


def generate_warnings_temperature(graphdata):
    con = sqlite3.connect('beeary.db')
    cur = con.cursor()
    dates_list = []
    for row in graphdata:
        if 10 <= row[1]:
            continue
        dt = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
        only_date = datetime.strftime(dt, '%Y-%m-%d')
        if only_date in dates_list:
            continue
        dates_list.append(only_date)
        sql = '''INSERT INTO warnings_temperature(hid, sid, warning_text, warning_date) VALUES (?, ?, ?, ?)'''
        cur.execute(sql, (1, 1, "Příliš nízká teplota (pod 10°C), hrozí promrznutí včel", only_date))
        con.commit()
    con.close()


def warnings_to_jsonify(date_from, date_to):
    con = sqlite3.connect('beeary.db')
    cur = con.cursor()
    sql = '''SELECT warning_date, warning_text FROM warnings'''
    cur.execute(sql)
    res = cur.fetchall()
    con.close()

    data_list = []
    date_from_date = datetime.strptime(date_from, '%d.%m.%Y')
    date_to_date = datetime.strptime(date_to, '%d.%m.%Y')
    for row in res:
        dt = datetime.strptime(row[0], '%Y-%m-%d')
        if date_from_date <= dt < date_to_date:
            line_dict = {'date': row[0], 'value': row[1]}
            data_list.append(line_dict)
    return data_list


def hive_with_graphs(hid, date_from, date_to):
    con = sqlite3.connect('beeary.db')
    cur = con.cursor()

    sql = '''SELECT hive_name FROM hives WHERE hive_id = ?'''
    cur.execute(sql, (hid,))
    hive = cur.fetchone()
    con.close()

    res_list = []
    data_humidity = select_humidity_graph()
    data_temperature = select_temperature_graph()
    data_weight = select_weight_graph()

    hive_dict = {'name': hive[0],
                 'humidity': graph_data_by_date_to_jsonify(data_humidity, date_from, date_to),
                 'temperature': graph_data_by_date_to_jsonify(data_temperature, date_from, date_to),
                 'weight': graph_data_by_date_to_jsonify(data_weight, date_from, date_to),
                 'warnings': warnings_to_jsonify(date_from, date_to)}
    res_list.append(hive_dict)
    return res_list


def hives_to_jsonify(hives):
    res_list = []
    data_humidity = select_humidity_graph()
    data_temperature = select_temperature_graph()
    data_weight = select_weight_graph()
    for hive in hives:
        hive_dict = {'id': hive[0], 'name': hive[1],
                     'humidity': graph_data_to_jsonify(data_humidity),
                     'temperature': graph_data_to_jsonify(data_temperature),
                     'weight': graph_data_to_jsonify(data_weight)}
        res_list.append(hive_dict)
    return res_list


def select_month(month):
    con = sqlite3.connect('beeary.db')
    cur = con.cursor()
    sql = '''SELECT description, pictogram  FROM months WHERE month_id = ?'''
    cur.execute(sql, (month, ))
    # con.commit()
    res = cur.fetchall()
    con.close()
    return res


def months_to_jsonify(activities):
    res_list = []
    for activity in activities:
        act_dict = {'description': activity[0], 'pictogram': activity[1]}
        res_list.append(act_dict)
    return res_list


def insert_notes(note_text, hid, note_date):
    con = sqlite3.connect('beeary.db')
    cur = con.cursor()
    sql = '''INSERT INTO notes(note_text, hid, note_date) VALUES (?, ?, ?)'''
    cur.execute(sql, (note_text, hid, note_date))
    con.commit()
    con.close()


def select_notes(hid):
    con = sqlite3.connect('beeary.db')
    cur = con.cursor()

    sql = '''SELECT note_text, note_date FROM notes WHERE hid = ?'''
    cur.execute(sql, (hid,))
    res = cur.fetchall()
    con.close()
    return res


def notes_to_jsonify(notes):
    res_list = []
    for note in notes:
        act_dict = {'note_text': note[0], 'note_date': note[1]}
        res_list.append(act_dict)
    return res_list


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
    # result = select_hives(2)
    # print(result)
    # graphdata = select_humidity_graph()
    # generate_warnings_humidity(graphdata)
    # graphdata = select_temperature_graph()
    # generate_warnings_temperature(graphdata)

