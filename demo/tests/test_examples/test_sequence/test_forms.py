from unittest import TestCase
from django.core.exceptions import ValidationError
from demo.examples.sequence.forms import NameForm, LCharField


class TestNameForm(TestCase):

    def test_one_field_validation(self):
        """
        Test: how we can validate form fields one by one
        """
        form = NameForm()

        first_name = 'Вася'

        with self.assertRaises(ValidationError):
            NameForm.base_fields['first_name'].clean(first_name)

        field = LCharField(exception_text='Любой текст')
        with self.assertRaises(ValidationError):
            field.clean('Вася')

        first_name = 'Лео'
        form.fields['first_name'].clean(first_name)
        last_name = 'Васёв'
        with self.assertRaises(ValidationError):
            form.fields['last_name'].clean(last_name)
        last_name = 'Леонов'
        form.fields['last_name'].clean(last_name)
        data = {
            'first_name': first_name,
            'last_name': last_name,
        }
        form = NameForm(data=data)
        is_valid = form.is_valid()
        self.assertTrue(is_valid)
