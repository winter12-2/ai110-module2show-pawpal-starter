from pawpal_system import Task, Pet, Owner


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