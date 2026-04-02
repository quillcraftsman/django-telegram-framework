from telegram_framework.keyboards import layouts


def test_layout_defaults():
    layout = layouts.Layout()
    assert 1 == layout.columns_count


def test_default_layout():
    layout = layouts.default_layout()
    assert 1 == layout.columns_count
