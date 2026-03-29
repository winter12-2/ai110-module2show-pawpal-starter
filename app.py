import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+ Pet Care Planner")

# -------------------------
# Session State
# -------------------------
if "owner" not in st.session_state:
    st.session_state.owner = None

if "pet" not in st.session_state:
    st.session_state.pet = None

if "tasks" not in st.session_state:
    st.session_state.tasks = []


# -------------------------
# Owner Input
# -------------------------
st.header("Owner Information")

owner_name = st.text_input("Owner name")
available_time = st.number_input("Available Time (minutes)", min_value=0, value=60)
preferences = st.text_input("Preferences")

if st.button("Save Owner"):
    st.session_state.owner = Owner(owner_name, available_time, preferences)
    st.success("Owner saved!")


# -------------------------
# Pet Input
# -------------------------
st.header("Pet Information")

pet_name = st.text_input("Pet name")
species = st.selectbox("Species", ["dog", "cat", "other"])
pet_age = st.number_input("Pet Age", min_value=0, value=1)

if st.button("Save Pet"):
    if st.session_state.owner:
        st.session_state.pet = Pet(pet_name, species, pet_age, st.session_state.owner)
        st.success("Pet saved!")
    else:
        st.error("Please create an owner first.")


# -------------------------
# Task Input
# -------------------------
st.header("Add Tasks")

task_title = st.text_input("Task title")
duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
priority_label = st.selectbox("Priority", ["low", "medium", "high"])

# Convert priority to number
priority_map = {"low": 1, "medium": 2, "high": 3}
priority = priority_map[priority_label]

category = st.text_input("Category (e.g., food, exercise)")

if st.button("Add Task"):
    if st.session_state.pet:
        task = Task(task_title, int(duration), priority, category)
        st.session_state.pet.add_task(task)
        st.session_state.tasks.append(task)
        st.success("Task added!")
    else:
        st.error("Please create a pet first.")


# -------------------------
# Display Tasks
# -------------------------
if st.session_state.tasks:
    st.subheader("Current Tasks")
    for t in st.session_state.tasks:
        st.write(f"- {t.task_name} ({t.duration} mins, Priority {t.priority})")
else:
    st.info("No tasks yet.")


# -------------------------
# Generate Schedule
# -------------------------
st.header("Generate Schedule")

if st.button("Generate Plan"):
    if st.session_state.owner and st.session_state.tasks:
        scheduler = Scheduler(
            available_time=st.session_state.owner.get_available_time()
        )

        for task in st.session_state.tasks:
            scheduler.add_task(task)

        schedule = scheduler.generate_schedule()

        st.subheader("Today's Schedule")

        for i, task in enumerate(schedule, 1):
            st.write(
                f"{i}. {task.task_name} - {task.duration} mins (Priority {task.priority})"
            )

        st.subheader("Explanation")
        st.write(scheduler.explain_plan())

    else:
        st.error("Please add owner and tasks first.")