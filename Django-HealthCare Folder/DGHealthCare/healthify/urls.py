from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('home/', views.HomeView, name='home'),
    path('admin/', views.AdminView, name='admin'),
    path('store/', views.storeView, name='store'),
    path('cart/', views.CartView, name='cart'),
    path('signup/', views.signupView, name='signup'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('addapp/', views.addAppointmentView, name='addapp'),
    path('addamb/', views.addAmbulanceView, name='addamb'),
    path('showapp/', views.showAppointmentView, name='showapp'),
    path('showamb/', views.showAmbulanceView, name='showamb'),
    path('deleteapp/<int:id>/', views.deleteAppointmentView, name='deleteapp'),
    path('deleteamb/<int:id>/', views.deleteAmbulanceView, name='deleteamb'),
    path('adddoct/', views.addDoctorView, name='adddoct'),
    path('addnur/', views.addNursingStaffView, name='addnur'),
    path('addrm/', views.addRoomServiceStaffView, name='addrm'),
    path('showdoct/', views.showDoctorView, name='showdoct'),
    path('shownur/', views.showNursingStaffView, name='shownur'),
    path('showrm/', views.showRoomServiceStaffView, name='showrm'),
    path('deletedoct/<int:id>/', views.deleteDoctorView, name='deletedoct'),
    path('deletenur/<int:id>/', views.deleteNursingStaffView, name='deletenur'),
    path('deleterm/<int:id>/', views.deleteRoomServiceStaffView, name='deleterm'),
    path('updatedoct/<int:id>/', views.updateDoctorView, name='updatedoct'),
    path('updatenur/<int:id>/', views.updateNursingStaffView, name='updatenur'),
    path('updaterm/<int:id>/', views.updateRoomServiceStaffView, name='updaterm'),
    path('addcr/', views.addCategoryView, name='addcr'),
    path('addpr/', views.addProductView, name='addpr'),
    path('showcr/', views.showCategoryView, name='showcr'),
    path('showpr/', views.showProductView, name='showpr'),
    path('deletecr/<int:id>/', views.deleteCategoryView, name='deletecr'),
    path('deletepr/<int:id>/', views.deleteProductView, name='deletepr'),
    path('updatepr/<int:id>/', views.updateProductView, name='updatepr'),
    path('display/', views.cart_display, name='cart_display'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('order/', views.customer_order, name='order'),


    #path('checkout_successful/',views.checkout_successful,name='checkout_successful'),
    #path('ho/', views.home, name='ho'),
    #path('success/' , views.success , name='success')

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="healthify/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="healthify/password_reset_sent.html"),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="healthify/password_reset_form.html"),
     name="password_reset_confirm"),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="healthify/password_reset_done.html"),
        name="password_reset_complete"),

]


