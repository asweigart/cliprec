# cliprec
A cross-platform clipboard monitoring and recording tool. Uses pyperclip. Only works for text.

This tool is especially handy when you want to rapidly select multiple segments of text in one application without having to individually paste them somewhere else each time. With this tool, you can record all the bits of text you copied into one place.

# Install

Run `pip install cliprec`

# Quickstart

Run `python cliprec.py`. This will output the following:

    Recording clipboard... (Ctrl-C to stop)

Each time you copy new text, it will appear on the screen:

    Copied this text.
    Copied this text too.
    Lorem ipsum.

When you press Ctrl-C, you will be prompted to either press Enter to copy all of the previous text to the clipboard (separated by newines) or press Ctrl-C again to quit.

    Recording stopped. Press Enter to copy everything together or Ctrl-C to quit.

Alternatively, you can run `import cliprec` and then call `cliprec.main()` to run the program.

The `cliprec.exe` Windows executable is also available in the GitHub repository.
