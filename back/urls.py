"""
URL configuration for back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # OCR and Image Description
    
    path('describe_image/', views.DescribeImageView.as_view(), name='describe_image'),
    # ocr and image description both are optional
    path('extract_text_from_pdf/', views.ExtractTextFromPDFView.as_view(), name='extract_text_from_pdf'),
    # just image description
    path('extract_text_from_pptx/', views.PptxProcessorAPIView.as_view(), name='extract_text_from_pptx'),

    # History
    path('history/create/', views.create_history, name='create_history'),
    path('history/<str:user_id>/list/', views.get_history, name='get_history'),
    path('history/<int:pk>/', views.get_history_by_id, name='get_history_by_id'),
]
