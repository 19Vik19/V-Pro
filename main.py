import customtkinter
import os
from PIL import Image
import importlib

from home import HomeFrame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("V-PRO")
        self.geometry("900x450")
        self.minsize(700,450)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(26, 26))
        self.home_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home.png")), size=(20, 20))
        self.under_construction = customtkinter.CTkImage(Image.open(os.path.join(image_path, "under_construction.jpg")), size=(20, 20))
        
        self.load_extensions()
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(len(self.extensions)+2, weight=1)
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  V-PRO", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.home_frame = HomeFrame(self)
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.buttons = []
        for i, (name, _) in enumerate(self.extensions, start=1):
            button = customtkinter.CTkButton(
                self.navigation_frame,
                corner_radius=0,
                height=40,
                border_spacing=10,
                text=name,
                fg_color="transparent",
                text_color=("gray10", "gray90"),
                hover_color=("gray70", "gray30"),
                image=self.under_construction, 
                anchor="w",
                command=lambda x=name: self.frame_button_event(x)
            )
            button.grid(row=i+1, column=0, sticky="ew")
            self.buttons.append(button)

        self.frames = {"home": self.home_frame}
        for name, frame_class in self.extensions:
            self.frames[name] = frame_class(self)

        self.select_frame_by_name("home")

    def load_extensions(self):
        self.extensions = []
        extensions_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "extensions")
        for filename in os.listdir(extensions_path):
            if filename.endswith("_frame.py"):
                try:
                    module_name = f"extensions.{filename[:-3]}"
                    module = importlib.import_module(module_name)
                    class_name = ''.join(word.capitalize() for word in filename[:-3].split('_'))
                    frame_class = getattr(module, class_name)
                    self.extensions.append((filename[:-9].replace('_', ' ').title(), frame_class))
                except:
                    print(f"Importing {filename} failed!")
            else:
                print(f"{filename} is not an extension or is not formated correctly!")

    def select_frame_by_name(self, name):
        for button in self.buttons:
            button.configure(fg_color="transparent")
        
        if name in self.frames:
            for frame in self.frames.values():
                frame.grid_forget()
            self.frames[name].grid(row=0, column=1, sticky="nsew")
            
            if name != "home":
                button_index = [extension[0] for extension in self.extensions].index(name)
                self.buttons[button_index].configure(fg_color=("gray75", "gray25"))
        else:
            self.home_button.configure(fg_color=("gray75", "gray25"))
            self.home_frame.grid(row=0, column=1, sticky="nsew")

    def home_button_event(self):
        self.select_frame_by_name("home")
        
    def frame_button_event(self, name):
        self.select_frame_by_name(name)


if __name__ == "__main__":
    app = App()
    app.mainloop()