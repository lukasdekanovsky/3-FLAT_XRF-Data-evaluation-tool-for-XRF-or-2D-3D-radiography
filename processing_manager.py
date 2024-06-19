from tkinter import filedialog
import tkinter as tk
import shutil
import os
import webbrowser
import subprocess
import numpy as np
import matplotlib.pyplot as plt

class ProcessingManager():


    def __init__(self, root, data_a, data_b, results_listbox):
        self.root = root
        self.data_a = data_a
        self.data_b = data_b
        self.results_listbox = results_listbox

        self.data_a_path = "./data_a/"
        self.data_b_path = "./data_b/"
        self.results_path = "./results/"

    
    def update_processed_data(self):
        # UPDATE LISTBOX FUNCTION
        self.results_listbox.delete(0, tk.END)
        for file_name in os.listdir(self.results_path):
            self.results_listbox.insert(tk.END, file_name)
        self.results_listbox.update()

    def open_file(self):
        index = self.results_listbox.curselection()[0]                      # Get selected line index
        filename = self.results_listbox.get(index)                          # Get the line's text
        file_path = os.path.abspath(os.path.join(self.results_path, filename))               # Get the absolute file path
        
        if os.path.isfile(file_path):                                       # Check if file exists
            os.startfile(file_path)                                         # Open the file in default program
        else:
            print(f"File {file_path} does not exist.")
        
        
            

    def process_data(self, selection_2D_image, selection_2D_CT_scan, selection_FF, selection_4):
        # DATA processing according to selection
        processes = [selection_2D_image, selection_2D_CT_scan, selection_FF, selection_4]
        if selection_2D_image.get():
            print("Processing 2D image")
            self.proces_2D_image()
        elif selection_2D_CT_scan.get():
            print("Processing 2D CT scan")
            self.proces_2D_CT_scan()
        elif selection_FF.get():
            print("Processing FF")
            self.proces_FF()
        elif selection_4.get():
            print("Processing option 4")
            self.proces_4()
        

    def proces_2D_image(self):
        # ---------------------- File selection logic  ------------------------#
        try:                                                                    # file selection, depending which listbox A or B was selected
            selected_file = self.data_a.get(self.data_a.curselection())            
        except:
            selected_file = self.data_b.get(self.data_b.curselection())
        
        print("Processing 2D image: ", selected_file)
        
        if os.path.exists(os.path.join(self.data_a_path, selected_file)):
            file_path = os.path.join(self.data_a_path, selected_file)           # defining the file path
            print(f"Processing from file A")
        else:
            file_path = os.path.join(self.data_b_path, selected_file)
            print(f"Processing from file B")

        # ---------------------- 2D image processing script ------------------------#
        pixel_values = np.loadtxt(file_path)                                    # load pixel values from the file
        fig, ax = plt.subplots()                                                # create a figure and axis
        
        img = ax.imshow(pixel_values, cmap='viridis')                           # plot the pixel values as an image
        cbar = fig.colorbar(img)                                                # add a colorbar to the image
        
        # adjust th evisual properties of the graph
        ax.set_title('Pixel Values')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        cbar.set_label('Intensity')
        
        # ---------------------- File needs to be saved in results listbox  ------------------------#
        # Save processed file as a .png
        save_path = os.path.join(self.results_path, selected_file.split('.')[0] + '.png')
        plt.savefig(save_path)
        print(f"Processed file saved as {save_path}")

        # ------------------------------------------------------------------------- # 
        # show plot after plt.savefig NEEDED -> figure shown cannot be reused in code
        plt.show()
        self.update_processed_data()


    def proces_2D_CT_scan(self):
        ...

    def proces_FF(self):
        ...

    def proces_4(self):
        ...