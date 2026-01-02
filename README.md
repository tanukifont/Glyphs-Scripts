# Glyphs Scripts for Font Production

## Overview
This is a collection of Python scripts for the [Glyphs 3](https://glyphsapp.com/) application. These tools are designed to streamline and automate various tasks in the font creation workflow.

## How to Download
1. Click the green "Code" button at the top-right of the repository page.
2. Select the "Local" tab and click "Download ZIP".
3. Unzip the downloaded file to find the Python script files (`.py`).

## How to Install
1. In Glyphs, go to `Script > Open Scripts Folder` from the menu bar.
2. A "Scripts" folder will open in Finder. Add the Python script files to this folder.
3. To make Glyphs recognize the new scripts, hold down the **Option key** and click the `Script` menu, then select `Reload Scripts`. (Holding the Option key changes some menu items).
The new scripts will now appear in your script menu.

## How to Use
To run a script in Glyphs, simply select it from the `Script` menu.

---

## Scripts

### Color Font
- **`Add_new_color_palette_dialog.py`**: Opens a dialog to add a new color palette.
- **`Copy_paths_from_lower_layers_to_top_layer.py`**: Copies paths from all layers below the top-most layer to the top-most layer for selected glyphs.

### Features
- **`Auto_Biting.py`**: Automates the creation of "biting" effects where glyphs overlap, by generating necessary `calt` feature code and glyph classes.
  - `Auto Biting_sample_calt.txt`: Sample `calt` feature code.
  - `Auto Biting_sample_classes.txt`: Sample class definitions.

### Label
Change the color label for selected **glyphs**:
- `Change_color_label_to_(0)red.py`
- `Change_color_label_to_(1)orange.py`
- `Change_color_label_to_(2)brown.py`
- `Change_color_label_to_(3)yellow.py`
- `Change_color_label_to_(4)light_green.py`
- `Change_color_label_to_(5)dark_green.py`
- `Change_color_label_to_(6)light_blue.py`
- `Change_color_label_to_(7)dark_blue.py`
- `Change_color_label_to_(8)purple.py`
- `Change_color_label_to_(9)magenta.py`
- `Change_color_label_to_(10)light_gray.py`
- `Change_color_label_to_(11)dark_gray.py`
- `Change_color_label_to_(None)unset.py`

Change the color label for selected **layers**:
- `Change_layer_color_label_to_(0)red.py`
- `Change_layer_color_label_to_(1)orange.py`
- `Change_layer_color_label_to_(2)brown.py`
- `Change_layer_color_label_to_(3)yellow.py`
- `Change_layer_color_label_to_(4)light_green.py`
- `Change_layer_color_label_to_(5)dark_green.py`
- `Change_layer_color_label_to_(6)light_blue.py`
- `Change_layer_color_label_to_(7)dark_blue.py`
- `Change_layer_color_label_to_(8)purple.py`
- `Change_layer_color_label_to_(9)magenta.py`
- `Change_layer_color_label_to_(10)light_gray.py`
- `Change_layer_color_label_to_(11)dark_gray.py`
- `Change_layer_color_label_to_(None)unset.py`

### LTTR/INK
- **`Enable_LTTR_INK_for_selected_layers.py`**: Enables the LTTR/INK plugin for all selected layers.
- **`Export_LTTR_INK_settings.py`**: Exports the LTTR/INK settings for the current master.

### Notes
- **`Record_layer_count_in_notes.py`**: Counts the number of layers in selected glyphs and records the count in the glyph's notes field.

### Path
- **`Apply_segment_component_to_selected_nodes.py`**: Applies a segment component to the selected nodes.
- **`Convert_lines_to_curves.py`**: Converts straight line segments into curve segments for selected paths.
- **`Delete_2_short_sides_in_selected_paths.py`**: Deletes the two shortest sides in selected closed paths. Useful for cleaning up imperfect rectangles.
- **`Delete_handles_in_selection.py`**: Deletes the handles (BCPs) of selected points, converting curves to straight lines.
- **`Select_all_corner_points_and_line_ends.py`**: Selects all corner points and the end points of lines in the current glyph.
- **`Select_all_handles.py`**: Selects all handles (BCPs) in the current glyph.
- **`Select_all_on_curve_points.py`**: Selects all on-curve points in the current glyph.

#### Path > Move & Align
- **`Align_selection_horizontally_center.py`**: Aligns selected points or components to the horizontal center.
- **`Align_selection_vertically_center.py`**: Aligns selected points or components to the vertical center.
- **`Align_selection_to_center.py`**: Aligns selected points or components to both the horizontal and vertical center.
- **`Fit_selection_to_body.py`**: Scales the selection to fit the full glyph body width and height.
- **`Move_selection_to_bottom_left.py`**: Moves the selection to the bottom-left corner of the glyph body (origin).

### Space
- **`Bulk_increase_decrease_side_bearings.py`**: Increases or decreases the side bearings (LSB/RSB) for selected glyphs in bulk via a dialog.

### Tab
- **`Create_tab_with_randomly_shuffled_characters.py`**: Opens a new tab containing all characters from the font, shuffled in a random order.

#### Tab > Sandwich
- **`Create_tab_with_selected_characters_sandwiched_by_hiragana.py`**: Creates a new tab where selected glyphs are placed between "h" and "n" (`/h/selected/n`).
- **`Create_tab_with_selected_characters_sandwiched_by_katakana.py`**: Creates a new tab where selected glyphs are placed between katakana "ha" and "n" (`/ha-katakana/selected/n-katakana`).

---

## Contributing
Bug reports and pull requests are welcome.

## License
Copyright 2024 Tanukizamurai.
Licensed under the Apache License, Version 2.0 (the "License"); you may not use the software provided here except in compliance with the License. You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
