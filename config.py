from secrets import get_secrets

secrets = get_secrets()

DB_HOST = secrets["DB_HOST"]
DB_USER = secrets["DB_USER"]
DB_PASSWORD = secrets["DB_PASSWORD"]
DB_NAME = secrets["DB_NAME"]
ENVIRONMENT = secrets["ENVIRONMENT"]
