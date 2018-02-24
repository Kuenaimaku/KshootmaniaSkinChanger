import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import os.path
import shutil
from shutil import copytree
from distutils.dir_util import copy_tree

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.minsize(width=642, height=500)
        master.maxsize(width=642, height=500)
        self.resize = 640, 360
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #Text Frame - Directory
        self.text_frame = ttk.Frame(self, width=500, height=25)
        self.text_frame.grid()
        self.text_frame.grid_propagate(False)

        #DropDown
        self.list = self.get_immediate_subdirectories('skins')
        self.current_skin = tk.StringVar()
        self.current_skin.trace("w", self.option_changed)
        self.drop = ttk.OptionMenu(self.text_frame, self.current_skin, "K-SHOOT", *self.list)
        self.drop.configure(width=75)
        self.drop.grid(row=0, column=0, sticky="nsew", padx=10, pady=0)

        self.browse = ttk.Button(self, text='Set As Skin', command=self.set_skin)
        self.browse.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        #ImageGallery Frame
        self.image_index = 0
        self.image_paths = self.get_immediate_files('skins/{}'.format(self.current_skin.get()))
        self.preview_image = 'skins/{}/imgs/standby.jpg'.format(self.current_skin.get())
        self.image_frame = tk.Frame(self, width=640, height=390)
        self.image_frame.grid(sticky="nw", row=1, column=0, columnspan=3)
        self.image_frame.grid_propagate(False)

        #ImageGallery Image
        self.image_name = os.path.basename(self.preview_image)
        self.image_name = os.path.splitext(self.image_name)[0]
        self.image = Image.open(self.preview_image)
        self.image = self.image.resize(self.resize, Image.ANTIALIAS)
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.image_gallery = ttk.Label(self.image_frame, image=self.tk_image, text=self.image_name, compound='top', background='MediumPurple1')
        self.image_gallery.grid(row=1, column=0, columnspan=3, sticky="nw", padx=0, pady=0)

        #GalleryControl Frame
        self.gallery_control_frame = tk.Frame(self, width=652, height=25)
        self.gallery_control_frame.grid(sticky="nsew", row=2, column=0, columnspan=3)
        self.gallery_control_frame.grid_propagate(False)

        self.previous_image = ttk.Button(self.gallery_control_frame, text='< Previous ', command=lambda: self.change_index(direction="Previous"), width=51)
        self.previous_image.grid(row=0, column=0)
        self.next_image = ttk.Button(self.gallery_control_frame, text=' Next >', command=lambda: self.change_index(direction="Next"), width=52)
        self.next_image.grid(row=0, column=1, padx=3)

        self.credits = ttk.Label(self, text='Created by Kuenaimaku')
        self.credits.grid(row=3, column=0, columnspan=2, sticky="nws", padx=10, pady=10)


    def copydir(self, source, dest, indent=0):
        """Copy a directory structure overwriting existing files"""
        for root, dirs, files in os.walk(source):
            if not os.path.isdir(root):
                os.makedirs(root)

            for file in files:
                rel_path = root.replace(source, '').lstrip(os.sep)
                dest_path = os.path.join(dest, rel_path)

                if not os.path.isdir(dest_path):
                    os.makedirs(dest_path)

                shutil.copyfile(os.path.join(root, file), os.path.join(dest_path, file))


    def set_skin(self):
        if os.path.isdir('cache'):
            shutil.rmtree('cache')
        if os.path.isdir('imgs'):
            shutil.rmtree('imgs')
        if os.path.isdir('se'):
            shutil.rmtree('se')
        os.mkdir('cache')
        self.copydir('skins/K-SHOOT/imgs', 'imgs')
        self.copydir('skins/K-SHOOT/se', 'se')
        if self.current_skin.get() == 'K-SHOOT':
            pass
        else:
            self.copydir('skins/{}/imgs'.format(self.current_skin.get()), 'imgs')
            self.copydir('skins/{}/se'.format(self.current_skin.get()), 'se')

    def get_immediate_subdirectories(self, a_dir):
        return [name for name in os.listdir(a_dir)
                if os.path.isdir(os.path.join(a_dir, name))]

    def get_immediate_files(self, a_dir):
        return [name for name in os.listdir(a_dir)
                if os.path.isfile(os.path.join(a_dir, name))]

    def reload_image(self, path):
        self.preview_image = path
        self.image_name = os.path.basename(self.preview_image)
        self.image_name = os.path.splitext(self.image_name)[0]
        self.image = Image.open(self.preview_image)
        self.image = self.image.resize(self.resize, Image.ANTIALIAS)
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.image_gallery = ttk.Label(self.image_frame, image=self.tk_image, text=self.image_name, compound='top', background='MediumPurple1')
        self.image_gallery.grid(row=1, column=0, columnspan=3, sticky="nw", padx=0, pady=0)


    def option_changed(self, *args):
        self.image_paths = self.get_immediate_files('skins/{}'.format(self.current_skin.get()))
        if len(self.image_paths) > 0:
            self.image_index = 0
            self.reload_image('skins/{}/{}'.format(self.current_skin.get(), self.image_paths[self.image_index]))
        else:
            self.reload_image('skins/{}/imgs/standby.jpg'.format(self.current_skin.get()))

    def change_index(self, direction):
        if direction == "Next" and self.image_index < len(self.image_paths)-1:
            self.image_index += 1
        elif direction == "Next" and self.image_index >= len(self.image_paths)-1:
            self.image_index = 0

        if direction == "Previous" and self.image_index > 0:
            self.image_index -= 1
        elif direction == "Previous" and self.image_index <= 0:
            self.image_index = len(self.image_paths)-1
        if len(self.image_paths)>0:
            self.reload_image('skins/{}/{}'.format(self.current_skin.get(), self.image_paths[self.image_index]))
        else:
            self.reload_image('skins/{}/imgs/standby.jpg'.format(self.current_skin.get()))


root = tk.Tk()
root.title("K-SHOOT MANIA Skin Swapper")
#root.iconbitmap(r'drill.ico')
root.resizable(width=False, height=False)
app = Application(master=root)

app.mainloop()

