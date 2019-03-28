# Project Title
Implementing celery in a flask application, so that users do not have to wait extended periods of time for transactions to complete. Redis will be used as a backend broker, postgres and flask-sqlalchemy (sqlalchemy) will be used as a database for this example.

# Before you get started


# Setup
**How to obtain this repository:**
```sh
git clone https//link.to.this.projects.git-repo
```


**Redis on Mac**
```sh
# Installation
brew install redis

# Restarting service
brew service restart redis
```

**Installation of RabbitMQ**
```sh
brew update
brew install rabbitmq
nano ~/.bash_profile
# Add /usr/local/sbin/ and /usr/local/Cellar/rabbitmq/{VERSION}/sbin/ to PATH and export PATH. Save bash profile and reload terminal.
# Note: cd into /usr/local/Cellar/rabbitmq to check for the correct version.
```

** Starting and stopping Rabbitmq server
```sh
# Start server
rabbitmq-server

# Stop server
# Control + C in terminal

# Visit dashboard in browser
http://localhost:15672
# The default user **and** password is 'guest'
```


**Modules/dependencies Python3:**
- `celery`
- `flask-celery`
- `flask`

Install the following dependences:
```sh
pip install flask celery flask-celery
```

# Tests
- Installation of RabbitMQ. Tested login successfully into dashboard.


# Contributors
- Daniel Corcoran

# Sources
- [Installing RabbitMQ on Mac](https://www.dyclassroom.com/howto-mac/how-to-install-rabbitmq-on-mac-using-homebrew)
- [Flask, Celery & SQLAlchemy Example by PrettyPrinted](https://www.youtube.com/watch?v=lOirTBrOek0)
# Screenshots
