from django.contrib import admin
from django.urls import path
from recipe.views import main, recipeDetail, categoryList, categoryDetail
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="main"),
    path('recipeDetail/', recipeDetail, name="recipeDetail"),
    path('categoryList/', categoryList, name="categoryList"),
    path('categoryDetail/', categoryDetail, name="categoryDetail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)