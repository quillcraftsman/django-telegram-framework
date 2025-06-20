from django import forms
from django.core.exceptions import ValidationError


class LCharField(forms.CharField):

    def __init__(self, exception_text, *args, **kwargs):
        self.exception_text = exception_text
        super().__init__(*args, **kwargs)

    def clean(self, value):
        value = super().clean(value)
        if not value.startswith('Л'):
            raise ValidationError(self.exception_text)
        return value


class NameForm(forms.Form):
    first_name = LCharField(
        required=True,
        exception_text='Неверно введено имя, пожалуйста введите снова:',
        label='Как бы вас звали на букву "Л"?:',

    )
    last_name = LCharField(
        required=True,
        exception_text='Неверно введена фамилия, пожалуйста введите снова:',
        label='Какой бы была ваша фамилия на букву "Л"?:',
    )
