import os
import sqlite3

db_filename='anime_database.db'
schema_filename='schema.sql'

db_is_new=not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creating the schema')
        with open(schema_filename, 'rt') as f:
            schema=f.read()
            conn.executescript(schema)

            print('Inserting initial data')

            conn.executescript('''
            INSERT INTO day (day)
            VALUES ('None');

            INSERT INTO day (day)
            VALUES ('Monday');

            INSERT INTO day (day)
            VALUES ('Tuesday');

            INSERT INTO day (day)
            VALUES ('Wednesday');

            INSERT INTO day (day)
            VALUES ('Thursday');

            INSERT INTO day (day)
            VALUES ('Friday');

            INSERT INTO day (day)
            VALUES ('Saturday');

            INSERT INTO day (day)
            VALUES ('Sunday');
            ''')
    else:
        print('Database exists, Schema should exist too')