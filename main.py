import pygame
import win32api
import win32gui
import win32con
import time
import sys
from pathlib import Path

# ==========================
# FIND ASSET FOLDER
# ==========================

if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys.executable).parent
else:
    BASE_DIR = Path(__file__).parent

ASSET_DIR = BASE_DIR / "assets"

# ==========================
# SETTINGS
# ==========================

FPS = 60

FOLLOW_SPEED = 0.25

IDLE_TIME = 3.0

FRAME_TIME = 0.15

SPRITE_SCALE = 0.5

# ==========================
# LOAD SPRITES
# ==========================

def load_frames(prefix, count):

    frames = []

    for i in range(1, count + 1):

        image = pygame.image.load(
            ASSET_DIR / f"{prefix}_{i}.png"
        ).convert_alpha()

        width = int(image.get_width() * SPRITE_SCALE)
        height = int(image.get_height() * SPRITE_SCALE)

        image = pygame.transform.smoothscale(
            image,
            (width, height)
        )

        frames.append(image)

    return frames

# ==========================
# INIT
# ==========================

pygame.init()

screen_width = win32api.GetSystemMetrics(0)
screen_height = win32api.GetSystemMetrics(1)

screen = pygame.display.set_mode(
    (screen_width, screen_height),
    pygame.NOFRAME
)

pygame.display.set_caption("CatCursor")

# ==========================
# TRANSPARENT OVERLAY
# ==========================

hwnd = pygame.display.get_wm_info()["window"]

style = (
    win32gui.GetWindowLong(
        hwnd,
        win32con.GWL_EXSTYLE
    )
    | win32con.WS_EX_LAYERED
    | win32con.WS_EX_TRANSPARENT
    | win32con.WS_EX_TOPMOST
    | win32con.WS_EX_TOOLWINDOW
)

win32gui.SetWindowLong(
    hwnd,
    win32con.GWL_EXSTYLE,
    style
)

TRANSPARENT_COLOR = (255, 0, 255)

win32gui.SetLayeredWindowAttributes(
    hwnd,
    win32api.RGB(*TRANSPARENT_COLOR),
    0,
    win32con.LWA_COLORKEY
)

# ==========================
# LOAD ANIMATIONS
# ==========================

walk_frames = load_frames("walk", 4)
sleep_frames = load_frames("sleep", 2)

# ==========================
# INITIAL STATE
# ==========================

mouse_x, mouse_y = win32api.GetCursorPos()

cat_x = float(mouse_x)
cat_y = float(mouse_y)

last_mouse_pos = (mouse_x, mouse_y)

last_move_time = time.time()

state = "walk"

direction = "right"

frame_index = 0

frame_timer = 0

clock = pygame.time.Clock()

# ==========================
# MAIN LOOP
# ==========================

running = True

while running:

    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    mouse_x, mouse_y = win32api.GetCursorPos()

    current_pos = (mouse_x, mouse_y)

    # ------------------
    # DIRECTION
    # ------------------

    dx = mouse_x - last_mouse_pos[0]

    if dx > 0:
        direction = "right"

    elif dx < 0:
        direction = "left"

    # ------------------
    # IDLE DETECTION
    # ------------------

    if current_pos != last_mouse_pos:

        state = "walk"

        last_move_time = time.time()

        last_mouse_pos = current_pos

    else:

        idle = time.time() - last_move_time

        if idle >= IDLE_TIME:

            state = "sleep"

    # ------------------
    # FOLLOW CURSOR
    # ------------------

    cat_x += (mouse_x - cat_x) * FOLLOW_SPEED
    cat_y += (mouse_y - cat_y) * FOLLOW_SPEED

    # ------------------
    # ANIMATION
    # ------------------

    frame_timer += dt

    if frame_timer >= FRAME_TIME:

        frame_timer = 0

        frame_index += 1

    if state == "walk":

        frame = walk_frames[
            frame_index % len(walk_frames)
        ]

    else:

        frame = sleep_frames[
            frame_index % len(sleep_frames)
        ]

    # ------------------
    # FACE LEFT/RIGHT
    # ------------------

    if direction == "left":

        frame = pygame.transform.flip(
            frame,
            True,
            False
        )

    # ------------------
    # DRAW
    # ------------------

    screen.fill(TRANSPARENT_COLOR)

    frame_width = frame.get_width()
    frame_height = frame.get_height()

    screen.blit(
        frame,
        (
            int(cat_x - frame_width / 2),
            int(cat_y - frame_height / 2)
        )
    )

    pygame.display.update()

pygame.quit()