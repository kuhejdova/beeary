import csv
import os
from datetime import datetime
from sqlalchemy import create_engine, text

connection_string = os.getenv('DATABASE_URL', default="postgresql+psycopg2://postgres:bakalarka@localhost:5432/beeary")
if connection_string.startswith("postgres://"):
    connection_string = connection_string.replace("postgres://", "postgresql://", 1)
engine = create_engine(connection_string)
conn = engine.connect()


def load_csv():
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
                    insert_line(updated_date, new_date.year, dt.month, round(float(row[1]), 2))
                line_count += 1
        print(f'read {line_count} lines')


def insert_line(date, year, month, value):
    sql = text('''INSERT INTO temperature(hid, date, year, month, value) VALUES (1, :d, :y, :m, :v)''')
    conn.execute(sql, d=date, y=year, m=month, v=value)


def load_csv_months():
    with open('months.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                insert_line_month(row[0], row[1], row[2])
                line_count += 1


def insert_line_month(month, description, pictogram):
    sql = '''INSERT INTO months(month_id, description, pictogram) VALUES (:mi, :d, :p)'''
    conn.execute(sql, mi=month, d=description, p=pictogram)


# if __name__ == '__main__':
#     load_csv()
