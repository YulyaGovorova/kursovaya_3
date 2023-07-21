import os
from operator import itemgetter
from utils import get_operations, filter_by_state, templ_operation


OPERATION_DIR = os.path.abspath(os.path.dirname(__file__))
data_file = os.path.join(OPERATION_DIR, 'operations.json')

user_operations = get_operations(data_file)

user_exec = filter_by_state(user_operations, 'EXECUTED')


for i in sorted(user_exec, key=itemgetter('date'), reverse=True)[:5]:
    data, descr, source, destin, amount, currency = templ_operation(i)
    print(data, descr)
    print(source, '->', destin) if source else print(destin)
    print(amount, currency, "\n")