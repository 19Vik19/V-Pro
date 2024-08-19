import customtkinter 
import os
from PIL import Image

class HomeFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.large_logo = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo_large.png")), size=(500, 150))
        self.home_frame_large_image_label = customtkinter.CTkLabel(self, text="", image=self.large_logo)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
        self.text_home = customtkinter.CTkLabel(self, text="V-PRO is a compact program designed to make numerous everyday tasks easier. It offers a wide range of functions, from simple explanations to complex calculations and code examples, to provide users with comprehensive support.", wraplength=500)
        self.text_home.grid(row=1, column=0, padx=20, pady=10)