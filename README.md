# Flask / Celery / Redis Tests
Implementing celery in a flask application, so that users do not have to wait extended periods of time for transactions to complete.
Redis being used as backend broker, however can be subbed out for memcached, RabbitMQ.
Postgres being used as database, however can be subbed out for mysql, sqlserver, sqlite3 etc.
This repo is based on a `Mac OS` and `Python 3.6.5`.

# Before you get started
- Basic understanding of python and web servers
- Knowledge of Redis/Message brokers
- Knowledge of ORM and relational databases
- Knowledge of Flask
- Knowledge of Celery

# Setup
**How to obtain this repository:**
```sh
git clone https//link.to.this.projects.git-repo
```
**Installation of Redis on Mac**
```sh
# Installation
brew install redis

# Restarting service
brew service restart redis
```

**Modules/dependencies Python3:**
- `celery`
- `flask`

Install the following dependences:
```sh
pip install flask celery
```

# Getting up and running

### Starting the web application
The application has two routes only which insert several thousand records to a database
1. localhost:5000/process (no celery)
2. localhost:5000/async (implements celery worker)
```sh
cd /location/of/cloned/repo
python3 application.py
```

### Starting the celery worker
```sh
celery -A application.celery worker --concurrency 2 --loglevel=info
```

### Starting the redis brew service
```sh
brew services restart redis
```

### Checking services in brew
```sh
brew services list
```

# Tests
- Installation of Redis.
- Installation of Celery.
- Tested non async route to push n records to database.
- Tested async route to push n records to database.

**Note:** commits were failing when the /async route was being requested rapidly. Fixed by changing `--concurrency` flag to `2` when starting a celery worker.

# Contributors
- Daniel Corcoran

# Sources
- [Installing Redis on Mac](https://medium.com/@petehouston/install-and-config-redis-on-mac-os-x-via-homebrew-eb8df9a4f298)
- [Flask, Celery & SQLAlchemy Example by PrettyPrinted](https://www.youtube.com/watch?v=lOirTBrOek0)

# Screenshots
### Starting the celery service
![](https://github.com/danielc92/flask-celery-tests/blob/master/screenshots/Screen%20Shot%202019-03-28%20at%201.59.47%20pm.png)
### The timing of `/process` route (non-async)
This route is not using celery, therefore waits until the entire insert() function is complete until the user receives the return code. It takes about 8 seconds to insert 30,000 records to postgres.
![](https://github.com/danielc92/flask-celery-tests/blob/master/screenshots/Screen%20Shot%202019-03-28%20at%202.02.55%20pm.png)
### The timing of `/async` route (async)
In this route the user receives feedback almost instantenously in a fraction of a second. The tasks are sent to the celery worker queue and await processing.
![](https://github.com/danielc92/flask-celery-tests/blob/master/screenshots/Screen%20Shot%202019-03-28%20at%202.02.33%20pm.png)
### The timing of background tasks, celery is processing
Shows in a burst of ~2 seconds, 5 requests to the `/async` route being made. 30,000 * 5 records join the queue. After ~ 40 seconds 4 requests complete in the background.
![](https://github.com/danielc92/flask-celery-tests/blob/master/screenshots/Screen%20Shot%202019-03-28%20at%202.01.50%20pm.png)