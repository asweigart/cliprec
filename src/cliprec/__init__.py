"""A cross-platform clipboard monitoring and recording tool. Uses pyperclip. Only works for text.
By Al Sweigart al@inventwithpython.com"""

import pyperclip
import time

__version__ = '1.0.1'

def main():
    print('Recording clipboard... (Ctrl-C to stop)')
    all_content = []
    previous_content = pyperclip.paste()  # Ignore current clipboard contents.
    try:
        while True:
            content = pyperclip.paste()  # Get clipboard contents.

            if content != previous_content:
                # If it's different from the previous, print it:
                print(content)
                all_content.append(content)
                previous_content = content

            time.sleep(0.1)  # Pause to avoid hogging the CPU.
    except KeyboardInterrupt:
        pass

    try:
        input('Recording stopped. Press Enter to copy everything together or Ctrl-C to quit.')
        print('\n'.join(all_content))
        pyperclip.copy('\n'.join(all_content))
    except (KeyboardInterrupt, EOFError):
        pass

if __name__ == '__main__':
    main()
