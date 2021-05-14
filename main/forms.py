from django.forms import ModelForm
from .models import Member, Mailing


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        error_messages = {
            'name': {
                'max_length': 'Ваше ФИО такое длинное, что не похоже на настоящее',
            },
            'email': {
                'invalid': 'Введите существующую почту',
                'required': 'Почта нужна обязательно',
            },
            'message': {
                'max_length': 'Длина сообщения превышает максимальную',
            }
        }


class MailingForm(ModelForm):
    class Meta:
        model = Mailing
        fields = ['email']
        error_messages = {
            'email': {
                'invalid': 'Введите существующую почту',
                'required': 'Это обязательное поле',
            }
        }
