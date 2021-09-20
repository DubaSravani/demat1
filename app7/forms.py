from django import forms

some_choices=[
("dosa","dosa"),
("idly","idly")
]
gender=[
("Male","male"),
("Female","female"),
("Other","other")
]
class supermarket(forms.Form):
    name=forms.CharField(max_length=100)
    text=forms.CharField(initial="sravani",widget=forms.Textarea(attrs={"rows":4,"cols":10}))
    roll=forms.IntegerField()
    present=forms.BooleanField()
    email=forms.EmailField(required=False)
    food_menu=forms.CharField(widget=forms.Select(choices=some_choices))
    gender=forms.CharField(label="GENDER",widget=forms.RadioSelect(choices=gender))
