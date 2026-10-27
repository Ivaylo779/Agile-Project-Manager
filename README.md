# Agile Project Manager

A short Django application for managing projects, sprints, tasks, and labels.

## Features

- Dashboard with an overview of all projects and tasks.
- Create, view, edit, and delete projects.
- Create and manage sprints for a specific project.
- Create and manage tasks for a specific sprint.
- Assign multiple labels to a task.
- Calculate sprint progress based on completed tasks.

## Local setup

1. Create and activate a virtual environment.
2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply the migrations:

   ```bash
   python manage.py migrate
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

5. Open `http://127.0.0.1:8000/` in your browser.

## Main pages

| Page | URL |
|---|---|
| Dashboard | `/` |
| Projects | `/projects/` |
| Sprints | `/sprints/` |
| Tasks | `/tasks/` |
| Labels | `/tasks/labels/` |

## Models

- **Project** – name, description, start date, end date, and status.
- **Sprint** – project, goal, date range, and status.
- **Task** – sprint, title, description, priority, status, and labels.
- **Label** – name and color; one label can be used by multiple tasks.

