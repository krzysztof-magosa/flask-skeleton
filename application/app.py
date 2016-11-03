from flask import Flask

app = Flask(__name__)
app.config.from_envvar('APPLICATION_COMMON_CONF')
app.config.from_envvar('APPLICATION_ENV_CONF', silent=True)
