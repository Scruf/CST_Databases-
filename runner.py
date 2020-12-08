from random_data_generator import *
from random import randrange

accounts = []
clients = []
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
        client.update({
            'disps': disp 
        })
        clients.append(client)
    accounts.append(account)

exclude_fields = {'loans', 'transactions', 'orders', 'disps'}
import pdb;pdb.set_trace()
columns = []
values = []
from datetime import datetime
child_dicts = {
        'loans': [],
        'transactions':[],
        'orders': []
}
headers = []
with open('account.csv', 'w') as writer:
    header = []
    for account in accounts:
        for field in account:
            if field not in exclude_fields:
                columns.append(field)
                values.append(str(account[field]))
            else:
                if field in child_dicts:
                    child_dicts[field].extend(account[field])
        if not header:
            header = columns
            writer.write(",".join(header)+"\n")
        writer.write(",".join(values)+"\n")
        values = []
for child in child_dicts:
    with open(f"{child}.csv", "w") as writer:
        is_header = False
        for data in child_dicts[child]:
            if not is_header:
                is_header = True
                writer.write(",".join(list(data.keys()))+"\n")
            writer.write(",".join(list(map(lambda x: str(x), list(data.values()))))+"\n")

with open('client.csv', 'w') as writer:
    is_client_header = False
    for client in clients:
        disps = client.pop('disps')
        if not is_client_header:
            writer.write(",".join(list(client.keys()))+"\n")
            is_client_header = True
        

        
