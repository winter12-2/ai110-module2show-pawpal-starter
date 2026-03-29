from pawpal_system import Task, Pet, Owner, Scheduler


# -------------------------
# Existing Tests
# -------------------------
def test_mark_complete():
    task = Task("Walk", 30, 3, "exercise")
    task.mark_complete()
    assert task.completed == True


def test_add_task_to_pet():
    owner = Owner("Senthil", 60, "none")
    pet = Pet("Buddy", "Dog", 3, owner)

    task = Task("Feed", 10, 5, "food")
    pet.add_task(task)

    assert len(pet.tasks) == 1


# -------------------------
# NEW TESTS (Phase 4)
# -------------------------

def test_sort_by_time():
    scheduler = Scheduler()

    t1 = Task("Task1", 10, 1, "test", time="10:00")
    t2 = Task("Task2", 10, 1, "test", time="08:00")
    t3 = Task("Task3", 10, 1, "test", time="09:00")

    scheduler.add_task(t1)
    scheduler.add_task(t2)
    scheduler.add_task(t3)

    scheduler.sort_by_time()

    assert scheduler.tasks[0].time == "08:00"
    assert scheduler.tasks[1].time == "09:00"
    assert scheduler.tasks[2].time == "10:00"


def test_recurring_task():
    task = Task("Feed", 10, 3, "food", frequency="daily")

    new_task = task.mark_complete()

    assert task.completed == True
    assert new_task is not None
    assert new_task.frequency == "daily"


def test_conflict_detection():
    scheduler = Scheduler(available_time=100)

    t1 = Task("Walk", 30, 3, "exercise", time="09:00")
    t2 = Task("Feed", 10, 5, "food", time="09:00")  # same time = conflict

    scheduler.add_task(t1)
    scheduler.add_task(t2)

    scheduler.generate_schedule()
    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1