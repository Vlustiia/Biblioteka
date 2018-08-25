from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(
        help_text="Введите дату между сегодняшним днем "
                  "и 4 неделями (по-умолчанию 3 недели)")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Проверка того, что дата не выходит за нижнюю границу (не в прошлом)
        if data < datetime.date.today():
            raise ValidationError(_('Неправильная дата - меньше настоящего момента'))

        # проверка того, что дата не выходит за верхнюю границу (+4 недели)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Неправильная дата (больше 4 недель)'))

        # Возвращаем очищенные данные
        return data


