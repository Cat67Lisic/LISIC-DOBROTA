import pygame
import keyboard
import sys

# Только аудиоподсистема
pygame.mixer.init()

# Загрузка и воспроизведение
try:
    pygame.mixer.music.load("NA_BASBUSTED_-_CHTO_TAKOE_DOBROTA_66317793.wav")
    pygame.mixer.music.play()
    print("Воспроизведение началось. Нажмите ESC для остановки.")
except pygame.error as e:
    print(f"Ошибка: {e}")
    sys.exit(1)

# Обработчик нажатия ESC
def on_esc():
    print("Воспроизведение остановлено.")
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    sys.exit(0)

# Перехват клавиши ESC (работает даже в фоне)
keyboard.add_hotkey('esc', on_esc)

try:
    # Ждём, пока музыка не закончится или не будет нажата ESC
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
finally:
    pygame.mixer.quit()
