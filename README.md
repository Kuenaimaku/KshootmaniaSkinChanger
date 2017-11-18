# K-Shoot Mania Skin Swapper

Small tool to change your k-shoot mania skin, with preview visuals.

### Details

This tool utilizes the images inside of the base skin folder in order to provide preview images. when you select a skin,
it will delete the `cache`, `imgs`, and `se` folders, use the base `K-SHOOT` skin to set it back to default, and then
apply the skins' files on top of the default.

So, don't remove the `K-SHOOT` skin folder, or you'll have a bad time.

### Prerequisites

This tool is developed on Python 3.5.1 and is packaged for windows using `pyinstaller`. Only core libraries are leaned upon,
 which are `tkinter`, and `os.path`.