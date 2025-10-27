from django import forms




    # pub_date = forms.DateTimeField(label="pub_date", widget=forms.DateTimeInput(attrs={'class':'datepicker'}))
    # question_text = forms.CharField(label="Your question text",max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # pub_date = forms.DateTimeField(label="pub_date", widget=forms.DateTimeInput(attrs={'class': 'form-control'}))

class QuestionForm(forms.Form):
    # with widget and Bootstrap classes
    # question_text = forms.CharField(label="Your question text",max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # pub_date = forms.DateTimeField(label='date published', widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))

    # original
    question_text = forms.CharField(label="Your question text",max_length=200)
    pub_date = forms.DateTimeField(label="pub_date", widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

