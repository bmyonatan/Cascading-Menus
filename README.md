# Cascading-Menus
This script makes it easy to add cascading menu's with multiple options to window's Context Menu
After searching the web for how to create submenus in the context menu, I found that there are now tools to esaily achieve this functionality. So I made one.
Creating Cascading Menu's for the context menu is achieved by adding specific 'shell' keys and values in the registry.

To use this tool, either run with out any arguments to create one submenu, or add -n <number_of_menus> to create multiple submenu's.
You then need to enter the file extension for which the submenu will appear, or * for all file types.
The script then queries the default value for that file extension under HKEY_CLASSES_ROOT\<file_extension> to get the associated file type.
Under HKEY_CLASSES_ROOT\<file_type> it then creates a shell key, and under that creates a key for each menu that you will create.
Each menu gets the following values: MUIVerb - the dispaly name for the menu, SubCommands, and optionally an icon value.
The script then asks you to enter the display names of the options, and the program that will be opened with the file selected. The values need to be entered with the following format: <display_name>:<full_path_to_program>

In order to remove the cascading menu's from your contect menu, open the registry (regedit.exe), and navigate to HKEY_CLASSES_ROOT\<file_extension> and check the default value to get the file type. Then navigate to HKEY_CLASSES_ROOT\<file_type>\shell\ and delete the keys that correspond to the menu's you created (Don't delete anything else!)
