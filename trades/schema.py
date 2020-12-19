import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from trades.models import Trade, Ticker, Exchange, TradeAction, TradeClass

class TradeType(DjangoObjectType):
    class Meta:
        model = Trade
    
    action = graphene.String()

    trade_class = graphene.String()

    def resolve_action(self, info):
        return TradeAction(self.action).label
    
    def resolve_trade_class(self, info):
        return TradeClass(self.trade_class).label

class TickerType(DjangoObjectType):
    class Meta:
        model = Ticker

class ExchangeType(DjangoObjectType):
    class Meta:
        model = Exchange

class Query(ObjectType):
    trade = graphene.Field(TradeType, id=graphene.Int())
    ticker = graphene.Field(TickerType, id=graphene.Int())
    exchange = graphene.Field(ExchangeType, id=graphene.Int())
    trades = graphene.List(TradeType)
    tickers = graphene.List(TickerType)
    exchanges = graphene.List(ExchangeType)
    trades_by_ticker = graphene.List(TradeType, symbol=graphene.String())

    def resolve_trade(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Trade.objects.get(pk=id)

        return None
    
    def resolve_trades_by_ticker(self, info, **kwargs):
        symbol = kwargs.get('symbol')

        if symbol is not None:
            return Trade.objects.filter(ticker__symbol=symbol)
        
        return None

    def resolve_ticker(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Ticker.objects.get(pk=id)

        return None

    def resolve_exchange(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Exchange.objects.get(pk=id)

        return None

    def resolve_trades(self, info, **kwargs):
        return Trade.objects.all()

    def resolve_tickers(self, info, **kwargs):
        return Ticker.objects.all()

    def resolve_exchanges(self, info, **kwargs):
        return Exchange.objects.all()

class TickerInput(graphene.InputObjectType):
    id = graphene.ID()
    symbol = graphene.String()

class ExchangeInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()

class TradeInput(graphene.InputObjectType):
    id = graphene.ID()
    ticker = graphene.Field(TickerInput)
    action = graphene.String()
    trade_class = graphene.String()
    quantity = graphene.Float()
    price = graphene.Float()
    exchange = graphene.Field(ExchangeInput)

class CreateTrade(graphene.Mutation):
    class Arguments:
        input = TradeInput(required=True)

    ok = graphene.Boolean()
    trade = graphene.Field(TradeType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True

        ticker, _ = Ticker.objects.get_or_create(symbol=input.ticker.symbol)

        exchange, _ = Exchange.objects.get_or_create(name=input.exchange.name)
        
        trade_instance = Trade(
            ticker=ticker,
            action=input.action,
            trade_class=input.trade_class,
            quantity=input.quantity,
            price=input.price,
            exchange=exchange
        )
        trade_instance.save()
        
        return CreateTrade(ok=ok, trade=trade_instance)

class CreateTicker(graphene.Mutation):
    class Arguments:
        input = TickerInput(required=True)

    ok = graphene.Boolean()
    ticker = graphene.Field(TickerType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        ticker_instance = Ticker(symbol=input.symbol)
        ticker_instance.save()

        return CreateTicker(ok=ok, ticker=ticker_instance)
        
class CreateExchange(graphene.Mutation):
    class Arguments:
        input = ExchangeInput(required=True)

    ok = graphene.Boolean()
    exchange = graphene.Field(ExchangeType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        exchange_instance = Exchange(name=input.name)
        exchange_instance.save()

        return CreateExchange(ok=ok, exchange=exchange_instance)

class Mutation(graphene.ObjectType):
    create_trade = CreateTrade.Field()
    create_ticker = CreateTicker.Field()
    create_exchange = CreateExchange.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)