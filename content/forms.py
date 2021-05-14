from django import forms


class RateForm(forms.Form):
    CHOICES = (
        ('useful', 'Полезно!'),
        ('want_more', 'Интересная статья, хочу больше таких!'),
        ('share', 'Поделюсь с друзьями!'),
        ('curious', 'Любопытно!')
    )
    rate = forms.ChoiceField(choices=CHOICES)
