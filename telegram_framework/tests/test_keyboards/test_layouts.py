import unittest
from telegram_framework.keyboards import layouts


class TestLayouts(unittest.TestCase):

    def test_layout_defaults(self):
        layout = layouts.Layout()
        self.assertEqual(1, layout.columns_count)

    def test_default_layout(self):
        layout = layouts.default_layout()
        self.assertEqual(1, layout.columns_count)
