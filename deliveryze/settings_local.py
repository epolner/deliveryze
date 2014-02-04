
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'delivsite',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '128.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

