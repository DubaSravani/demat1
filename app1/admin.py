from django.contrib import admin
from.models import Post,Book #,employee,salary
class Bookadmin(admin.ModelAdmin):
    fields=['book_name','author_name','comments','created_date','student_updated','new_content','email','profile_pic','resume','address','rating']
    readonly_fields=['created_date','student_updated','new_content']
    def new_content(self,obj,*args,**kwargs):
        return str(obj.book_name)
    class Meta:
        model=Book
admin.site.register(Post)
admin.site.register(Book,Bookadmin)
#admin.site.register(employee)
#admin.site.register(salary)
