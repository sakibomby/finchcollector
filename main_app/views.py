from django.shortcuts import render

finches = [
    {'name': 'Shorty', 'species': 'Black rosy finch', 'description': 'red feathers, black body', 'age': 0},
    {'name': 'Birdy', 'species': 'House finch', 'description': 'brown feathers, red head', 'age': 2},
    {'name': 'Cassie', 'species': 'Cassin''s finch', 'description': 'black feathers, white chest, red head', 'age': 3},
    {'name': 'Sam', 'species': 'American Goldfinch', 'description': 'black feathers and yellow chest', 'age': 4},
]
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })