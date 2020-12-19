from django.db import models

class TradeAction(models.TextChoices):
    BUY = 'B', 'Buy'
    SELL = 'S', 'Sell'

class TradeClass(models.TextChoices):
    STOCK = 'ST', 'Stock'
    OPTION = 'OP', 'Option'

class Trade(models.Model):

    ticker = models.ForeignKey('Ticker', on_delete=models.DO_NOTHING)
    action = models.CharField(max_length=1, choices=TradeAction.choices)
    trade_class = models.CharField(max_length=2, choices=TradeClass.choices)
    quantity = models.DecimalField(max_digits=30, decimal_places=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    exchange = models.ForeignKey('Exchange', on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'trade'
        ordering = ['created_date', 'last_modified_date', 'ticker']
        constraints = [
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_action_valid',
                check=models.Q(action__in=TradeAction.values),
            ),
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_trade_class_valid',
                check=models.Q(trade_class__in=TradeClass.values),
            )
        ]

    def __str__(self) -> str:
        return f'{self.ticker} | {self.action} | {self.trade_class} | {self.quantity} | {self.price} | {self.exchange} | {self.created_date} | {self.last_modified_date}'

class Ticker(models.Model):

    symbol = models.CharField(max_length=6, db_index=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ticker'
        ordering = ['symbol']
    
    def __str__(self) -> str:
        return self.symbol

class Exchange(models.Model):

    name = models.CharField(max_length=50, db_index=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'exchange'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name
