def get_user_role(user_id, users_df):
    user = users_df[users_df["_id"] == user_id]
    return user.iloc[0]["role"] if not user.empty else None

def filter_tasks_by_role(role, tasks_df, user_id):
    if role == "boss":
        return tasks_df
    elif role == "delegator":
        return tasks_df[tasks_df["delegatorName"] == user_id]
    elif role == "delegatee":
        return tasks_df[
            (tasks_df["delegateeName[0]"] == user_id) |
            (tasks_df["delegateeName[1]"] == user_id) |
            (tasks_df["delegateeName[2]"] == user_id)
        ]
    return tasks_df.iloc[0:0]  # empty
