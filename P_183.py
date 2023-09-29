import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    c = customers.merge(orders, left_on='id',
                        right_on='customerId', how='left')
    c = c[c['id_y'].isnull()]
    c = pd.DataFrame(c['name'])
    c = c.rename(columns={'name': 'customers'})
    return c
