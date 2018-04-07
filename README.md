# MyKeyMouse
Blender keymapper addon - Map shortcuts on mouse button 4 and 5

**[Download latest](https://github.com/Pullusb/MyKeyMouse/raw/master/MyKeyMouse.py)** (right click, save Target as)  
  
--------
  
Description:
  
The purpose is put 'view selection' and 'view all' shortcut on mouse. having them on numpad is far from both hands so it break your workflow. 
Keymapp a list of shortcut for almost all editor where:
- *mouse button 4* (ofen used as 'previous' action) is used to focus on selected items. (like *numpad period* button in 3D view)
- *mouse button 5* (ofen used as 'next' action) is used to fit all element in view. (like *home* button in timeline)
  
### An exception to confirm the rule
There's an exception : *mouse button 5* in 3D view does not call *view all* (easily accessible with left hand through *Shift+C*) but *view local* (equivalent of *numpad slash*).
If you want the *view all* action to be completely consistent even in 3D view, the line in the code is ready and explained, you just have to edit the .py file to comment line 55 and uncomment line 57 and voila !
  
  
Usual location of button 4 and 5 on a mouse with basic extra buttons (this may vary a lot on different device)
  
![mouse with additional buttons 4 and 5](https://github.com/Pullusb/images_repo/blob/master/Mouse_button-4-5_zoom.png)
  
  
Thanks to [Vincent Lamy for the base idea](https://www.nothing-is-3d.com/article22/blender-utiliser-les-boutons-lateraux-de-la-souris)
