from django import forms

class EncodeForm(forms.Form):
    message = forms.CharField(
        label='Mesaj de ascuns',
        max_length=100,
        widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'Scrie un mesaj scurt...'})
    )

    DIFFICULTY_CHOICES = [
        ('easy', 'Ușor'),
        ('medium', 'Mediu'),
        ('hard', 'Greu'),
    ]

    difficulty = forms.ChoiceField(
        label='Dificultate Sudoku',
        choices=DIFFICULTY_CHOICES,
        widget=forms.Select()
    )
