import factory
from factory import fuzzy
from faker import Faker
from models import *
from random import randrange, choice
from datetime import datetime, timezone

FREQUENCY_CHOICES= (
    (0, 'Weekly'),
    (1, 'Bi-Weekly'),
    (2, 'Semi-monthly'),
    (3, 'Monthly')
)

CARD_TYPES = (
    (0, 'Visa'),
    (1, 'American Express'),
    (2, 'Master Card')
)

GENDER = (
    (0, 'Female'),
    (1, 'Male'),
    (2, 'Not-Specified')
)

DISP_TYPE = (
    (0, 'Disp 1'),
    (1, 'Disp 2'),
    (2, 'Disp 3')
)

DURATION = (
    (0, 12),
    (1, 24),
    (2, 36),
    (3, 48)
)

PAYMENTS = (
    (0, 'PAYMENT'),
    (1, 'DEFERED'),
    (2, 'CANCELLED'),
    (3, 'PEND')
)

BANKS = (
    (0, 'Bofa'),
    (1, 'Amex'),
    (2, 'Chase'),
    (3, 'City')
)

class AccountFactory(factory.Factory):
    class Meta:
        model = Account

    account_id = factory.LazyAttribute(lambda x: randrange(1, 100))
    frequency = factory.LazyAttribute(lambda x: choice(FREQUENCY_CHOICES)[1])
    date = fuzzy.FuzzyDateTime(datetime(2019, 1, 1, tzinfo=timezone.utc))

class CardFactory(factory.Factory):
    class Meta:
        model = Card

    card_id = factory.LazyAttribute(lambda x: randrange(444444, 9999999))
    disp_id = factory.LazyAttribute(lambda x: randrange(1, 20))
    card_type = factory.LazyAttribute(lambda x: choice(CARD_TYPES)[1])

class ClientFactory(factory.Factory):
    class Meta:
        model = Client

    client_id = factory.LazyAttribute(lambda x: randrange(100, 3000))
    gender = factory.LazyAttribute(lambda x: choice(GENDER)[1])
    birth_date = fuzzy.FuzzyDateTime(datetime(1945, 1, 1, tzinfo=timezone.utc))

class DispFactory(factory.Factory):
    class Meta:
        model = Disp
    disp_type = factory.LazyAttribute(lambda x: choice(DISP_TYPE)[1])

class LoanFactory(factory.Factory):
    class Meta:
        model = Loan
    loan_id = factory.LazyAttribute(lambda x: randrange(1, 400))
    loan_date = fuzzy.FuzzyDateTime(datetime(2010, 1, 1, tzinfo=timezone.utc))
    amount = factory.LazyAttribute(lambda x: randrange(1, 10000))
    duration = factory.LazyAttribute(lambda x: choice(DURATION)[1])
    payments = fuzzy.FuzzyDecimal(1.0, 4000.0, 3)
    loan_status = factory.LazyAttribute(lambda x: choice(PAYMENTS)[1])

class OrderFactory(factory.Factory):
    class Meta:
        model = Order
    order_id = factory.LazyAttribute(lambda x: randrange(1, 10000))
    bank_to = factory.LazyAttribute(lambda x: choice(BANKS)[1])
    amount = fuzzy.FuzzyDecimal(100.0, 40000.0, 2)
