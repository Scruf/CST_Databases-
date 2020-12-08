from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

class Account(BaseModel):
    account_id: int
    frequency: str
    date: datetime

class Card(BaseModel):
    card_id: int
    disp_id: int
    card_type: str
    issued: datetime

class Client(BaseModel):
    client_id: int
    gender: str
    birth_date: datetime

class Disp(BaseModel):
    disp_id: int
    disp_type: str

class Loan(BaseModel):
    loan_id: int
    loan_date: datetime
    amount: int
    duration: int
    payments: Decimal
    loan_status: str

class Order(BaseModel):
    order_id: int
    bank_to: str
    account_to: int
    amount: Decimal
    k_symbol: str

class Transaction(BaseModel):
    trans_id: int
    transaction_date: datetime
    transaction_type: str
    operation: str
    amount: int
    balance: int
    k_symbol: str
    bank: str
    account: int
