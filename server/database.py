import os
from datetime import datetime, timedelta
from sqlalchemy import create_engine, text

connection_string = os.getenv('DATABASE_URL', default="postgresql+psycopg2://postgres:bakalarka@localhost:5432/beeary")
if connection_string.startswith("postgres://"):
    connection_string = connection_string.replace("postgres://", "postgresql://", 1)
engine = create_engine(connection_string)
conn = engine.connect()


def insert_sites(name, email, location):
    sql = text('''INSERT INTO sites(site_name, uid, location) VALUES (:n, :u, :l)''')
    conn.execute(sql, n=name, u=email, l=location)


def select_sites(email):
    sql = text('''
    SELECT site_id, site_name, location,   CASE
    WHEN hives_count is not null THEN 1
    ELSE 0 
  END 
  AS have_hive
    FROM sites 
    LEFT JOIN (SELECT COUNT(*) as hives_count, sid FROM hives group by sid) as hive_count on hive_count.sid = site_id 
    WHERE uid = :u ORDER BY site_id
    ''')
    data = conn.execute(sql, u=email)
    return data.fetchall()


def delete_site(sid):
    sql = text('''DELETE FROM sites WHERE site_id = :s''')
    conn.execute(sql, s=sid)


def sites_to_jsonify(sites):
    res_list = []
    for site in sites:
        site_dict = {'id': site[0], 'name': site[1], 'location': site[2], 'have_hive': site[3]}
        res_list.append(site_dict)
    return res_list


def insert_hive(name, sid):
    sql = text('''INSERT INTO hives(hive_name, sid) VALUES (:h, :s)''')
    conn.execute(sql, h=name, s=sid)


def select_hives(sid):
    sql = text('''SELECT hive_id, hive_name FROM hives WHERE sid = :s''')
    res = conn.execute(sql, s=sid)
    return res.fetchall()


def delete_hive(hid):
    sql = text('''DELETE FROM hives WHERE hive_id = :h''')
    conn.execute(sql, h=hid)


def select_humidity_graph(date_from, date_to):
    sql = text("SELECT date, value FROM humidity WHERE date BETWEEN \'" + date_from + "\' AND \'" + date_to + "\'")
    res = conn.execute(sql)
    return res.fetchall()


def select_temperature_graph(date_from, date_to):
    sql = text("SELECT date, value FROM temperature WHERE date BETWEEN \'" + date_from + "\' AND \'" + date_to + "\'")
    res = conn.execute(sql)
    return res.fetchall()


def select_weight_graph(date_from, date_to):
    conn = engine.connect()
    sql = "SELECT date, value FROM weight  WHERE date BETWEEN \'" + date_from + "\' AND \'" + date_to + "\'"
    res = conn.execute(sql)
    return res.fetchall()


def graph_data_to_jsonify(graphdata):
    data_list = []
    for row in graphdata:
        line_dict = {'date': row[0], 'value': row[1]}
        data_list.append(line_dict)
    return data_list


def generate_warnings_humidity(graphdata):
    dates_list = []
    for row in graphdata:
        if 0 <= row[1] < 95:
            continue
        dt = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
        only_date = datetime.strftime(dt, '%Y-%m-%d')
        if only_date in dates_list:
            continue
        dates_list.append(only_date)
        sql = text('''INSERT INTO warnings(hid, sid, warning_text, warning_date) VALUES (1, 1, :t, :d)''')
        text_warning = "P????li?? vysok?? vlhkost (nad 95%)" if row[1] >= 95 else "Probl??m se senzorem, zkontroluje baterie"
        conn.execute(sql, t=text_warning, d=only_date)


def generate_warnings_temperature(graphdata):
    dates_list = []
    for row in graphdata:
        if 10 <= row[1]:
            continue
        dt = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
        only_date = datetime.strftime(dt, '%Y-%m-%d')
        if only_date in dates_list:
            continue
        dates_list.append(only_date)
        sql = '''INSERT INTO warnings_temperature(hid, sid, warning_text, warning_date) VALUES (1, 1, :t, :d)'''
        text_warning = "P????li?? n??zk?? teplota (pod 10??C), hroz?? promrznut?? v??el"
        conn.execute(sql, t=text_warning, d=only_date)


def generate_warnings_weight(graphdata):
    for i in range(len(graphdata)-1):
        if i == 0:
            continue
        if abs(graphdata[i][1] - graphdata[i-1][1]) < 5:
            continue
        dt = datetime.strptime(graphdata[i][0], '%Y-%m-%d %H:%M:%S')
        format_date = datetime.strftime(dt, '%Y-%m-%d')
        sql = '''INSERT INTO warnings_weight(hid, sid, warning_text, warning_date) VALUES (1, 1, %s, %s)'''
        text_warning = "Velk?? rozd??l hmotnosti (v??ce ne?? 5 kg)"
        conn.execute(sql, (text_warning, format_date))


def warnings_to_jsonify(table_name, date_from, date_to):
    sql = text("SELECT warning_date, warning_text FROM " + table_name +
               " WHERE warning_date BETWEEN \'" + date_from + "\' AND \'" + date_to + "\'")
    data = conn.execute(sql, t=table_name)
    res = data.fetchall()

    data_list = []
    for row in res:
        line_dict = {'date': row[0], 'value': row[1]}
        data_list.append(line_dict)
    return data_list


def hive_with_graphs(hid, date_from, date_to):
    sql = text('''SELECT hive_name FROM hives WHERE hive_id = :h''')
    data = conn.execute(sql, h=hid)
    hive = data.fetchone()

    res_list = []

    date_from_date = datetime.strptime(date_from, '%d.%m.%Y')
    date_to_date = datetime.strptime(date_to, '%d.%m.%Y')

    date_to = date_to_date.strftime('%Y-%m-%d %H:%M:%S')
    date_from = date_from_date.strftime('%Y-%m-%d %H:%M:%S')

    data_humidity = select_humidity_graph(date_from, date_to)
    data_temperature = select_temperature_graph(date_from, date_to)
    data_weight = select_weight_graph(date_from, date_to)
    hive_dict = {}

    if hive is not None:
        hive_dict = {'name': hive[0],
                     'humidity': graph_data_to_jsonify(data_humidity),
                     'temperature': graph_data_to_jsonify(data_temperature),
                     'weight': graph_data_to_jsonify(data_weight),
                     'warnings': warnings_to_jsonify("warnings", date_from, date_to),
                     'warnings_temperature': warnings_to_jsonify("warnings_temperature", date_from, date_to),
                     'warnings_weight': warnings_to_jsonify("warnings_weight", date_from, date_to)}
    res_list.append(hive_dict)
    return res_list


def hives_to_jsonify(hives):
    res_list = []

    now = datetime.today()
    last_week = now - timedelta(days=7)

    date_to = now.strftime('%Y-%m-%d %H:%M:%S')
    date_from = last_week.strftime('%Y-%m-%d %H:%M:%S')

    data_humidity = select_humidity_graph(date_from, date_to)
    data_temperature = select_temperature_graph(date_from, date_to)
    data_weight = select_weight_graph(date_from, date_to)
    for hive in hives:
        hive_dict = {'id': hive[0], 'name': hive[1],
                     'humidity': graph_data_to_jsonify(data_humidity),
                     'temperature': graph_data_to_jsonify(data_temperature),
                     'weight': graph_data_to_jsonify(data_weight)}
        res_list.append(hive_dict)
    return res_list


def select_month(month):
    sql = text('''SELECT description, pictogram  FROM months WHERE month_id = :m''')
    res = conn.execute(sql, m=month)
    return res.fetchall()


def months_to_jsonify(activities):
    res_list = []
    for activity in activities:
        act_dict = {'description': activity[0], 'pictogram': activity[1]}
        res_list.append(act_dict)
    return res_list


def insert_notes(note_text, hid, note_date):
    sql = text('''INSERT INTO notes(note_text, hid, note_date) VALUES (:t, :h, :d)''')
    conn.execute(sql, t=note_text, h=hid, d=note_date)


def select_notes(hid):
    sql = text('''SELECT note_id, note_text, note_date 
                  FROM notes 
                  WHERE hid = :h 
                  ORDER BY TO_DATE(note_date, 'DD.MM.YYYY')''')
    res = conn.execute(sql, h=hid)
    return res.fetchall()


def notes_to_jsonify(notes):
    res_list = []
    for note in notes:
        act_dict = {'note_id': note[0], 'note_text': note[1], 'note_date': note[2]}
        res_list.append(act_dict)
    return res_list


def delete_note(note_id):
    sql = text('''DELETE FROM notes WHERE note_id = :n''')
    conn.execute(sql, n=note_id)


def select_user(email):
    sql = text('''SELECT password FROM users WHERE email = :e''')
    res = conn.execute(sql, e=email)
    return res.fetchone()


def insert_user(email, password):
    sql = text('''INSERT INTO users(email, password) VALUES (:e, :p)''')
    conn.execute(sql, e=email, p=password)


if __name__ == '__main__':
    pass

