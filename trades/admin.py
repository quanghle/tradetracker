from django.contrib import admin
from .models import Trade, Ticker, Exchange

admin.site.register(Trade)
admin.site.register(Ticker)
admin.site.register(Exchange)