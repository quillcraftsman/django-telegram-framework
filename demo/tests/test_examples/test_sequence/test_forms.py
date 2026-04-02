from pytest import raises
from django.core.exceptions import ValidationError
from demo.examples.sequence.forms import NameForm, LCharField


def test_one_field_validation():
    """
    Test: how we can validate form fields one by one
    """
    form = NameForm()

    first_name = 'Василий'

    with raises(ValidationError):
        NameForm.base_fields['first_name'].clean(first_name)

    field = LCharField(exception_text='Любой текст')
    with raises(ValidationError):
        field.clean(first_name)

    first_name = 'Лео'
    form.fields['first_name'].clean(first_name)
    last_name = 'Васёв'
    with raises(ValidationError):
        form.fields['last_name'].clean(last_name)
    last_name = 'Леонов'
    form.fields['last_name'].clean(last_name)
    data = {
        'first_name': first_name,
        'last_name': last_name,
    }
    form = NameForm(data=data)
    is_valid = form.is_valid()
    assert is_valid
