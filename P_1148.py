import pandas as pd


def article_views(data: pd.DataFrame) -> pd.DataFrame:
    Views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype(
        {'article_id': 'Int64', 'author_id': 'Int64', 'viewer_id': 'Int64', 'view_date': 'datetime64[ns]'})
    self_joined = Views.merge(Views, left_on=['author_id', 'article_id'], right_on=[
                              'viewer_id', 'article_id'], how='inner')
    result = self_joined['author_id_x'].drop_duplicates(
    ).sort_values().rename('id')
    d = pd.DataFrame(result)
    return d
