import pandas as pd

USERS_CSV = "data/delegation.users.csv"
TASKS_CSV = "data/delegation.tasks1.csv"

def load_users():
    return pd.read_csv(USERS_CSV)

def load_tasks():
    return pd.read_csv(TASKS_CSV)
