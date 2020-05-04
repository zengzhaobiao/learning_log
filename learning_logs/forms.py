from django import forms

from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    #内嵌一个Meta类，告诉Django根据那个模型创建表单
    #以及在表单中包含哪些字段
    class Meta:
        #根据模型Topic创建一个表单，该表单只包含字段text
        model = Topic
        fields = ['text']
        #让Django不要为字段text生成标签
        labels = {'text' : ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        # 让Django不要为字段text生成标签
        labels = {'text': ''}
        widgets = {'text' : forms.Textarea(attrs={'cols':80})}
