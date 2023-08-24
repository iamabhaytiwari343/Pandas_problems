import pandas as pd


def fix_names(Users: pd.DataFrame) -> pd.DataFrame:
    # Function to format names
    def format_name(name):
        return name.capitalize()

    # Apply the formatting function to the 'name' column
    Users['name'] = Users['name'].apply(format_name)

    # Sort the DataFrame by user_id
    Users = Users.sort_values(by='user_id')

    return Users
