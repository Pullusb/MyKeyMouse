bl_info = {
    "name": "MyKeyMouse",
    "description": "Add 'view selected' and 'view all' actions to mouse buttons 4 and 5",
    "author": "Samuel Bernou",
    "version": (0, 0, 9),
    "blender": (2, 80, 0),
    "location": "Mouse button 4 (usually 'previous') and 5 (usually 'next') on almost all editors",
    "warning": "",
    "wiki_url": "",
    "category": "Object" }

import bpy
import os

#keymap focus view selected (numpad_period) to mouse button 4 on all related editors
#keymap view all (home key) to mouse button 5 on all related editors

#customisation
#3D view only :
#  Button 4 can view center pick on mouse instead (really a mouse related shortcut)
#  Button 5 can do local view instead (already have shit+C accessible for view all)


addon_keymaps = []
def register_keymaps():
    preferences = bpy.context.preferences
    addon_prefs = preferences.addons[__name__].preferences

    #mouse 4 and 5 often correspond to previous and next on mouse device
    if addon_prefs.mkmouse_invert_buttons == True:
        key_one = "BUTTON4MOUSE"
        key_two = "BUTTON5MOUSE"
    else:#default
        key_one = "BUTTON5MOUSE"
        key_two = "BUTTON4MOUSE"

    shortcuts_items = [
 
    ##button 4 - focus selection
    ["3D View", "VIEW_3D", "view3d.view_selected", key_one],
    ["Graph Editor", "GRAPH_EDITOR", "graph.view_selected", key_one],
    ["Dopesheet", 'DOPESHEET_EDITOR', "action.view_selected", key_one],
    ["Sequencer", 'SEQUENCE_EDITOR', "sequencer.view_selected", key_one],
    ["Node Editor", "NODE_EDITOR", "node.view_selected", key_one],
    ["NLA Editor", "NLA_EDITOR", "nla.view_selected", key_one],
    ["Clip Editor", "CLIP_EDITOR", "clip.view_selected", key_one],
    ["Image", "IMAGE_EDITOR", "image.view_selected", key_one],
    ["Outliner", "OUTLINER", "outliner.show_active", key_one],

    ##button 5 - view all
    ["3D View", "VIEW_3D", "view3d.view_all", key_two],
    ["Graph Editor", "GRAPH_EDITOR", "graph.view_all", key_two],
    ["Image", "IMAGE_EDITOR", "image.view_all", key_two],
    ["Node Editor", "NODE_EDITOR", "node.view_all", key_two],
    ["Dopesheet", "DOPESHEET_EDITOR", "action.view_all", key_two],
    ["NLA Editor", "NLA_EDITOR", "nla.view_all", key_two],
    ["Sequencer", "SEQUENCE_EDITOR", "sequencer.view_all", key_two],
    ["SequencerPreview", "SEQUENCE_EDITOR", "sequencer.view_all_preview", key_two],
    ["Logic Editor", "LOGIC_EDITOR", "logic.view_all", key_two],
    ["Clip Editor", "CLIP_EDITOR", "clip.view_all", key_two],
    ["Clip Graph Editor", "CLIP_EDITOR", "clip.graph_view_all", key_two],
    ["Clip Dopesheet Editor", "CLIP_EDITOR", "clip.dopesheet_view_all", key_two],

    #not exists anymore
    # ["Timeline", "TIMELINE", "time.view_all", key_two],
    #["Logic Editor", "LOGIC_EDITOR", "logic.view_all", key_two],

    #other
    #["Frames", "EMPTY", "screen.keyframe_jump", key_one, False, False, True]
    
    ]

    shortcuts_items.append(["3D View", "VIEW_3D", "view3d.localview", key_one, True, False, False])

    # Snapping utility with shift (cursor to selection and selection to selected)
    shortcuts_items.append(["3D View", "VIEW_3D", "view3d.snap_cursor_to_selected", key_two, False, True, False])
    shortcuts_items.append(["3D View", "VIEW_3D", "view3d.snap_selected_to_cursor", key_one, False, True, False])

    
    ##3D view > keymap view center pick on mouse (Alt+F) Changed to 'alt + MMB' to match early 2.8 settings
    #if LooseVersion(str(bpy.app.version)) < LooseVersion('(2, 80, 0)'):#only set for 2.79
    shortcuts_items.append(["3D View", "VIEW_3D", "view3d.view_center_pick", "MIDDLEMOUSE", False, False, True])

    ## appending all keymap from above list
    addon = bpy.context.window_manager.keyconfigs.addon
    for item in shortcuts_items:
        #print(item)# printing items for debug
        km = addon.keymaps.new(name = item[0], space_type = item[1])
        if len(item) > 4:#contain modifiers keys
            kmi = km.keymap_items.new(item[2], type = item[3], value = "PRESS", ctrl=item[4], shift=item[5],alt=item[6])
        else:
            kmi = km.keymap_items.new(item[2], type = item[3], value = "PRESS")
        addon_keymaps.append(km)


        #special case (because hold properties), combo keyframe jump with alt (button 6 et 7 not working with logitech software...)
        km = addon.keymaps.new(name = "Frames", space_type = "EMPTY")
        #kmi = km.keymap_items.new("screen.keyframe_jump", type = "BUTTON6MOUSE", value = "PRESS")#mouse button above 5 aren't recognize on logitech mouse on windaube
        kmi = km.keymap_items.new("screen.keyframe_jump", type = key_one, value = "PRESS", alt = True)
        kmi.properties.next = False
        #kmi = km.keymap_items.new("screen.keyframe_jump", type = "BUTTON7MOUSE", value = "PRESS")#mouse button above 5 aren't recognize on logitech mouse on windaube
        kmi = km.keymap_items.new("screen.keyframe_jump", type = key_two, value = "PRESS", alt = True)
        kmi.properties.next = True




###---user pref 

class My_key_mouse_addon_pref(bpy.types.AddonPreferences):
    bl_idname = __name__

    mkmouse_invert_buttons : bpy.props.BoolProperty(
        name="Invert buttons everywhere (prev button = view all, next button = view selected)",
        default=False,
        )
    '''
    mkmouse_viewport_local_view : bpy.props.BoolProperty(
        name="Use local view (instead of view all)",
        default=False,
        )#"Use local view (like numpad slash) instead of view all (else combine ctrl)"
    mkmouse_viewport_center_on_mouse : bpy.props.BoolProperty(
        name="Use centering view on mouse (instead of view selected)",
        default=False,
        )#"Use centering view on mouse (like Alt+F) instead of view selected (else combine ctrl)"
    '''

    def draw(self, context):
        layout = self.layout
        layout.label(
            text="In all editor :")
        layout.label(
            text="mouse Prev button = view selected")
        layout.label(
            text="mouse Next button = view all")
        layout.label(text="")

        layout.label(
            text="Only in 3D viewport:")
        
        layout.label(text="Ctrl + mouse Next button = Use local view (like numpad slash)")
        #layout.label(text="Ctrl + mouse Prev button = Use centering view on mouse ")

        layout.label(text="Cursor Snapping:")
        layout.label(text="Shift + mouse Prev button = 3D cursor to selection")
        layout.label(text="Shift + mouse Next button = selection to 3D cursor")
        layout.label(text="")

        layout.label(text="Extra:")
        layout.label(text="Alt + middle mouse button = centering view on mouse (default shortcut in 2.8) as with Alt+F ")
        layout.label(text="Alt + mouse Prev button = jump to prev keyframe ")
        layout.label(text="Alt + mouse Next button = jump to next keyframe ")
        layout.label(text="")
        layout.label(
            text="Customization (save settings and restart Blender to apply changes)")
        layout.prop(self, "mkmouse_invert_buttons")
        '''
        layout.label(
            text="Options to swap calls in 3D viewport (accessible with 'ctrl' modifier):") 
        layout.prop(self, "mkmouse_viewport_center_on_mouse")
        layout.prop(self, "mkmouse_viewport_local_view")
        '''

def unregister_keymaps():
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        for kmi in km.keymap_items:
            km.keymap_items.remove(kmi)
        ## Can't (and supposedly shouldn't ) suppress original category name...
        # wm.keyconfigs.addon.keymaps.remove(km)
    addon_keymaps.clear()



## note : register via bpy.utils.register_module(__name__) Fails !
## addons prefs isn't loaded when keymap_register try to access it.

def register():
    if not bpy.app.background:
        bpy.utils.register_class(My_key_mouse_addon_pref)
        register_keymaps()

def unregister():
    if not bpy.app.background:
        unregister_keymaps()
        bpy.utils.unregister_class(My_key_mouse_addon_pref)

if __name__ == "__main__":
    register()