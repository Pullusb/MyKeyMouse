bl_info = {
    "name": "MyKeyMouse",
    "description": "Add 'view selected' and 'view all' actions to mouse buttons 4 and 5",
    "author": "Samuel Bernou",
    "version": (0, 0, 4),
    "blender": (2, 79, 0),
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
    user_preferences = bpy.context.user_preferences
    addon_prefs = user_preferences.addons[__name__].preferences

    #mouse 4 and 5 often correspond to previous and next on mouse device
    if addon_prefs.mkmouse_invert_buttons == True:
        key_one = "BUTTON5MOUSE"
        key_two = "BUTTON4MOUSE"
    else:#default
        key_one = "BUTTON4MOUSE"
        key_two = "BUTTON5MOUSE"

    shortcuts_items = [
 
    ##button 4 - focus selection
    ["Graph Editor", "GRAPH_EDITOR", "graph.view_selected", key_one],
    ["Dopesheet", 'DOPESHEET_EDITOR', "action.view_selected", key_one],
    ["Sequencer", 'SEQUENCE_EDITOR', "sequencer.view_selected", key_one],
    ["Node Editor", "NODE_EDITOR", "node.view_selected", key_one],
    ["NLA Editor", "NLA_EDITOR", "nla.view_selected", key_one],
    ["Clip Editor", "CLIP_EDITOR", "clip.view_selected", key_one],
    ["Image", "IMAGE_EDITOR", "image.view_selected", key_one],
    ["Outliner", "OUTLINER", "outliner.show_active", key_one],

    ##button 5 - view all
    ["Timeline", "TIMELINE", "time.view_all", key_two],
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
    
    ]

    if addon_prefs.mkmouse_viewport_center_on_mouse == True:
        ##button 4 - 3D view > keymap view center pick on mouse (Alt+F)
        shortcuts_items.append(["3D View", "VIEW_3D", "view3d.view_center_pick", key_one])
    else:
        ##- view selected in 3D view (more consistent, same usage in all editor)
        shortcuts_items.append(["3D View", "VIEW_3D", "view3d.view_selected", key_one])


    if addon_prefs.mkmouse_viewport_local_view == True:
        ##button 5 - 3D view > keymap local_view (numpad_slash)
        shortcuts_items.append(["3D View", "VIEW_3D", "view3d.localview", key_two])
    else:
        ##- view all in 3D view (more consistent, same usage in all editor)
        shortcuts_items.append(["3D View", "VIEW_3D", "view3d.view_all", key_two])


    ##appending keymap from above list
    addon = bpy.context.window_manager.keyconfigs.addon
    for item in shortcuts_items:
        #print(item)# printing items for debug
        km = addon.keymaps.new(name = item[0], space_type = item[1])
        kmi = km.keymap_items.new(item[2], type = item[3], value = "PRESS")
        addon_keymaps.append(km)


###---user pref 

class My_key_mouse_addon_pref(bpy.types.AddonPreferences):
    bl_idname = __name__

    mkmouse_invert_buttons = bpy.props.BoolProperty(
        name="Invert buttons everywhere (prev button = view all, next button = view selected)",
        default=False,
        )
    mkmouse_viewport_local_view = bpy.props.BoolProperty(
        name="Use local view (like numpad slash) instead of view all",
        default=False,
        )
    mkmouse_viewport_center_on_mouse = bpy.props.BoolProperty(
        name="Use centering view on mouse (like Alt+F) instead of view selected",
        default=False,
        )

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
            text="Customization (save settings and restart Blender to apply changes)")
        layout.prop(self, "mkmouse_invert_buttons")
 
        layout.label(
            text="Only in 3D viewport:")
        layout.prop(self, "mkmouse_viewport_center_on_mouse")
        layout.prop(self, "mkmouse_viewport_local_view")

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