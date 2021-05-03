import sqlite3
import csv
from datetime import datetime


def create_connection():
    con = sqlite3.connect('../beeary.db')
    cur = con.cursor()
    return con, cur


def load_csv():
    con, cur = create_connection()
    with open('temperature_schwartau.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                dt = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
                if dt.year == 2018:
                    break
                if dt.minute == 0 and row[1] != '':
                    new_date = datetime(dt.year + 4, dt.month, dt.day, dt.hour, dt.minute, dt.second)
                    updated_date = datetime.strftime(new_date, '%Y-%m-%d %H:%M:%S')
                    # insert_line(con, cur, updated_date, new_date.year, dt.month, round(float(row[1])/1000, 2))
                    insert_line(con, cur, updated_date, new_date.year, dt.month, round(float(row[1]), 2))
                line_count += 1
        print(f'read {line_count} lines')
    con.close()


def insert_line(con, cur, date, year, month, value):
    sql = '''INSERT INTO temperature(hid, date, year, month, value) VALUES (1, ?, ?, ?, ?)'''
    cur.execute(sql, (date, year, month, value))
    con.commit()


def load_csv_months():
    con, cur = create_connection()
    with open('months.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                insert_line_month(con, cur, row[0], row[1], row[2])
                line_count += 1
    con.close()


def insert_line_month(con, cur, month, description, pictogram):
    sql = '''INSERT INTO months(month_id, description, pictogram) VALUES (?, ?, ?)'''
    cur.execute(sql, (month, description, pictogram))
    con.commit()


# if __name__ == '__main__':
#     load_csv()
