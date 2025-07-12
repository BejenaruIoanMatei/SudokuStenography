from django.shortcuts import render
from .forms import EncodeForm, DecodeForm
from .generator import generate_sudoku
from .generator import encode_message_in_sudoku
from .decoder import decode_message_from_sudoku

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
            
            max_message_len = sum(1 for row in sudoku_grid for val in row if val != 0) // 8
            
            if len(message) > max_message_len:
                form.add_error('message', f'Mesajul este prea lung. Max {max_message_len} caractere pentru această grilă.')
                return render(request, 'sudoku/encode.html', {'form': form})
            
            sudoku_encoded = encode_message_in_sudoku(sudoku_grid, message)
            
            
            decoded = decode_message_from_sudoku(sudoku_grid, len(message))
            print(f'DEBUG - {decoded}')

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

def parse_grid_text(text):
    lines = text.strip().split('\n')
    grid = []
    for line in lines:
        numbers = list(map(int, line.strip().split()))
        grid.append(numbers)
    return grid

def decode_view(request):
    if request.method == 'POST':
        form = DecodeForm(request.POST)
        if form.is_valid():
            grid_text = form.cleaned_data['grid_text']
            msg_length = form.cleaned_data['message_length']

            try:
                grid = parse_grid_text(grid_text)
                message = decode_message_from_sudoku(grid, msg_length)
                return render(request, 'sudoku/decode_result.html', {
                    'form': form,
                    'message': message,
                })
            except Exception as e:
                form.add_error('grid_text', f"Format invalid: {e}")
    else:
        form = DecodeForm()

    return render(request, 'sudoku/decode.html', {'form': form})
