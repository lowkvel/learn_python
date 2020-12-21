from  django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea管理后台'
    index_title = '首页'

custom_admin_site = CustomAdminSite(name='cus_admin')

