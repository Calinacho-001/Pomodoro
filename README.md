# Pomodoro Timer🍅

## Description

This is a **Pomodoro Timer** built with Python using the Tkinter library, designed to help users manage their work and break periods based on the [Pomodoro Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique). The project showcases key programming concepts such as Object-Oriented Programming (OOP), GUI development, and time-based functionality.

## Features

- **Timer Functionality**: Start a countdown for work or break periods, with the ability to reset the timer.
- **Visual Timer Display**: A dynamic countdown display, showing minutes and seconds in a formatted timer.
- **Break Management**: Switch between work sessions, short breaks, and long breaks based on the Pomodoro Technique (25 minutes of work followed by short breaks and long breaks after several work sessions).
- **Work Session Tracking**: Track the number of completed work sessions with checkmarks that appear after each work session.
- **Start/Reset Buttons**: Control the timer through a simple Start button, and reset the timer when needed.

## Requirements

- Python 3.x
- Tkinter library (built into Python standard library, no installation required)

## How to Use

<details>
<summary>Click here for detailed instructions</summary>

1. **Start the Application**:
   - Run the application by executing the `main.py` file with Python.
   - To start the app, simply execute the following command in the terminal:


2. **Input**:
- No input is required from the user except clicking the Start and Reset buttons.

3. **Functionality**:
- **Start**: Click the "Start" button to begin a work session. The timer will count down from 25 minutes (by default). 
- **Reset**: Click the "Reset" button to stop the timer, clear the checkmarks, and reset the timer to the default state (00:00).
- **Timer Behavior**: After every work session (25 minutes), a short break (5 minutes) will follow. After every 4th work session, a longer break (20 minutes) will occur.

</details>

## Code Structure

The project consists of the following file:

<details>
<summary>Click here for file breakdown</summary>

### `main.py`
- **Purpose**: Contains the main logic for the Pomodoro Timer application.
- **Key Functions**:
- `__init__()`: Initializes the GUI and sets up the initial timer values.
- `canvas_for_image()`: Creates the canvas with the tomato image and the timer text.
- `timer_text_label()`: Displays the "Timer" label above the timer.
- `check_mark_label()`: Displays a checkmark after completing a work session.
- `start_button()`: Creates the "Start" button to begin the timer.
- `reset_button()`: Creates the "Reset" button to stop and reset the timer.
- `count_down()`: Handles the countdown logic and updates the timer display.
- `reset_timer()`: Resets the timer to its initial state.
- `start_timer()`: Starts the timer for work or break sessions.
- `layout()`: Organizes all the GUI components.

</details>

## How to Run

1. Clone or download the project files.
2. Make sure Python 3.x is installed on your computer.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the following command to start the application:

```bash
python main.py
```

## Future Improvements

<details>
<summary>Click here for possible future improvements</summary>

- **Improvement 1**: Add sound notifications to signal the end of a work session or break.
- **Improvement 2**: Allow users to customize the length of work sessions, short breaks, and long breaks.
- **Improvement 3**: Add a progress bar to visually indicate the remaining time for each session.
- **Improvement 4**: Store session history (e.g., number of sessions completed, total work time, etc.).

</details>

## Credits

This project was created using Python and Tkinter as part of a personal project to learn about time management techniques and GUI programming.

## Change Log

<details>
<summary>Click here to view change log</summary>

### Version 1.0.0
- **Initial Release**: Basic Pomodoro Timer functionality with Start, Reset buttons and timer countdown.

### Bug Fixes
- Fixed issues with the timer running multiple times if the Start button is clicked repeatedly.
- Prevented overlapping timers when the Start button is clicked multiple times.

### Known Issues
- No audio notifications when the timer finishes.
- The timer display is static and doesn't visually show progress (yet).

</details>
