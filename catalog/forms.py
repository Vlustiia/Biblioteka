from django import forms
from django.forms import ModelForm

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from catalog.models import BookInstance

import datetime


class RenewBookForm(forms.Form):
    """
    Форма, которая не привязана к модели
    """
    renewal_date = forms.DateField(
        help_text="Введите дату между сегодняшним днем "
                  "и 4 неделями (по-умолчанию 3 недели)")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Проверка того, что дата не выходит за нижнюю границу (не в прошлом)
        if data < datetime.date.today():
            raise ValidationError(_('Неправильная дата - '
                                    'меньше настоящего момента'))

        # проверка того, что дата не выходит за верхнюю границу (+4 недели)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Неправильная дата (больше 4 недель)'))

        # Возвращаем очищенные данные
        return data


# Альтернативная реализация формы обновления даты возравта книги
class RenewBookModelForm(ModelForm):
    """
    Форма, которая наследуется от ModelForm и привязана к модели BookInstance
    """
    def clean_due_back(self):
        data = self.cleaned_data['due_back']

        # Проверка того, что дата не выходит за нижнюю границу (не в прошлом)
        if data < datetime.date.today():
            raise ValidationError(_('Неправильная дата - '
                                    'меньше настоящего момента'))

        # проверка того, что дата не выходит за верхнюю границу (+4 недели)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Неправильная дата (больше 4 недель)'))

        # Возвращаем очищенные данные
        return data


    class Meta:
        model = BookInstance
        fields = ['due_back']
        labels = {'due_back': _('Обновление даты')}
        help_texts = {'due_back': _('Введите дату между сегодняшним днем '
                  'и 4 неделями (по-умолчанию 3 недели)')}