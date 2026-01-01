Attention: This is a secure version of dobrota.exe! For exit press esc!
`lisic_dobrota` is a modified, "secure" version of the well—known script `dobrota.exe `. Unlike the original:
- All effects ** do not damage the system** (do not delete files, do not block the OS, do not change settings).
- Added **correct output** by pressing `ESC'.
- The code is structured and commented for understanding.
- Secure Windows API calls are used.

**What does the script do:**
- Plays an audio file (`NA_BASBUSTED_-_CHTO_TAKOE_DOBROTA_66317793.wav`).
- Shows animation effects on the screen (tunnel, inversion, glitches, etc.).
- Displays dialog boxes and warning icons.
- Runs in the background until pressing `ESC'.


## Requirements

- Python 3.7+
- Windows (due to the use of `win32gui`, `ctypes`, etc.)
‑ Installed Python packages:
  ```bash
  pip install pygame keyboard pywin32
Installation and launch


bash
cd lisic_dobrota
Install the dependencies:

bash
pip install -r requirements.txt
Place the NA_BASBUSTED_-_CHTO_TAKOE_DOBROTA_66317793.wav audio file in the root folder of the project.

Run the script:

bash
python lisic_dobrota.py
Usage
Audio playback will start automatically.

Stop the program: press ESC (it works even in the background).

The effects will stop smoothly when you exit.

The main components of the code
Audio system (pygame.mixer) — audio playback.

Windows API (ctypes, win32gui) — working with the screen, windows, cursor.

Multithreading (threading) is the parallel launch of effects.

Keyboard processing — intercepting ESC to exit.

Effects (briefly)
tunnel() — the "tunnel" effect (scaling the screen).

message() — pop-up windows with text.

drawwarning() — random warning icons.

drawerror() — error icons near the cursor.

invers() — inverting the colors of the screen.

glitches() — random "glitch effects".

colors() — applying color filters.

Safety
There is no malicious code: the script does not modify system files, registry, or settings.

Resource control: All descriptors (DC, hdc) are released correctly.

Graceful shutdown: When ESC is pressed, all streams stop and audio turns off.
What will happen if you launch a window with the text HACKED BY LISIC BRO!
There will be glitches in a second!
