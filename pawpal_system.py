from dataclasses import dataclass, field
from typing import List


# -------------------------
# Owner Class
# -------------------------
@dataclass
class Owner:
    name: str
    available_time: int
    preferences: str

    def update_preferences(self, new_preferences: str):
        self.preferences = new_preferences

    def get_available_time(self) -> int:
        return self.available_time


# -------------------------
# Pet Class
# -------------------------
@dataclass
class Pet:
    name: str
    type: str
    age: int
    owner: "Owner"
    tasks: List["Task"] = field(default_factory=list)

    def get_pet_info(self) -> str:
        return f"{self.name} ({self.type}, {self.age} years old)"

    def add_task(self, task):
        self.tasks.append(task)


# -------------------------
# Task Class
# -------------------------
@dataclass
class Task:
    task_name: str
    duration: int
    priority: int
    category: str

    def update_task(self, task_name=None, duration=None, priority=None, category=None):
        if task_name is not None:
            self.task_name = task_name
        if duration is not None:
            self.duration = duration
        if priority is not None:
            self.priority = priority
        if category is not None:
            self.category = category

    def get_task_details(self) -> str:
        return f"{self.task_name} - {self.duration} mins (Priority: {self.priority})"


# -------------------------
# Scheduler Class
# -------------------------
@dataclass
class Scheduler:
    tasks: List[Task] = field(default_factory=list)
    available_time: int = 0
    schedule: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)

    def sort_by_priority(self):
        # Sort tasks by priority (higher first)
        self.tasks.sort(key=lambda task: task.priority, reverse=True)

    def generate_schedule(self):
        self.sort_by_priority()

        remaining_time = self.available_time
        self.schedule = []

        for task in self.tasks:
            if task.duration <= remaining_time:
                self.schedule.append(task)
                remaining_time -= task.duration

        return self.schedule

    def explain_plan(self) -> str:
        if not self.schedule:
            return "No tasks could be scheduled within the available time."

        explanation = "Tasks were selected based on priority and available time:\n"

        for task in self.schedule:
            explanation += f"- {task.task_name} (Priority {task.priority}, {task.duration} mins)\n"

        return explanation



