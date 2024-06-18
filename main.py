# "C:\LukasADVACAM\Data" is the path to the folder where the data is stored

import tkinter as tk
from tkinter import *


from data_manager import DataManager

# ----------------------------------------------#
# ----------------- CONSTANTS--------------------#
# ----------------------------------------------#
ROOT_BACKGROUND = "white"
LOGO_FRAME_BACKGROUND = "#20B2AA"
PROCESSING_FRAME_BACKGROUND = "#E0EEEE"
DATA_FRAME_BACKGROUND = "#E0EEEE"
IMAGE_FRAME_BACKGROUND = "#E0EEEE"
EXPORT_FRAME_BACKGROUND = "#E0EEEE"

LOGO_FONT = ('Helvetica', 20, "bold")
FRAME_LABELS = ('Helvetica', 10, "bold")
AUTHOR_LABEL = ('Helvetica', 8, "italic")

FRAME_SUBLABEL_1 = ('Helvetica', 10)
BUTTON_LABEL = ('Helvetica', 10)

# ----------------------------------------------#
# ----------------- UI-SETUP--------------------#
# ----------------------------------------------#

def main():

    root = Tk()                         # create root window
    root.title("FLAT_XRF")              # set title of the window
    root.maxsize(850, 850)              # set maximum size of the window
    root.config(bg=ROOT_BACKGROUND)     # set background color of the window
    

    # ------------------------#
    # ----- FRAMES SETUP -----#
    # ------------------------#
    # data processing selection frame with bools for processing steps
    processing_frame = Frame(root, width=300, height=100, bg=PROCESSING_FRAME_BACKGROUND, highlightbackground="black", highlightthickness=1)  
    processing_frame.grid(row=1, column=0, padx=10, pady=5) 
    
    # data frame for data load, delete and run the visualization
    data_frame = Frame(root, width=300, height=560, bg=DATA_FRAME_BACKGROUND, highlightbackground="black", highlightthickness=1)  
    data_frame.grid(row=2, column=0, rowspan=3, padx=10, pady=5)                          

    # logo frame for the SW name and image
    logo_frame = Frame(root, width=500, height=100, bg=LOGO_FRAME_BACKGROUND)   
    logo_frame.grid(row=1, column=1, padx=10, pady=5)

    # image frame - main visualization window
    image_frame = Frame(root, width=500, height=500, bg=IMAGE_FRAME_BACKGROUND, highlightbackground="black", highlightthickness=2)  
    image_frame.grid(row=2, column=1, padx=10, pady=5)                

    # export fram - options for image save or other postprocessing? 
    export_frame = Frame(root, width=500, height=50, bg=EXPORT_FRAME_BACKGROUND, highlightbackground="black", highlightthickness=1)  
    export_frame.grid(row=3, column=1, padx=10, pady=5)                            

    Label(logo_frame, text="FLAT_XRF", font=LOGO_FONT, bg=LOGO_FRAME_BACKGROUND).place(relx=0.15, rely=0.20, anchor=CENTER)
    Label(logo_frame, text="lukasdekanovsky@gmail.com", font=AUTHOR_LABEL, bg=LOGO_FRAME_BACKGROUND).place(relx=0.84, rely=0.85, anchor=CENTER)
    Label(processing_frame, text="Processing selection", font=FRAME_LABELS, bg=PROCESSING_FRAME_BACKGROUND).place(relx=0.5, rely=0.13, anchor=CENTER)
    Label(data_frame, text="Data", font=FRAME_LABELS, bg=DATA_FRAME_BACKGROUND).place(relx=0.5, rely=0.02, anchor=CENTER)
    Label(image_frame, text="Image", font=FRAME_LABELS, bg=IMAGE_FRAME_BACKGROUND).place(relx=0.5, rely=0.022, anchor=CENTER)
    Label(export_frame, text="Export", font=FRAME_LABELS, bg=EXPORT_FRAME_BACKGROUND).place(relx=0.05, rely=0.5, anchor=CENTER)


    # ----------------------------#
    # ----- PROCESSING FRAME -----#
    # ----------------------------#
    selection_2D_image = BooleanVar()
    selection_2D_CT_scan = BooleanVar()
    selection_FF = BooleanVar()
    selection_4 = BooleanVar()

    Checkbutton(processing_frame, text="2D image", variable=selection_2D_image, onvalue=True, offvalue=False).place(relx=0.10, rely=0.4, anchor=W)
    Checkbutton(processing_frame, text="2D CT scan - gif", variable=selection_2D_CT_scan, onvalue=True, offvalue=False).place(relx=0.10, rely=0.8, anchor=W)
    Checkbutton(processing_frame, text="Flat field", variable=selection_FF, onvalue=True, offvalue=False).place(relx=0.6, rely=0.4, anchor=W)
    Checkbutton(processing_frame, text="Option 4", variable=selection_4, onvalue=True, offvalue=False).place(relx=0.6, rely=0.8, anchor=W)
    # ---> selection_2D_image.get()  ZISKAVAME TRUE/FALSE HODNOTU Z CHEKCBOXU
    
    # ----------------------------#
    # ---------- CLASSES ---------#
    # ----------------------------#
    # class instances as managers
    data_manager = DataManager()



    # ----------------------------#
    # -------- DATA FRAME --------#
    # ----------------------------#
    
    # LOADED DATA listbox
    Label(data_frame, text="Loaded data", font=FRAME_SUBLABEL_1, bg=DATA_FRAME_BACKGROUND).place(relx=0.16, rely=0.08, anchor=CENTER)

    loaded_data_scrollbar = tk.Scrollbar(data_frame)
    loaded_data_listbox = tk.Listbox(data_frame, yscrollcommand=loaded_data_scrollbar.set, width=30, height=10)
    loaded_data_listbox.place(relx=0.42, rely=0.25, width=230, anchor=CENTER)
    loaded_data_scrollbar.place(relx=0.9, rely=0.25, anchor=CENTER, relheight=0.3)

    Button(data_frame, text="Load data", font=BUTTON_LABEL, command = lambda: data_manager.load_data()).place(relx=0.15, rely=0.44, anchor=CENTER)
    Button(data_frame, text="Delete data", font=BUTTON_LABEL, command=lambda: data_manager.delete_data()).place(relx=0.41, rely=0.44, anchor=CENTER)

    # PROCESSED data listbox
    Label(data_frame, text="Processed data", font=FRAME_SUBLABEL_1, bg=DATA_FRAME_BACKGROUND).place(relx=0.19, rely=0.53, anchor=CENTER)

    processed_data_scrollbar = tk.Scrollbar(data_frame)
    processed_data_listbox = tk.Listbox(data_frame, yscrollcommand=loaded_data_scrollbar.set, width=30, height=10)
    processed_data_listbox.place(relx=0.42, rely=0.7, width=230, anchor=CENTER)
    processed_data_scrollbar.place(relx=0.9, rely=0.7, anchor=CENTER, relheight=0.3)




    root.update()                       # update the window continuously
    root.mainloop()                     # start the main loop of the window


if __name__ == "__main__":
    main()