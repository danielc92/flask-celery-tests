# Flask / Celery / Redis Tests
Implementing celery in a flask application, so that users do not have to wait extended periods of time for transactions to complete.
Redis being used as backend broker, however can be subbed out for memcached, RabbitMQ.
Postgres being used as database, however can be subbed out for mysql, sqlserver, sqlite3 etc.
This repo is based on a `Mac OS` and `Python 3.6.5`.

# Before you get started
- Basic unstanding python 3
- Knowledge of Redis
- Knowledge of ORM and relational databases
- Knowledge of Flask

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

```sh
# Starting the web application
cd /location/of/cloned/repo
python3 application.py
```

```sh
# Starting the celery worker
```

```sh
# Starting the redis brew service
brew services restart redis

# Checking services in brew
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
![](https://github.com/danielc92/flask-celery-tests/blob/master/screenshots/Screen%20Shot%202019-03-28%20at%202.02.55%20pm.png)
### The timing of `/async` route (async)
![](https://github.com/danielc92/flask-celery-tests/blob/master/screenshots/Screen%20Shot%202019-03-28%20at%202.02.33%20pm.png)
### The timing of background tasks, celery is processing
![](https://github.com/danielc92/flask-celery-tests/blob/master/screenshots/Screen%20Shot%202019-03-28%20at%202.01.50%20pm.png)