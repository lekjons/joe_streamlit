import streamlit as st
from task import Task

# task_list = [Task("Buy milk"), Task("Walk the dog")]
# task_list=[]
if "task_list" not in st.session_state:
    st.session_state.task_list = []

task_list = st.session_state.task_list

def add_task(task_name: str):
    task_list.append(Task(task_name))

def mark_done(task: Task):
    task.is_done = True

def mark_not_done(task: Task):
    task.is_done = False

def delete_task(idx: int):
    del task_list[idx]
# for task in task_list:
#     st.checkbox(task.name, task.is_done)

# for task in task_list:
#     task_col, delete_col = st.columns([0.8, 0.2])
#     task_col.checkbox(task.name, task.is_done)
#     if delete_col.button("Delete"):
#         pass

with st.sidebar:
    task = st.text_input("Enter a task")
    if st.button("Add task", type="primary"):
        add_task(task)

total_tasks = len(task_list)
completed_tasks = sum(1 for task in task_list if task.is_done)
metric_display = f"{completed_tasks}/{total_tasks} done"
st.metric("Task completion", metric_display, delta=None)

st.header("Today's to-dos:", divider=True)
# st.info(f"task_list: {task_list}")
for idx, task in enumerate(task_list):
    task_col, delete_col = st.columns([0.8, 0.2])
    # task_col.checkbox(task.name, task.is_done)
    # task_col.checkbox(task.name, task.is_done, key=f"task_{idx}")
    label = f"~~{task.name}~~" if task.is_done else task.name    
    # 将复选框的值保存到一个新的名为 checked 的变量中，以提高可读性。
    checked = task_col.checkbox(label, task.is_done, key=f"task_{idx}")    
    # 只有在复选框被选中并且任务尚未标记为完成时才调用 mark_done。
    if checked and not task.is_done:    
        mark_done(task)
        st.rerun()
    #只有在复选框未选中且任务仍被标记为已完成时才调用 mark_not_done。 
    elif not checked and task.is_done:  
        mark_not_done(task)
        st.rerun()
    if delete_col.button("Delete", key=f"delete_{idx}"):
        delete_task(idx)
        st.rerun()


