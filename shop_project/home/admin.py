from django.contrib import admin
from . models import categ,shop

# Register your models here.
class catadmin(admin.ModelAdmin):
    list_display =['name','slug']
    prepopulated_fields ={'slug':('name',)}  #data's in the name pass to slug
admin.site.register(categ, catadmin)


class shopadmin(admin.ModelAdmin):
    list_display =['name','slug','price','stock','img','available','cate']
    list_editable =['price','stock','available','img','cate']
    prepopulated_fields ={'slug':('name',)}
admin.site.register(shop, shopadmin)

