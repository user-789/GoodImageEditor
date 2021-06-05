# GoodImageEditor
A command line image editor which requires python 3 and can open `.ppm` files (P3 only).

---

## Run

To edit an existing image:

```sh
python3 goodImageEditor.py <image_name>.ppm
```

To create a new image:

```sh
python3 goodImageEditor.py <width> <height>
```

## Commands

| Command | Description                               | Argument                                                                             | Sample             |
| ------- | ----------------------------------------- | ------------------------------------------------------------------------------------ | ------------------ |
| `paint` | Paints the pixel under the cursor         | The HEX color to paint                                                               | `paint FFE000`     |
| `move`  | Moves the cursor                          | The direction to move (`up`/`down`/`left`/`right`)                                   | `move left`        |
| `save`  | Saves the image to a existent or new file | The file name (to create a new file) or nothing (to save changes to the opened file) | `save creeper.ppm` |
| `quit`  | Quits without saving                      |                                                                                      | `quit`             |

## Hacker mode

Hacker mode is enabled and disabled by `toggle h4ck3rMode`. In hacker mode, `paint` is replaced by commands such as `red++` and `green--` which modify color values of the selected pixel by one.

---

> PS: Windows 8 and below don't support colored output, so this program won't work on them.
