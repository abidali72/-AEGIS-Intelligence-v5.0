import unittest
import os
import sqlite3
import tempfile
from database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.temp_db_fd, self.temp_db_path = tempfile.mkstemp(suffix=".db")
        os.close(self.temp_db_fd)
        self.db = Database(db_path=self.temp_db_path)

    def tearDown(self):
        if os.path.exists(self.temp_db_path):
            os.remove(self.temp_db_path)

    def test_init_db(self):
        conn = sqlite3.connect(self.temp_db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='events'")
        table = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(table)

    def test_log_event_and_get_history(self):
        timestamp = self.db.log_event("archives/test.jpg", "SMOKING_INCIDENT", "Cigarette", 0.95)
        self.assertIsNotNone(timestamp)

        history = self.db.get_history(limit=5)
        self.assertEqual(len(history), 1)
        # Event fields: id, timestamp, image_path, event_type, product_name, confidence
        row = history[0]
        self.assertEqual(row[2], "archives/test.jpg")
        self.assertEqual(row[3], "SMOKING_INCIDENT")
        self.assertEqual(row[4], "Cigarette")
        self.assertAlmostEqual(row[5], 0.95)

if __name__ == '__main__':
    unittest.main()
