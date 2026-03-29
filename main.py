from pawpal_system import Owner, Pet, Task, Scheduler


# -------------------------
# Create Owner
# -------------------------
owner = Owner("Senthil", 90, "Prefers morning activities")

# -------------------------
# Create Pets (at least 2)
# -------------------------
pet1 = Pet("Buddy", "Dog", 3, owner)
pet2 = Pet("Whiskers", "Cat", 2, owner)

# -------------------------
# Add Tasks to Pets
# -------------------------
task1 = Task("Walk Buddy", 30, 3, "exercise")
task2 = Task("Feed Whiskers", 10, 5, "food")
task3 = Task("Play with Buddy", 20, 2, "enrichment")
task4 = Task("Groom Whiskers", 25, 1, "care")

pet1.add_task(task1)
pet1.add_task(task3)

pet2.add_task(task2)
pet2.add_task(task4)

# -------------------------
# Create Scheduler
# -------------------------
scheduler = Scheduler(available_time=owner.get_available_time())

# Add all pet tasks to scheduler
for pet in [pet1, pet2]:
    for task in pet.tasks:
        scheduler.add_task(task)

# -------------------------
# Generate Schedule
# -------------------------
schedule = scheduler.generate_schedule()

# -------------------------
# Print Schedule
# -------------------------
print("\nToday's Schedule:\n")

for i, task in enumerate(schedule, 1):
    print(f"{i}. {task.task_name} - {task.duration} mins (Priority {task.priority})")

# -------------------------
# Print Explanation
# -------------------------
print("\nExplanation:")
print(scheduler.explain_plan())