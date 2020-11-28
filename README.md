# MyKeyMouse
Blender keymapper addon - Map shortcuts on mouse button 4 and 5 for mouse with additional buttons.

**[Download latest](https://github.com/Pullusb/MyKeyMouse/raw/master/MyKeyMouse.py)** (right click, save Target as)  

**[Download older (2.7 version)](https://github.com/Pullusb/MyKeyMouse/raw/master/MyKeyMouse_279.py)** (right click, save Target as)
  
--------
  
### Description
  
Add '*view selection*' and '*view all*' shortcuts on mouse.
  
Keymapp a list of shortcut for almost all editor where:
- *mouse button 4* (often used as 'previous' action) is used to "get back", fit all elements in view. (like *home* button)
- *mouse button 5* (often used as 'next' action) is used to "go to", focus on selected items. (like *numpad period* button)

In the addons preferences you can choose to invert (button 4 to focus and button 5 to view all) :

It does NOT affect any original shortcut on keyboard.
<br/>
Usual location of button 4 and 5 on a mouse with basic extra buttons (this may vary a lot on different device)

![mouse with additional buttons 4 and 5](https://github.com/Pullusb/images_repo/blob/master/Mouse_button-4-5_zoom.png)
  
  
### Why ?
The location of *home* key and *numpad period* are far from both hands and force you to quit temporarily your rest positions, tending to break the workflow fluidity.
<br/>

### Other added keymaps

- *Ctrl + mouse button 5* Toggle isolate selection (*numpad slash* button)
<br/>

- *Shift + mouse button 4* Snap 3D cursor to selection  
- *Shift + mouse button 5* Snap selection to 3D cursor  
<br/>

- *Alt + mouse button 4* Jump to previous keyframe  
- *Alt + mouse button 5* Jump to next keyframe  
<br/>

- *Ctrl + Shift + alt + mouse mouse button 4* Origin to geometry
- *Ctrl + Shift + alt + mouse mouse button 5* Origin to cursor
<br/>

<!--
- *Ctrl + mouse button 4* Recenter the view on mouse cursor (like "Alt+F"), can be inverted in addon prefs  
- *Ctrl + mouse button 5* Toggle isolate selection (*numpad slash* button), can be inverted in addon prefs  
-->
 
Thanks to [Vincent Lamy for the base idea](https://www.nothing-is-3d.com/article22/blender-utiliser-les-boutons-lateraux-de-la-souris)

---

## changelog:

1.1.1 - 2020-11-28:

- feat: added cursor to selected and selection to cursor for grease pencil
- fix: Bug in keymap register that could affect other addon's keymap
- better UI for infos in addon prefs
- readme: changelog formating updated

1.0.0 - 13-09-2019:

- invert preference work only on the focus/view all shortcut
- fixed bug with keyframe jumping
- new shortcut : move origin point

0.0.9 - 02-06-2019:

- full change of keymap setting:
  - inverting default shortchut to a more logical setup (prev = going back, next = going to).
  - suppressing all preferences that overcomplicated the addon, letting only the possibility to invert everything (maybe delete even this one  later).

0.0.8 - 19-02-2019:

- 2.8 version

0.0.7 - 05-06-2018:

- Added Alt combo to jump keyframe

0.0.4 - nd 0.0.5 (22-04-2018:

- Fix bad keymap unregister
- Added modifiers functions:
  - Shift combo : cursor to selection and selection to cursor
  - Ctrl combo : access alternative view tweak

0.0.3 - 14-04-2018:

- By default shortcuts are now completely consistent (view_selected and view all everywhere)
- added addon preferences to invert buttons and customize shortcut in 3D view.
