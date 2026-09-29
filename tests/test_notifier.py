import unittest
from unittest.mock import patch, MagicMock
from notifier import AegisNotifier

class TestAegisNotifier(unittest.TestCase):
    def setUp(self):
        self.notifier = AegisNotifier()

    def test_default_unconfigured_behavior(self):
        self.assertFalse(self.notifier.is_configured)
        result = self.notifier.send_alert("dummy/path.jpg", "SMOKING_INCIDENT", "Cigarette")
        self.assertFalse(result)

    @patch('smtplib.SMTP_SSL')
    def test_configured_send_alert(self, mock_smtp):
        self.notifier.is_configured = True
        self.notifier.sender_email = "test@example.com"
        self.notifier.app_password = "password123"

        mock_server = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server

        result = self.notifier.send_alert("non_existent_file.jpg", "SMOKING_INCIDENT", "Cigarette")
        self.assertTrue(result)
        mock_server.login.assert_called_once_with("test@example.com", "password123")
        mock_server.sendmail.assert_called_once()

if __name__ == '__main__':
    unittest.main()
