from django.shortcuts import render, redirect, get_object_or_404
from .forms import Review_board_Form, Review_board_CommentForm
from django.utils import timezone
from .models import Review_board, Review_Comment
from django.db.models import Q


# Create your views here.
def review_read(request):
    review_board_queryset = Review_board.objects.all().order_by('-id')
    return render(request, 'review_read.html', {'review_board': review_board_queryset})

def review_create(request):
    if request.method == 'POST':
        form = Review_board_Form(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('review_read')
    else:
        form = Review_board_Form
        return render(request, 'review_create.html', {'form': form})
    
def review_detail(request, id):  
    review_board = get_object_or_404(Review_board, id = id)  
    if request.method == 'POST':
        form = Review_board_CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.review_board_id = review_board
            comment.save()
            return redirect('review_detail', id)
    else:
        form = Review_board_CommentForm
        return render(request, 'review_detail.html', {'form' : form,'review_board' : review_board})  

def review_update(request, id):
    review_board = get_object_or_404(Review_board, id = id)
    if request.method == 'POST':
        form = Review_board_Form(request.POST, instance=review_board)
        if form.is_valid():
            form = form.save(commit = False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('review_read')
    else:
        form = Review_board_Form(instance=review_board)
        return render(request, 'review_update.html', {'form' : form})
    
def review_delete(request, id):
    review_update = get_object_or_404(Review_board, id = id)
    review_update.delete()
    return redirect('review_read')

def review_comment_delete(request, id, c_id):
    comment = get_object_or_404(Review_Comment, id=c_id)
    comment.delete()
    return redirect('review_detail',id)

def review_comment_update(request, id, com_id):
    comment = Review_Comment.objects.get(id = com_id)
    form = Review_board_CommentForm(instance=comment)
    if request.method == "POST":
        form = Review_board_CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('review_detail', id)
    return render(request, 'review_comment_update.html', {'form':form})

def search(request):
    review_board = Review_board.objects.all().order_by('-id')
    
    q = request.POST.get('q', "")
    
    if q:
        review_board = review_board.filter(Q (title__icontains=q) | Q (body__icontains=q))
        return render(request, 'search.html', {'review_board':review_board, 'q':q})
    
    else:
        return render(request, 'search.html', {'review_board':review_board})