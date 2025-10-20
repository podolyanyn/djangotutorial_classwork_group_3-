from django import forms

class QuestionForm(forms.Form):
    question_text = forms.CharField(label="Your question text",max_length=200)
    pub_date = forms.DateTimeField(label="pub_date", widget=forms.DateTimeInput(attrs={'class':'datepicker'}))