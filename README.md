# Campus Lost and Found Management System

## Project Description
A simple Python console application to manage lost and found items on a college campus. Users can add, view, search, update, and delete item records.

## Objectives
- Maintain records of lost and found items.
- Search for items by name.
- Mark returned items.
- Organize project tasks using GitHub Projects Kanban board.

## Technologies Used
- Python 3
- Visual Studio Code
- GitHub and GitHub Projects

## Features
1. **Add Item:** Record item name, Lost/Found type, location, and date.
2. **View Items:** Display item IDs, details, and statuses.
3. **Search Item:** Search by item name (case-insensitive).
4. **Mark Item as Returned:** Update the selected item's status.
5. **Delete Item:** Remove an item by its displayed ID.
6. **Exit:** Close the application.

## How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in VS Code or a terminal.
4. Run:

```bash
python main.py
```

> If your Python file has a different name, replace `main.py` with that filename.

## Sample Menu
```text
===== LOST AND FOUND MANAGEMENT =====
1. Add Item
2. View Items
3. Search Item
4. Mark Item as Returned
5. Delete Item
6. Exit
Enter your choice:
```

## Kanban Workflow
Tasks are tracked in GitHub Projects using **Backlog**, **Ready**, **In progress**, **In review**, and **Done** statuses.

## Limitations
- Records are stored in memory in a Python list and disappear when the program exits.
- There is no database or user authentication.
- The application runs in the terminal.

## Future Enhancements
- Save records permanently using SQLite.
- Add a graphical user interface.
- Add user accounts and matching suggestions.

## Conclusion
This mini project demonstrates basic Python functions, lists, dictionaries, loops, input handling, and simple task tracking with GitHub Projects.
