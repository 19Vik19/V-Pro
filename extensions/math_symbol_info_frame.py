import customtkinter as ctk
import math

class FoldableTableFrame(ctk.CTkFrame):
    def __init__(self, master, rows=24, columns=3, **kwargs):
        super().__init__(master, **kwargs)

        self.is_expanded = False

        self.toggle_button = ctk.CTkButton(self, text="▼ Show Greek Letters", command=self.toggle_visibility)
        self.toggle_button.pack(pady=10)

        self.table_frame = TableFrame(self, rows=rows, columns=columns)
        self.table_frame.pack(expand=True, fill="both", padx=10, pady=10)
        self.table_frame.pack_forget()

    def toggle_visibility(self):
        if self.is_expanded:
            self.table_frame.pack_forget()
            self.toggle_button.configure(text="▼ Show Greek Letters")
        else:
            self.table_frame.pack(expand=True, fill="both", padx=10, pady=10)
            self.toggle_button.configure(text="▲ Hide Greek Letters")
        self.is_expanded = not self.is_expanded

class TableFrame(ctk.CTkFrame):
    def __init__(self, master, rows, columns, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(tuple(range(columns)), weight=1)
        self.grid_rowconfigure(tuple(range(rows)), weight=1)

        headers = ["Gr. letter (large)", "Gr. letter (small)", "Gr. name"]
        for j, header in enumerate(headers):
            label = ctk.CTkLabel(self, text=header, font=("Arial", 14, "bold"))
            label.grid(row=0, column=j, padx=5, pady=5, sticky="nsew")

        self.entries = [
            ["Α", "Β", "Γ", "Δ", "Ε", "Ζ", "Η", "Θ", "Ι", "Κ", "Λ", "Μ", "Ν", "Ξ", "Ο", "Π", "Ρ", "Σ", "Τ", "Υ", "Φ", "Χ", "Ψ", "Ω"],
            ["α", "β", "γ", "δ", "ε", "ζ", "η", "θ", "ι", "κ", "λ", "μ", "ν", "ξ", "ο", "π", "ρ", "σ", "τ", "υ", "φ", "χ", "ψ", "ω"],
            ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa", "Lambda", "My", "Ny", "Xi", "Omikron", "Pi", "Rho", "Sigma", "Tau", "Ypsilon", "Phi", "Chi", "Psi", "Omega"]
        ]

        for i in range(columns):
            column = self.entries[i]
            for j in range(rows):
                entry = ctk.CTkButton(self, width=120, height=30, text=column[j], command=lambda x=column[j]: self.add_to_clipboard(x))
                entry.grid(row=j+1, column=i, padx=5, pady=5, sticky="nsew")
                column.append(entry)
            self.entries.append(column)

    def add_to_clipboard(self, text):
        self.clipboard_clear()
        self.clipboard_append(text)

class ShowPI(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989"
        
        self.output_pi = math.pi()
        
        self.label_title = ctk.CTkLabel(self, text="PI - π")
        self.label_title.grid(row=0, column=1)

        self.label = ctk.CTkLabel(self, text="Digits after the decimal point:")
        self.label.grid(row=1, column=0)
        
        self.slider_value = ctk.CTkLabel(self, text="8")
        self.slider_value.grid(row=1, column=1)
        
        self.slider = ctk.CTkSlider(self, from_=0, to=16, command=self.slider_event)
        self.slider.set(8)
        self.slider.grid(row=2, column=0)
        
        self.pilabel = ctk.CTkLabel(self, text=str(round(self.output_pi, 8)))
        self.pilabel.grid(row=2, column=1)
        
        self.copy_button = ctk.CTkButton(self, width=120, height=30, text="Copy", command=self.add_to_clipboard)
        self.copy_button.grid(row=3, column=2, padx=5, pady=5)

        self.copy2_button = ctk.CTkButton(self, width=120, height=30, text="Copy with 1000 digits after the decimal point", command=self.add_to_clipboard_pi)
        self.copy2_button.grid(row=1, column=2, padx=5, pady=5)

    def add_to_clipboard(self):
        self.clipboard_clear()
        self.clipboard_append(self.pilabel.cget("text"))
        
    def add_to_clipboard_pi(self):
        self.clipboard_clear()
        print(self.pi)
        self.clipboard_append(self.pi)

    def slider_event(self, value):
        rounded_value = int(float(value))
        self.actual_pi_value = round(self.output_pi, rounded_value)
        self.pilabel.configure(text=str(self.actual_pi_value))
        self.slider_value.configure(text=str(rounded_value))

class MathSymbolInfoFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, fg_color="transparent", **kwargs)
        
        # Add your widgets and logic for the second frame here
        # For example:
        self.label = ctk.CTkLabel(self, text="Mathematical symbols and further explanations")
        self.label.pack(pady=20)

        self.greek_table_frame = FoldableTableFrame(self)
        self.greek_table_frame.pack(expand=True, fill="both", padx=20, pady=20)

        self.showPi = ShowPI(self)
        self.showPi.pack(fill="both", padx=20, pady=20)
