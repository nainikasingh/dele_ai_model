from services.data_loader import load_users, load_tasks
from services.role_access import get_user_role, filter_tasks_by_role
from services.llm_client import query_model

def generate_answer(user_id: str, question: str):
    users_df = load_users()
    tasks_df = load_tasks()
    
    role = get_user_role(user_id, users_df)
    if not role:
        return "Invalid user ID."

    relevant_tasks = filter_tasks_by_role(role, tasks_df, user_id)
    
    prompt = f"""
You are an assistant helping with team task performance.
The user role is: {role}.
They asked: "{question}"

Here is task data (trimmed for brevity):

{relevant_tasks[['taskTitle', 'taskDescription', 'priority']].head(10).to_string(index=False)}

Please respond clearly and concisely based on the task data and user role.
"""
    return query_model(prompt)
