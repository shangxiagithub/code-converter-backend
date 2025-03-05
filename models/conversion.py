from datetime import datetime
import mysql.connector


class ConversionDAO:
    def __init__(self, config):
        self.config = config

    def _get_connection(self):
        return mysql.connector.connect(
            host=self.config['MYSQL_HOST'],
            user=self.config['MYSQL_USER'],
            password=self.config['MYSQL_PASSWORD'],
            database=self.config['MYSQL_DB']
        )

    def create_record(self, source_code: str, detected_lang: str,
                      target_lang: str, converted_code: str):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO conversions 
                (source_code, detected_lang, target_lang, converted_code, conversion_date)
                VALUES (%s, %s, %s, %s, %s)
            ''', (source_code, detected_lang, target_lang,
                  converted_code, datetime.now()))
            conn.commit()

    def get_history(self):
        with self._get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute('''
                SELECT * FROM conversions 
                ORDER BY conversion_date DESC
            ''')
            return cursor.fetchall()
