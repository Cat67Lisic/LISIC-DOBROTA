import pygame
import keyboard
import sys
import threading
import time
import random
import ctypes
from ctypes import wintypes
import win32gui
import win32ui
import win32con

# Инициализация аудиоподсистемы PyGame
pygame.mixer.init()

# Загрузка и воспроизведение аудио
try:
    pygame.mixer.music.load("NA_BASBUSTED_-_CHTO_TAKOE_DOBROTA_66317793.wav")
    pygame.mixer.music.play()
    print("Воспроизведение началось. Нажмите ESC для остановки.")
except pygame.error as e:
    print(f"Ошибка: {e}")
    sys.exit(1)

# Флаг для остановки всех эффектов
running = True

# Загрузка Windows API
user32 = ctypes.WinDLL('user32', use_last_error=True)
gdi32 = ctypes.WinDLL('gdi32', use_last_error=True)

# Константы
SM_CXSCREEN = 0
SM_CYSCREEN = 1
SRCCOPY = 0x00CC0020
NOTSRCCOPY = 0x00330008
IDI_WARNING = 101
IDI_HAND = 102

# Получение размеров экрана
def get_screen_size():
    return (
        user32.GetSystemMetrics(SM_CXSCREEN),
        user32.GetSystemMetrics(SM_CYSCREEN)
    )

# Обработчик нажатия ESC (для аудио)
def on_esc():
    global running
    print("Воспроизведение остановлено.")
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    running = False
    sys.exit(0)

# Перехват клавиши ESC (работает даже в фоне)
keyboard.add_hotkey('esc', on_esc)

# Эффект: «туннель» (исправленный и оптимизированный)
def tunnel():
    hdc = win32gui.GetDC(0)  # Получаем DC экрана
    hwnd = win32gui.GetDesktopWindow()  # Окно рабочего стола
    
    while running:
        # Получаем координаты рабочего стола
        rect = win32gui.GetWindowRect(hwnd)
        left, top, right, bottom = rect
        
        width = right - left
        height = bottom - top
        
        # Параметры масштабирования: уменьшаем область назначения
        dest_x = 25
        dest_y = 25
        dest_width = width - 50
        dest_height = height - 50
        
        # Копируем и масштабируем изображение
        gdi32.StretchBlt(
            hdc,                  # DC назначения (экран)
            dest_x, dest_y,     # Позиция на экране
            dest_width, dest_height,  # Размер области назначения
            hdc,               # DC источника (тот же экран)
            0, 0,             # Позиция источника
            width, height,      # Размер источника
            SRCCOPY            # Режим копирования
        )
        
        time.sleep(0.1)  # Плавность анимации
    
    win32gui.ReleaseDC(0, hdc)  # Освобождаем DC при выходе

# Остальные эффекты
def message():
    while running:
        win32gui.MessageBox(None, "HACKED BY LISIC BRO", "lisic lol", win32con.MB_SYSTEMMODAL | win32con.MB_OK | win32con.MB_ICONWARNING)
        time.sleep(10)

def drawwarning():
    hdc = win32gui.GetDC(0)
    x, y = get_screen_size()
    while running:
        icon = win32gui.LoadIcon(0, IDI_WARNING)
        win32gui.DrawIcon(hdc, random.randint(0, x), random.randint(0, y), icon)
        time.sleep(0.1)
    win32gui.ReleaseDC(0, hdc)

def drawerror():
    hdc = win32gui.GetDC(0)
    while running:
        pt = wintypes.POINT()
        user32.GetCursorPos(ctypes.byref(pt))
        icon = win32gui.LoadIcon(0, IDI_HAND)
        win32gui.DrawIcon(hdc, pt.x, pt.y, icon)
        time.sleep(0.05)
    win32gui.ReleaseDC(0, hdc)

def invers():
    hdc = win32gui.GetDC(0)
    x, y = get_screen_size()
    while running:
        gdi32.BitBlt(hdc, 0, 0, x, y, hdc, 0, 0, NOTSRCCOPY)
        time.sleep(2)
    win32gui.ReleaseDC(0, hdc)

def glitches():
    hdc = win32gui.GetDC(0)
    x, y = get_screen_size()
    while running:
        x1 = random.randint(0, x - 400)
        y1 = random.randint(0, y - 400)
        x2 = random.randint(0, x - 400)
        y2 = random.randint(0, y - 400)
        w = random.randint(100, 400)
        h = random.randint(100, 400)
        gdi32.BitBlt(hdc, x1, y1, w, h, hdc, x2, y2, SRCCOPY)
        time.sleep(0.15)
    win32gui.ReleaseDC(0, hdc)

def colours():
    desktop = win32gui.GetDC(0)
    x, y = get_screen_size()
    while running:
        upWnd = win32gui.GetForegroundWindow()
        upHdc = win32gui.GetDC(upWnd)
        gdi32.BitBlt(desktop, -1, 1, x, y, upHdc, 2, 2, 0x999999)
        win32gui.ReleaseDC(upWnd, upHdc)
        time.sleep(0.5)
    win32gui.ReleaseDC(0, desktop)

# Основной поток
def main():
    global running
    
    # Запуск потока ожидания клавиши ESC
    esc_thread = threading.Thread(target=wait_for_esc, daemon=True)
    esc_thread.start()

    # Список эффектов
    effects = [drawerror, message, drawwarning, invers, tunnel, glitches, colours]
    threads = []

    # Запуск потоков с эффектами
    for effect in effects:
        thread = threading.Thread(target=effect, daemon=True)
        thread.start()
        threads.append(thread)
        time.sleep(0.5)

    try:
        while running:
            time.sleep(0.1)
    except KeyboardInterrupt:
        running = False

    time.sleep(1)
    print("Программа завершена.")

# Функция ожидания нажатия ESC для завершения программы
def wait_for_esc():
    print("Нажмите Esc для завершения программы...")
    keyboard.wait('esc')
    global running
    running = False
    print("Выход...")

# Запуск программы
if __name__ == "__main__":
    main()
