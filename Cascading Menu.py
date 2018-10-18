# Author: Yonatan Ben-Menachem
# Date: 17.10.18
# Script Name: cascading_menu_script.py
# Description: This script creates cascading menu's for windows context menu

# imports
import argparse
import _winreg

# constants
GLOBAL_HELP = '''This Script makes it very easy to make multiple cascading menu's in the context menu.'''

# main

def main():
    a = argument_parser()
    for menu in range(1, a.number_of_menus + 1):
        print "{}Options for menu #{}{}".format('-' * 20, menu, '-' * 20)
        menuName = raw_input("Enter the display name for the menu: ")
        fileExt = raw_input("Enter the file extension that the menu will be applied on. If you want to apply the meny to all file types enter '*' (include '.'): ")
        fileExtKeySuccess = 1
        while(fileExtKeySuccess):
            try:
                fileExtKey = _winreg.OpenKey(_winreg.HKEY_CLASSES_ROOT, fileExt)
            except WindowsError:
                fileExt = raw_input("The value you entered is incorrect, please enter a correct file extension: ")
            else:
                fileExtKeySuccess = 0
        fileType = _winreg.QueryValue(fileExtKey, None)

        workingKey = _winreg.CreateKey(_winreg.HKEY_CLASSES_ROOT, "{}\\shell\\{}".format(fileType, menuName))
        _winreg.SetValueEx(workingKey, "MUIVerb", 0, _winreg.REG_SZ, menuName)
        _winreg.SetValueEx(workingKey, "SubCommands", 0, _winreg.REG_SZ, "")
        icon = raw_input("Do you want to have an icon for this menu? (y/n): ")
        if icon == 'y':
            iconPath = raw_input("Enter the path to the icon or application that has the icon: ")
            _winreg.SetValueEx(workingKey, "icon", 0, _winreg.REG_SZ, iconPath)
        submenuOptions = []
        option = 1
        print "Enter options to populate the submenu. The options must be in the format - <name>:<path_to_program>. After each option press Enter, and when you are done don't write anything and press enter"
        while option:
            option = raw_input()
            if option:
                submenuOptions.append(option)
        print len(submenuOptions)
        menuKey = _winreg.CreateKey(workingKey, "shell")
        for option in submenuOptions:
            optionName, optionValue = option.split(":")
            optionKey = _winreg.CreateKey(menuKey, optionName)
            _winreg.SetValueEx(optionKey, None, 0, _winreg.REG_SZ, optionName)
            _winreg.SetValueEx(optionKey, "icon", 0, _winreg.REG_SZ, optionValue)
            optionCommandKey = _winreg.CreateKey(optionKey, "command")
            _winreg.SetValueEx(optionCommandKey, None, 0,_winreg.REG_SZ, '{} "%1"'.format(optionValue))



def argument_parser():
    parser = argparse.ArgumentParser(description=GLOBAL_HELP)
    parser.add_argument('-n', '--number-of-menus', type=int, default=1, help="Enter the number of Menu's you want to add")
    return parser.parse_args()

# def create_submenu(menuName, menuPosition=None, fileType=)


if __name__ == '__main__':
    main()
