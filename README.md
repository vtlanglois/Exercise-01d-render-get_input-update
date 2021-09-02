# Exercise-01d-render-get_input-update
Exercise for MSCH-C220, 2 September 2021

This exercise will get you much closer to a basic solution to Project 01. You will be implementing the game loop using render, get_input, and update functions.

Begin by Forking this repository. Check that it has been forked successfully; the repository should now read [your username]/Exercise-01d-render-get_input-update

Edit the LICENSE and replace BL-MSCH-C220-F21 with your full name. Commit your changes.

Press the green "Code" button and select "Open in GitHub Desktop". Allow the browser to open (or install) GitHub Desktop. Once GitHub Desktop has loaded, you should see a window labeled "Clone a Repository" asking you for a Local Path on your computer where the project should be copied. Choose a location. Make sure the Local Path ends with "Exercise-01d-render-get_input-update" and then press the "Clone" button. GitHub Desktop will now download a copy of the repository to the location you indicated.

Open the folder in VS Code. You should see five files: .gitignore, LICENSE, main.py, Zork.html, and README.md. First, open Twine.

The first step will be to export Zork.html as a json object. If you have not installed the "Harlowe 3 to JSON 0.0.6" format, do that first: (In the right-hand sidebar, select "Formats". You should see a list of possible story formats for Twine. In the bar on the top of that window is a button "Add a New Format". Select that now. The window should now read "To add a story format, enter its address below." Enter https://jtschoonhoven.github.io/twine-to-json/dist/harlowe-3.js and press the green "Add" button.)

Select "Import from File" from the right-hand sidebar and select Zork.html. After it has loaded, select the Zork menu and "Change Story Format". Select Harlowe 3 to JSON 0.0.6. "Play" the story; a browser window should open with the Zork story represented as a JSON object. Copy the contents of that browser window. 

Open main.py in VS Code. In main.py, you will see a world variable defined on line 5. Replace the {} with the JSON object you exported out of Twine.

Your final task is to implement each of the three functions that are part of the game loop: render(), get_input(), and update().

**render()** should display the name and description (using the "cleanText" key) of the current location. You can choose to print out the player's options if you would like to.

**get_input()** should ask the player what they would like to do and return what the player types in response. I would recommend normalizing that response using .upper() (to make it upper case) and .strip() (to remove any extraneous whitespace).

**update()** should check the player's response against the list of links in the current passage. If the player's response matches the "linkText", update() should return the name of the new location.

This is probably the learning-curve jump so far, so if this seems overwhelming, feel free to follow my video demonstration. When you are  done, run the program to make sure it is functioning correctly. Then, save your files and return to Github Desktop.

In GitHub Desktop, you should now see main.py highlighted. Add a Summary message at the bottom of that panel, and push the "Commit to master" button. On the right side of the top, black panel, you should see a button labeled "Push origin". Press that now.

In GitHub Desktop, you should now see main.py highlighted. Add a Summary message at the bottom of that panel (something like "Implements game loop"), and push the "Commit to master" button. On the right side of the top, black panel, you should see a button labeled "Push origin". Press that now.

If you return to and refresh your GitHub repository page, you should now see that your files have been changed (with a new date).

Now edit the README.md file. When you have finished editing, commit your changes, and then turn in the URL of the main repository page (https://github.com/[username]/Exercise-01d-render-get_input-update) on Canvas.

The final state of the file should be as follows (replacing my information with yours):
```
# Exercise-01d-render-get_input-update
Exercise for MSCH-C220, 2 September 2021

A simple interactive-fiction game loop that allows players to experience eight locations from the classic Zork, implemented in Python.

## Implementation
Created using Python 3.9

## References
[Zork, 1977 by Tim Anderson, Marc Blank, Dave Lebling, and Bruce Daniels](https://en.wikipedia.org/wiki/Zork)

## Future Development
None

## Created by
Jason Francis
```
