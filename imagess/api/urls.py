from django.urls import path
from imagess.api import views

urlpatterns = [
    path("upload/", views.UploadFileAPIView.as_view(), name="upload_image"),
    path("", views.ImageAllFilesAPIView.as_view(), name="list_images"),
    path("download/<int:image_id>/", views.download_file, name="image_download"),
    path("display/<int:image_id>/", views.display_image, name="image_display"),
    path("<int:image_id>/", views.delete_file, name="image_delete"),
]