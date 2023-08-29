import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(
        department, left_on='departmentId', right_on='id', how='inner')
    max_salaries = merged.groupby('name_y')['salary'].transform('max')
    highest_salary = merged[merged['salary'] ==
                            max_salaries][['name_y', 'name_x', 'salary']]
    highest_salary.columns = ['department', 'employee', 'salary']
    return highest_salary
