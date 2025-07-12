from django.shortcuts import render
from .forms import EncodeForm
from .generator import generate_sudoku
from .generator import encode_message_in_sudoku

DIFFICULTY_MAP = {
    'easy': 30,
    'medium': 40,
    'hard': 50,
}

def encode_view(request):
    if request.method == 'POST':
        form = EncodeForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            difficulty = form.cleaned_data['difficulty']
            empty_cells = DIFFICULTY_MAP.get(difficulty, 40)
            sudoku_grid = generate_sudoku(empty_cells=empty_cells)
            sudoku_encoded = encode_message_in_sudoku(sudoku_grid, message)

            context = {
                'form': form,
                'sudoku': sudoku_encoded,
                'message': message,
                'difficulty': difficulty,
            }
            return render(request, 'sudoku/encode_result.html', context)
    else:
        form = EncodeForm()

    return render(request, 'sudoku/encode.html', {'form': form})
