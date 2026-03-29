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

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

One tradeoff in my scheduler is that conflict detection only checks for tasks with the exact same time rather than overlapping durations. This simplifies the implementation and keeps the algorithm efficient, but it may miss more complex scheduling conflicts where tasks partially overlap. I chose this approach to keep the system simple and easy to understand while still demonstrating basic conflict detection.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
