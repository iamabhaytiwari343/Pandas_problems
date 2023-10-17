import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    r=players.shape
    return [r[0],r[1]]