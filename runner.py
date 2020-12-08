from random_data_generator import *
from random import randrange

accounts = []
for i in range(0, 10):
    account = AccountFactory().dict()
    account_id = account['account_id']
    account.update({
        'loans': [],
        'transactions': [],
        'orders': [],
        'disps': []
    })
    for loan_count in range(0, randrange(1, 4)):
        loan = LoanFactory().dict()
        loan.update({
            'account_id': account_id  
        })
        account['loans'].append(loan)
    for transaction_count in range(0, randrange(1, 4)):
        transaction = TransactionFactory().dict()
        transaction.update({
            'account_id': account_id
        })
        account['transactions'].append(transaction)
        
    for order_count in range(0, randrange(1, 4)):
        order = OrderFactory().dict()
        order.update({
            'account_id': account_id
        })
        account['orders'].append(order)

    for client_count in range(0,randrange(1, 5)):
        client = ClientFactory().dict()
        client_id = client['client_id']
        for disp_count in range(0, randrange(1, 10)):
            disp = DispFactory().dict()
            disp.update({'client_id': client_id,
                        'account_id': account_id})
            disp.update({
                'cards': []
            })
            for card in range(0,randrange(1, 3)):
                card = CardFactory().dict()
                card.update({
                    'disp_id': disp['disp_id']    
                })
                disp['cards'].append(card)
            account['disps'].append(disp)
    accounts.append(account)

account = accounts[0]
exclude_fields = {'loans', 'transactions', 'orders', 'disps'}

columns = []
values = []
from datetime import datetime
import csv
headers = []
for field in account:
    if field not in exclude_fields:
        columns.append(field)
        values.append(str(account[field]))
rows = dict(zip(columns, values))
with open('writer.csv', 'w') as w:
    w.write(",".join(columns)+"\n")
    w.write(",".join(values)+"\n")


        
