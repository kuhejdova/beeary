# Beeary

Aplikace je dostupná na https://beeary.herokuapp.com/

Při prvním spuštění může načítání trvat déle, heroku aplikace automaticky po nějaké době uspí.

---

## Český návod

---

Tento postup byl vytvořen pro Linux Ubuntu.

### Před spuštěním

Pro spuštění aplikace je potřeba mít nainstalovaný Python 3.8, Node.js a npm a PostgreSQL.

```
apt install -y python3.8 python3-pip nodejs npm postgresql libpq-dev
```

Dále je potřeba nainstalovat všechny závislosti

```
npm install
```

```
pip install -r requirements.txt
```

### Databáze

Je třeba vytvořit prázdnou PostgreSQL databázi, do které dále importujete dump databáze s názvem beeary.sql

```
service postgresql start
su postgres
createdb beeary
psql beeary < server/beeary.sql
```

### Spuštění Python backendu

Spustí Python backend s env proměnnou DATABASE_URL.

```
DATABASE_URL=postgresql+psycopg2:///beeary python3 server/app.py
```

### Spuštění Vue.js frontendu

```
npm run serve
```

---

## English version

---

This works for Linux Ubuntu,

### Setup

It is necessary to have installed Python 3.8, Node.js and npm and PostgreSQL.

```
apt install -y python3.8 python3-pip nodejs npm postgresql libpq-dev
```

Also it is required to install all dependencies

```
npm install
```

```
pip install -r requirements.txt
```

### Database

It is necessary to create empty PostgreSQL database where you import dump of database called beeary.sql

```
service postgresql start
su postgres
createdb beeary
psql beeary < server/beeary.sql
```

### Run Python backend

Run backend with env variable DATABASE_URL.

```
DATABASE_URL=postgresql+psycopg2:///beeary python3 server/app.py
```

### Run Vue.js frontend

```
npm run serve
```
