from django.urls import path
from bookstore import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home', views.home, name='home' ),
    path('AllBooks', views.AllBooks, name='AllBooks' ),
    path('<int:id>', views.book_details, name='bookstore.book_details'),
    path('<int:id>/delete', views.book_delete, name='bookstore.book_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)