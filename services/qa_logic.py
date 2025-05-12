def generate_answer(user_id: str, question: str):
    users_df = load_users()
    tasks_df = load_tasks()

    role = get_user_role(user_id, users_df)
    if not role:
        return "Invalid user ID."

    relevant_tasks = filter_tasks_by_role(role, tasks_df, user_id)

    task_snippet = relevant_tasks[['taskTitle', 'taskDescription', 'priority']].head(5).to_string(index=False)

    prompt = (
        f"You are an AI assistant helping a user with the role '{role}' analyze task data.\n"
        f"The user has asked: '{question}'\n\n"
        f"Here are some recent tasks:\n{task_snippet}\n\n"
        f"Based on the user's role and question, provide a helpful and specific answer."
    )

    result = generator(prompt, max_new_tokens=256)[0]["generated_text"]
    return result.strip()
