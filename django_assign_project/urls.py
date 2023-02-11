from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from read_excel.views import IapViewSet

router = routers.SimpleRouter()
router.register("Iap_sheet",IapViewSet)

urlpatterns = router.urls

urlpatterns += [

    path('admin/', admin.site.urls),
    path('api_auth/', include('read_excel.urls'))
]
