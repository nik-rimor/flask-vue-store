# services/webapp/project/tests/test_items.py


import json
import unittest

from project.tests.base import BaseTestCase


class TestItemResource(BaseTestCase):
    """Tests the Items resource endpoint."""

    def test_items(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/items/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()

