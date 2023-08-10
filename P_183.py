import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    never_ordered_customers = customers.merge(
        orders, left_on='id', right_on='customerId', how='left')
    never_ordered_customers = never_ordered_customers[never_ordered_customers['customerId'].isnull(
    )]
    result = never_ordered_customers[['name']].rename(
        columns={'name': 'Customers'})
    d = pd.DataFrame(result)
    return d
