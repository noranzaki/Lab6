from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from bookstore.models import Book
# Create your views here.

books = [
    {"id":1 , "name": "Real Love", "image":"pic1.png", "author": "Sharon Salzberg", "price": "5$", "numpages": "660 pages"},
    {"id":2 , "name": "A Return To Love", "image":"pic2.png", "author": "Marianne Williamson", "price": "4$", "numpages": "640 pages"},
    {"id":3 , "name": "The Secret To Love, Health, And Money", "image":"pic3.png", "author": "Rhonda Byne", "price": "7$", "numpages": "900 pages"},
]


def home(request):
    return render(request, 'bookstore/index.html')

def AllBooks(request):
    # books=Book.objects.all()
    # return render(request,'bookstore/books.html',context={"books": books})
    return render(request, 'bookstore/books.html',context={"books": books})

# def book_details(request , id ):
#     filtered_books = filter(lambda book: book["id"] == id, books)
#     filtered_books = list(filtered_books)
#     if filtered_books:
#         return render(request,
#                       'bookstore/book_details.html',
#                       context= {"book":filtered_books[0]})
#     return HttpResponse("Book not found")

def book_details(request,id):
    book=Book.objects.get(id=id)
    return render(request,'bookstore/book_details.html',context={"book":book})


def edit_book(request, id):
    if request.method == 'POST':
        print(request.FILES)
        print(request.POST)
        name = request.POST["name"]
        author = request.POST["author"]
        price = request.POST['price']
        numpages = request.POST['numpages']
        book = Book()
        book.name = name
        book.author = author
        book.price = price
        book.numpages = numpages
        book.image = request.FILES['image']
        book.save()

        url = reverse("AllBooks")
        return redirect(url)

    return render(request, 'bookstore/book_edit.html')

def book_delete(request, id):
    book= Book.objects.get(id=id)
    book.delete()
    url = reverse("AllBooks")
    return redirect(url)