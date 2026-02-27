import pandas as pd

def read_patients_excel(path: str):
    df = pd.read_excel(path)
    df.columns = df.columns.str.strip().str.lower()
    return df

def read_doctors_excel(path: str):
    df = pd.read_excel(path)
    df.columns = df.columns.str.strip().str.lower()
    return df
