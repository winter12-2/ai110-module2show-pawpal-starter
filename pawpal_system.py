from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime, timedelta


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
# Task Class
# -------------------------
@dataclass
class Task:
    task_name: str
    duration: int
    priority: int
    category: str
    completed: bool = False
    time: str = "09:00"  # format HH:MM
    frequency: Optional[str] = None  # "daily", "weekly", or None

    def update_task(self, task_name=None, duration=None, priority=None, category=None):
        if task_name is not None:
            self.task_name = task_name
        if duration is not None:
            self.duration = duration
        if priority is not None:
            self.priority = priority
        if category is not None:
            self.category = category

    def mark_complete(self):
        """Mark task complete and create next occurrence if recurring"""
        self.completed = True

        if self.frequency == "daily":
            return Task(
                self.task_name,
                self.duration,
                self.priority,
                self.category,
                completed=False,
                time=self.time,
                frequency="daily"
            )

        return None

    def get_task_details(self) -> str:
        return f"{self.task_name} - {self.duration} mins (Priority: {self.priority}, Time: {self.time})"


# -------------------------
# Pet Class
# -------------------------
@dataclass
class Pet:
    name: str
    type: str
    age: int
    owner: Owner
    tasks: List[Task] = field(default_factory=list)

    def get_pet_info(self) -> str:
        return f"{self.name} ({self.type}, {self.age} years old)"

    def add_task(self, task: Task):
        self.tasks.append(task)


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
        """Sort tasks by priority (high → low)"""
        self.tasks.sort(key=lambda t: t.priority, reverse=True)

    def sort_by_time(self):
        """Sort tasks by time (HH:MM format)"""
        self.tasks.sort(key=lambda t: t.time)

    def filter_tasks(self, completed: Optional[bool] = None):
        """Filter tasks by completion status"""
        if completed is None:
            return self.tasks
        return [t for t in self.tasks if t.completed == completed]

    def generate_schedule(self):
        """Greedy scheduling based on priority and available time"""
        self.sort_by_priority()

        remaining_time = self.available_time
        self.schedule = []

        for task in self.tasks:
            if task.duration <= remaining_time:
                self.schedule.append(task)
                remaining_time -= task.duration

        return self.schedule

    def detect_conflicts(self):
        """Detect tasks scheduled at the same time"""
        conflicts = []
        seen_times = {}

        for task in self.schedule:
            if task.time in seen_times:
                conflicts.append((task, seen_times[task.time]))
            else:
                seen_times[task.time] = task

        return conflicts

    def explain_plan(self) -> str:
        if not self.schedule:
            return "No tasks could be scheduled."

        explanation = "Tasks selected based on priority and available time:\n"

        for task in self.schedule:
            explanation += f"- {task.task_name} (Priority {task.priority}, {task.duration} mins, Time {task.time})\n"

        return explanation