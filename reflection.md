# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

The PawPal+ system allows users to manage pet care efficiently. First, users can add and update information about their pets, which helps customize the experience. Second, users can create and manage care tasks such as feeding, walking, and medication, including details like duration and priority. Finally, the system generates a daily care plan based on available time, task priorities, and user preferences, and provides an explanation for the chosen schedule. 

The system is designed using four main classes: Owner, Pet, Task, and Scheduler. 
The Owner class stores user information and available time. 
The Pet class represents the pet and is linked to the owner. 
The Task class defines individual care activities with attributes like duration and priority. 
The Scheduler class contains the main logic to organize tasks into a daily plan based on constraints and priorities.

**b. Design changes**

Yes, the design changed slightly during implementation. Initially, the relationships between classes were more abstract, but during coding I explicitly linked the Pet class to the Owner class and ensured the Scheduler directly manages a list of Task objects. I also added default lists using dataclasses to simplify initialization. These changes made the system more practical and easier to implement in Python.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler considers several key constraints, including available time, task duration, and task priority. Tasks with higher priority are selected first, and the scheduler ensures that the total duration does not exceed the owner's available time. Preferences can also influence how tasks are interpreted, although they are not strictly enforced in the current implementation. I decided that priority and time constraints mattered most because they directly affect whether tasks can realistically be completed in a given day.

**b. Tradeoffs**

One tradeoff in my scheduler is that conflict detection only checks for tasks with the exact same time rather than overlapping durations. This simplifies the implementation and keeps the algorithm efficient, but it may miss more complex scheduling conflicts where tasks partially overlap. I chose this approach to keep the system simple and easy to understand while still demonstrating basic conflict detection.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI tools throughout the project for brainstorming system design, generating class structures, debugging errors, and improving code organization. AI was especially helpful when creating the UML design, implementing scheduling logic, and integrating the backend with the Streamlit UI. The most helpful prompts were specific and task-oriented, such as asking how to implement sorting, filtering, or conflict detection in a scheduler.

**b. Judgment and verification**

There were situations where I did not accept AI suggestions directly, especially when the solutions were overly complex or did not match the assignment requirements. I evaluated suggestions by testing them in my code and checking whether they aligned with the project goals. If a solution made the system harder to understand, I simplified it to maintain clarity and correctness.

---

## 4. Testing and Verification

**a. What you tested**

I tested several key behaviors, including task completion, adding tasks to pets, sorting tasks by time, recurring task generation, and conflict detection. These tests were important because they ensured that the core functionality of the scheduler worked correctly and handled both normal and edge cases.

**b. Confidence**

I am highly confident that my scheduler works correctly for the main use cases, as all tests pass successfully. However, if I had more time, I would test additional edge cases such as overlapping task durations, multiple pets with complex schedules, and more advanced recurring task patterns.

---

## 5. Reflection

**a. What went well**

The part I am most satisfied with is the scheduling logic and how it integrates with the Streamlit UI. The system successfully connects backend logic with a user-friendly interface, making it easy to use and understand.

**b. What you would improve**

If I had another iteration, I would improve the scheduling algorithm to handle overlapping time conflicts more accurately and support more advanced recurring tasks. I would also enhance the UI by allowing users to assign tasks to specific pets more clearly.

**c. Key takeaway**

One important takeaway from this project is the value of combining clear system design with incremental development. I also learned how to effectively use AI as a tool for guidance while still applying my own judgment to ensure the final solution is correct and understandable.