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

class DecodeForm(forms.Form):
    grid_text = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 10, "cols": 40}),
        help_text="Pastează aici grila Sudoku (9 linii, 9 cifre separate prin spații)"
    )
    message_length = forms.IntegerField(
        min_value=1,
        help_text="Lungimea mesajului ascuns"
    )
