# 🐈 CatCursor

A lightweight Windows desktop companion that follows your mouse cursor and falls asleep when the cursor is idle.

CatCursor is built with Python, Pygame, and PyWin32, and runs as a transparent click-through overlay on top of the desktop.

---

## Features

- 🐾 Follows the mouse cursor smoothly
- ↔️ Automatically faces left or right based on cursor movement
- 😴 Switches to a sleeping animation after inactivity
- 🖥️ Transparent desktop overlay
- 🖱️ Does not interfere with mouse clicks
- 🚀 Can be configured to launch automatically on Windows startup
- 🎨 Custom sprite support

---

## Preview

### Walking State

The cat follows the cursor while moving.

### Sleeping State

After a few seconds of inactivity, the cat switches to a sleeping animation.

---

## Tech Stack

- Python 3.12+
- Pygame Community Edition
- PyWin32
- PyInstaller

---

## Project Structure

```text
CatCursor/
│
├── main.py
│
├── assets/
│   ├── walk_1.png
│   ├── walk_2.png
│   ├── walk_3.png
│   ├── walk_4.png
│   ├── sleep_1.png
│   └── sleep_2.png
│
├── requirements.txt
│
└── README.md
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/CatCursor.git
cd CatCursor
```

### 2. Create Virtual Environment

```powershell
python -m venv venv
```

Activate:

```powershell
.\venv\Scripts\activate
```

### 3. Install Dependencies

```powershell
pip install pygame-ce pywin32
```

---

## Running the Project

```powershell
python main.py
```

The cat should appear on your desktop and begin following your cursor.

---

## Building an Executable

Install PyInstaller:

```powershell
pip install pyinstaller
```

Build:

```powershell
pyinstaller --onefile --noconsole --name CatCursor main.py
```

Generated executable:

```text
dist/
└── CatCursor.exe
```

---

## Important

The executable expects the following structure:

```text
dist/
│
├── CatCursor.exe
│
└── assets/
    ├── walk_1.png
    ├── walk_2.png
    ├── walk_3.png
    ├── walk_4.png
    ├── sleep_1.png
    └── sleep_2.png
```

Make sure the `assets` folder is located next to `CatCursor.exe`.

---

## Launch Automatically on Windows Startup

1. Press `Win + R`
2. Run:

```text
shell:startup
```

3. Create a shortcut to:

```text
CatCursor.exe
```

inside the Startup folder.

CatCursor will now launch automatically when Windows starts.

---

## Customization

### Change Follow Speed

Inside `main.py`:

```python
FOLLOW_SPEED = 0.25
```

Higher value:

- Faster response
- Less lag

Lower value:

- More natural movement
- More trailing effect

---

### Change Idle Time

```python
IDLE_TIME = 3.0
```

Controls how long the cursor must remain stationary before the sleeping animation begins.

---

### Change Sprite Size

```python
SPRITE_SCALE = 0.5
```

Examples:

```python
SPRITE_SCALE = 0.4
SPRITE_SCALE = 0.6
SPRITE_SCALE = 1.0
```

## Acknowledgements

Built with:

- Pygame CE
- PyWin32
- PyInstaller

Inspired by desktop pets and animated cursor companions.
