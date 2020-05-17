from django.contrib import admin
from django.urls import path
import user.views
import PNR.views
urlpatterns = [
    path('', user.views.login, name = 'login'),
    path('login_auth',PNR.views.login_auth,name = 'loginauth'),
    path('admin/', admin.site.urls),
    path('dash/',PNR.views.redirect_to_dash, name = 'dashboard'),
    path('GoAirVerify/',PNR.views.goair_landing,name = 'goair_land'),
    path('IndigoVerify/',PNR.views.indigo_landing,name = 'indigo_land'),
    path('VerifyIndigo',PNR.views.indigo_verify,name = 'indigo_verify'),
    path('VerifyGoAir',PNR.views.goair_verify,name = 'goair_verify'),

]
