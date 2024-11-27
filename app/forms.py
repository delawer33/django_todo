from django.forms import ModelForm
from .models import TodoItem

class TodoForm(ModelForm):

    class Meta:
        model = TodoItem
        fields = ('title', 'text',)

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['text'].required = False
