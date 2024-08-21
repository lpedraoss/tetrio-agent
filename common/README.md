### How to Use the Tetris Bot

To use the bot correctly, you'll need to capture the pixel coordinates where the Tetris pieces are located. Follow these steps:

#### 1. Capture the Pixel Coordinates
- Move your mouse to the exact location where the Tetris piece appears on the screen.
- Run the provided Python code to get the current mouse position and the color of the pixel at that position. The code will print the coordinates and the pixel color in the terminal.
- Note down these coordinates as they correspond to where the Tetris pieces will appear.

    ```python
    import pyautogui
    import pyscreeze

    # Get the current mouse cursor position
    x, y = pyautogui.position()

    # Get the color of the pixel at the cursor position
    pixel_color = pyscreeze.pixel(x, y)

    print(f"The cursor position is: ({x, y})")
    print(f"The pixel color at the cursor position is: {pixel_color}")
    ```

#### 2. Record the Pixel Coordinates
- After capturing the coordinates, store them in the `pixels` dictionary. This dictionary will map the pixel IDs to their corresponding coordinates. Here’s an example:

    ```python
    pixels = {
        # Example coordinates
        1: (937, 157),
        2: (946, 257),
        3: (952, 355), 
        4: (943, 451),
        5: (945, 544)
    }
    ```

#### 3. Execute the Bot
- Once you’ve set up the pixel dictionary, you can run the bot using the command `python main.py gui`. Keep in mind that this version of the bot is limited to 40 lines of code, so it’s still a bit basic and might need further refinement.

---

To summarize, capture the pixel positions of where the Tetris pieces will appear, record those positions in the `pixels` dictionary, and run the bot. This bot is currently in its early stages, so there’s room for improvement, but it should help you get started.
