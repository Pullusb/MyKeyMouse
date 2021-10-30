# changelog

1.3.0 - 2021-10-30:

- fix: bad mode in for snap selection to cursor / cursor to selected for Grease Pencil
- code: converted to multifile addons and added Changelog
- code: transfered 2.79 version to another repo

1.2.1 - 2020-12-20:

- fix: keymap unregister

1.2.0 - 2020-12-16:

- new shortcut: jump prev/next marker with `shift+alt+mouse4/5` (in every editor)

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

0.0.5 - 22-04-2018:

- Fix bad keymap unregister
- Added modifiers functions:
  - Shift combo : cursor to selection and selection to cursor
  - Ctrl combo : access alternative view tweak

0.0.3 - 14-04-2018:

- By default shortcuts are now completely consistent (view_selected and view all everywhere)
- added addon preferences to invert buttons and customize shortcut in 3D view.
