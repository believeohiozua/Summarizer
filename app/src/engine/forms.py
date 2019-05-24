from django import forms
import datetime

#Multiple choice
LANGUAGE_CHOICE = [
    
    ('english', 'English'),
    ('chinese_(Simplified)', 'Chinese (Simplified)'),
    ('czech', 'Czech'),   
    ('french', 'French'),
	('german', 'German'),
    ('japanese', 'Japanese'),
	('portuguese', 'Portuguese'),
    ('slovak', 'Slovak'),
	('spanish', 'Spanish'),
    ]











class URLInput(forms.TextInput):
    input_type = 'url'


#entry for the web link    
class summary_form(forms.Form): 
    SUMMARIZE = forms.URLField(required = True, widget=URLInput(),  help_text = "", label='Enter a Valid Url:')
    LANGUAGE = forms.CharField(required = True, label='choose language', widget=forms.Select(choices=LANGUAGE_CHOICE))
    SENTENCES_COUNT = forms.IntegerField(required = True, min_value = 1, help_text = '',  label='sentence count',) 
    
    
"""   
class summary_form2(forms.Form): 
    SUMMARIZE2 =  forms.CharField(required = True, max_length=2000, help_text = "Enter text")
    LANGUAGE2 = forms.CharField(required = True, label='LANGUAGE', widget=forms.Select(choices=LANGUAGE_CHOICE))
    SENTENCES_COUNT2 = forms.IntegerField(required = True, help_text = '',  label='SENTENCES_COUNT',) 
	
 """       
   
    
    
    
    
    