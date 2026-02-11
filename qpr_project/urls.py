from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from qpr_app.views import (
    api_records, api_record_detail, request_edit_api, login_view, register_view, logout_view,
    user_profile, user_dashboard, user_office_form, change_password,
    hod_dashboard, hod_detail_list, hod_manager_requests,
    admin_dashboard, admin_approve_request, admin_employee_list, admin_create_hod, api_update_hod
)

urlpatterns = [
    path('', login_required(TemplateView.as_view(template_name='index.html'), login_url='login_view'), name='home'),
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('logout/', logout_view, name='logout_view'),
    
    # User routes
    path('profile/', user_profile, name='user_profile'),
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('office/', user_office_form, name='user_office_form'),
    path('change-password/', change_password, name='change_password'),
    
    # HOD routes
    path('hod/dashboard/', hod_dashboard, name='hod_dashboard'),
    path('hod/detail-list/', hod_detail_list, name='hod_detail_list'),
    path('hod/manager-requests/', hod_manager_requests, name='hod_manager_requests'),
    
    # Admin/Manager routes - MUST come before generic /admin/
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin-approve-request/<int:request_id>/', admin_approve_request, name='admin_approve_request'),
    path('admin-employee-list/', admin_employee_list, name='admin_employee_list'),
    path('admin-create-hod/', admin_create_hod, name='admin_create_hod'),
    
    # Django admin - keep at the end to avoid conflicts
    path('admin/', admin.site.urls),
    
    # API routes
    path('api/records', api_records),
    path('api/records/<int:record_id>/', api_record_detail),
    path('api/request-edit/', request_edit_api, name='request_edit_api'),
    path('api/update-hod/', api_update_hod, name='api_update_hod'),

    # Report list and detail pages
    path('reports/', login_required(TemplateView.as_view(template_name='report_list.html'), login_url='login_view'), name='reports'),
    path('reports/<int:record_id>/', login_required(TemplateView.as_view(template_name='report_detail.html'), login_url='login_view'), name='report_detail'),
]