bl_info = {
    "name": "MyKeyMouse",
    "description": "Add 'view selected' and 'view all' action to mouse button 4 and 5",
    "author": "Samuel Bernou",
    "version": (0, 0, 1),
    "blender": (2, 79, 0),
    "location": "Mouse button 4 and 5 on almost all editors",
    "warning": "",
    "wiki_url": "",
    "category": "Object" }

import bpy

addon_keymaps = []
def register_keymaps():
    addon = bpy.context.window_manager.keyconfigs.addon

    #keymap focus view selected (numpad_period) to mouse button 4 on all related editors
    #keymap view all (home key) to mouse button 5 on all related editors
    #except for 3D view (already have shit+C for that) local view (numpad slash)

    #mouse 4 and 5 often correspond to previous and next on mouse device
    bprev = "BUTTON4MOUSE"
    bnext = "BUTTON5MOUSE"
    

    shortcuts_items = [
 
    ##button 4 - focus selection
    ["3D View", "VIEW_3D", "view3d.view_selected", bprev],
    ["Graph Editor", "GRAPH_EDITOR", "graph.view_selected", bprev],
    ["Dopesheet", 'DOPESHEET_EDITOR', "action.view_selected", bprev],
    ["Sequencer", 'SEQUENCE_EDITOR', "sequencer.view_selected", bprev],
    ["Node Editor", "NODE_EDITOR", "node.view_selected", bprev],
    ["NLA Editor", "NLA_EDITOR", "nla.view_selected", bprev],
    ["Clip Editor", "CLIP_EDITOR", "clip.view_selected", bprev],
    ["Image", "IMAGE_EDITOR", "image.view_selected", bprev],
    ["Outliner", "OUTLINER", "outliner.show_active", bprev],

    ##button 5 - view all
    ["Timeline", "TIMELINE", "time.view_all", bnext],
    ["Graph Editor", "GRAPH_EDITOR", "graph.view_all", bnext],
    ["Image", "IMAGE_EDITOR", "image.view_all", bnext],
    ["Node Editor", "NODE_EDITOR", "node.view_all", bnext],
    ["Dopesheet", "DOPESHEET_EDITOR", "action.view_all", bnext],
    ["NLA Editor", "NLA_EDITOR", "nla.view_all", bnext],
    ["Sequencer", "SEQUENCE_EDITOR", "sequencer.view_all", bnext],
    ["SequencerPreview", "SEQUENCE_EDITOR", "sequencer.view_all_preview", bnext],
    ["Logic Editor", "LOGIC_EDITOR", "logic.view_all", bnext],
    ["Clip Editor", "CLIP_EDITOR", "clip.view_all", bnext],
    ["Clip Graph Editor", "CLIP_EDITOR", "clip.graph_view_all", bnext],
    ["Clip Dopesheet Editor", "CLIP_EDITOR", "clip.dopesheet_view_all", bnext],

    ##button 5 special 3D view > keymap local_view (numpad_slash)
    ["3D View", "VIEW_3D", "view3d.localview", bnext,],
    ##if you prefer view all than local view in 3D view comment previous line and uncomment following
    #["3D View", "VIEW_3D", "view3d.view_all", bnext],

    ]

    ##appending keymap from above list
    for item in shortcuts_items:
        #print(item)# printing items for debug
        km = addon.keymaps.new(name = item[0], space_type = item[1])
        kmi = km.keymap_items.new(item[2], type = item[3], value = "PRESS")
        addon_keymaps.append(km)


def unregister_keymaps():
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        for kmi in km.keymap_items:
            km.keymap_items.remove(kmi)
        wm.keyconfigs.addon.keymaps.remove(km)
    addon_keymaps.clear()


###---register (keymap-only)

def register():
    register_keymaps()

def unregister():
    unregister_keymaps()

if __name__ == "__main__":
    register()

