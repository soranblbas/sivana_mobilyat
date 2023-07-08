# from importlib.resources import _

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html
# from importlib_resources._common import _

from .models import *


# Register your models here.

class SalesItem(admin.TabularInline):
    model = SaleItem
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "item":
            kwargs["queryset"] = Item.objects.exclude(price_list='شراء')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(SaleInvoice)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [SalesItem]

    class Meta:
        model = SaleInvoice

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        if request.method == 'POST':
            try:
                return super().changeform_view(request, object_id=object_id, form_url=form_url,
                                               extra_context=extra_context)
            except ValueError as error:
                self.message_user(request, _(str(error)), level='ERROR')
                url = reverse('admin:%s_%s_change' % (self.opts.app_label, self.opts.model_name), args=[object_id])
                return HttpResponseRedirect(url)
        else:
            return super().changeform_view(request, object_id=object_id, form_url=form_url, extra_context=extra_context)

    # def show_sales_total(self, obj):
    #     total_sales = sum(sale.total_amt for sale in obj.sales.all())
    #     return format_html('<b>{}</b>', total_sales)

    list_display = (
        'invoice_number', 'customer_name', 'total_sub_amount', 'total_discount_amount', 'total_sales_amount', 'date')
    list_filter = ('status',)
    search_fields = ('customer_name__customer_name',)


class PurchasesItem(admin.TabularInline):
    model = PurchaseItem
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "item":
            kwargs["queryset"] = Item.objects.exclude(price_list__in=['مفرد', 'جملة'])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Purchase)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [PurchasesItem]

    class Meta:
        model = Purchase

    list_display = ('invoice_number', 'vendor', 'total_purchase_amount', 'date')


@admin.register(Item)
class CustomerPagination(admin.ModelAdmin):
    list_display = ('name', 'price_list', 'price')
    # list_filter = ("client_name", "status", "date_created")
    # list_display_links = ('client_name',)
    # list_per_page = 20


# @admin.register(Purchase)
# class CustomerPagination(admin.ModelAdmin):
#     list_display = ('item', 'vendor', 'qty', 'price', 'total_amt', 'pur_date')
#     # list_filter = ("client_name", "status", "date_created")
#     # list_display_links = ('client_name',)
#     # list_per_page = 20
#     readonly_fields = ['total_amt', ]


# @admin.register(PurchaseItem)
# class CustomerPagination(admin.ModelAdmin):
#     list_display = ('item', 'qty', 'total_amt', 'pur_date')
#
#     readonly_fields = ['total_amt', ]

#
# @admin.register(SaleItem)
# class CustomerPagination(admin.ModelAdmin):
#     list_display = ('item', 'qty', 'total_amt', 'sale_date')
#
#     readonly_fields = ['total_amt', ]


@admin.register(Inventory)
class CustomerPagination(admin.ModelAdmin):
    list_display = ('item', 'purchase', 'sale', 'pur_qty', 'sale_qty', 'total_bal_qty')
    list_display_links = ['purchase', 'sale', ]


@admin.register(Payment_Entry)
class CustomerPagination(admin.ModelAdmin):
    raw_id_fields = ['sales_invoice']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "sales_invoice":
            kwargs["queryset"] = SaleInvoice.objects.select_related('customer_name')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        try:
            search_term_as_int = int(search_term)
            queryset |= self.model.objects.filter(sales_invoice_id=search_term_as_int)
        except ValueError:
            queryset |= self.model.objects.filter(sales_invoice__customer_name__customer_name__icontains=search_term)
        return queryset, use_distinct

    def sales_invoice_display(self, obj):
        if obj.sales_invoice:
            url = reverse("admin:mobilyat_saleinvoice_change", args=[obj.sales_invoice.pk])
            customer_name = obj.sales_invoice.customer_name.customer_name
            return format_html('<a href="{}">{}</a>', url, customer_name)
        return None

    sales_invoice_display.short_description = 'Sales Invoice'
    sales_invoice_display.admin_order_field = 'sales_invoice'

    list_display = ('invoice_number', 'sales_invoice_display', 'paid_amount', 'payment_date', 'note')
    search_fields = ['sales_invoice__customer_name__customer_name']

    # list_display = ('invoice_number', 'sales_invoice', 'paid_amount', 'payment_date', 'note',)
    # list_display_links = ['purchase', 'sale', ]


admin.site.register(JournalEntry)

admin.site.register(Vendor)
admin.site.register(Unit)

admin.site.register(Customer)
# admin.site.register(Price_List)
# admin.site.register(Payment_Entry)

admin.site.site_header = "Siavan Mobilyat Admin"
admin.site.site_title = "Siavan Mobilyat Admin Portal"
admin.site.index_title = "Welcome to Siavan Mobilyat Retailer Portal"
