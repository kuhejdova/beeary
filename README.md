# Beeary

## Český návod

---------------

Tento postup byl vytvořen pro Linux Ubuntu.

### Před spuštěním

Pro spuštění aplikace je potřeba mít nainstalovaný Python 3.8, Node.js a npm a PostgreSQL.

Dále je potřeba nainstalovat všechny závislosti
```
npm install
```
```
pip install -r requirements.txt
```

### Databáze

Je třeba vytvořit prázdnou PostgreSQL databázi, do které dále importujete dump databáze s názvem beeary.sql

### Spuštění Python backendu

Před spuštěním je třeba nastavit do env proměnné DATABASE_URL váš connection string, kterým se připojíte k vlastní databázi.

```
source env/bin/activate

DATABASE_URL=your_connection_string python app.py
```

### Spuštění Vue.js frontendu
```
npm run serve
```


## English version

---------------

This works for Linux Ubuntu,

### Setup

It is necessary to have installed Python 3.8, Node.js and npm and PostgreSQL.

Also it is required to install all dependencies

```
npm install
```
```
pip install -r requirements.txt
```

### Database

It is necessary to create empty PostgreSQL database where you import dump of database called beeary.sql


### Run Python backend

Before run it is required to setup env variable DATABASE_URL with your connection string for connecting to your creaded database.


```
source env/bin/activate

DATABASE_URL=your_connection_string python app.py
```

### Run Vue.js frontend
```
npm run serve
```


<!-- ## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```



## Run Python backend
```
source env/bin/activate

python app.py
```

## Postgres DB
```
sudo -u postgres psql
``` -->




[comment]: <> (### Compiles and minifies for production)

[comment]: <> (```)

[comment]: <> (npm run build)

[comment]: <> (```)

[comment]: <> (### Lints and fixes files)

[comment]: <> (```)

[comment]: <> (npm run lint)

[comment]: <> (```)

[comment]: <> (### Customize configuration)

[comment]: <> (See [Configuration Reference]&#40;https://cli.vuejs.org/config/&#41;.)
