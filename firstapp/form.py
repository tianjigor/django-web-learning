from django import forms
from django.core.exceptions import ValidationError

def words_validator(comment):
    if len(comment) < 4:
        raise ValidationError('Not enough words')

def comment_validator(comment):
    if 'love' in comment:
        raise ValidationError('Do not use that word!')

class CommentForms(forms.Form):
    print 'CommentForms'
    name = forms.CharField(max_length=50)
    comment = forms.CharField(
        widget=forms.Textarea(),
        error_messages={
            'required':'wow,such words'
            },
        validators=[words_validator, comment_validator]
        )
