import pandas as pd


def calculate_special_bonus(data: pd.DataFrame) -> pd.DataFrame:
    Employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype(
        {'employee_id': 'int64', 'name': 'object', 'salary': 'int64'})

    Employees['bonus'] = Employees.apply(
        lambda row: row['salary'] if row['employee_id'] % 2 != 0 and not row['name'].startswith('M') else 0, axis=1)

    result = Employees[['employee_id', 'bonus']].sort_values(by='employee_id')
    d = pd.DataFrame(result)
    return d
