A command line image editor which requires python 3 and can open .ppm files (P3 only).

Run with:
"python3 goodImageEditor.py imagename.ppm" if you want to edit an existing image
"python3 goodImageEditor.py yourwidth yourheight" if you want to create a blank image

Normal commands:

"paint XXXXXX", where XXXXXX is a hex code of a color, paints the pixel under the cursor to that color.
"move up/down/left/right" moves the cursor.
"save" saves current image to opened file (if there is one).
"save filename.ppm" saves current image to filename.ppm.
"quit" quits without saving.

Hacker mode is enabled and disabled by "toggle h4ck3rMode". In hacker mode, "paint" is replaced by commands such as "red++" and "green--" which modify color values of the selected pixel by one.

PS: Windows 8 and below don't support colored output, so this program won't work on them.