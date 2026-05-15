# Parks and National Parks Explorer

![CI/CD Pipeline](https://github.com/mrbirat1/Deadly-Duo-Project/actions/workflows/ci.yml/badge.svg)

## Project Overview
This application was developed by **Team Deadly Duo** as part of a collaborative coding project.
It helps users discover parks and national parks by displaying useful information such as
location, descriptions, and available activities.

## Team Members
| Name | Role |
|------|------|
| Birat Sapkota | Developer / Recorder |
| Anup Kharel | Developer / Scrum Leader |

## Features
- View all parks and national parks
- Search parks by keyword (name, location, description)
- Filter parks by activity type
- View all available activities
- Automated CI/CD testing with GitHub Actions

## Parks Included
- Royal National Park (Australia)
- Blue Mountains National Park (Australia)
- Yellowstone National Park (USA)
- Yosemite National Park (USA)
- Fiordland National Park (New Zealand)
- Banff National Park (Canada)
- Kakadu National Park (Australia)
- Grand Canyon National Park (USA)

## How to Run
```bash
python parks_explorer.py
```

## How to Run Tests
```bash
pytest test_parks_explorer.py -v
```

## CI/CD Pipeline
This project uses **GitHub Actions** for automated testing.
Every time code is pushed or a pull request is made, the pipeline:
1. Sets up Python environment
2. Installs dependencies
3. Runs all test cases automatically
4. Reports pass/fail results

## Future Enhancements (Backlog)
- Add more parks to the database
- Add a search function by country
- Include photos of parks
- Filter parks by activity type (GUI version)
- Build a graphical user interface (GUI)
- Connect to a live parks API for real-time data

## GitHub Repository
[https://github.com/mrbirat1/Deadly-Duo-Project](https://github.com/mrbirat1/Deadly-Duo-Project)
