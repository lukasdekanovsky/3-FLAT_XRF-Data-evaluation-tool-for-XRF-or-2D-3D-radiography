from tkinter import filedialog
import tkinter as tk
import shutil
import os

class DataManager():

    def __init__(self, root):
        self.data_a_path = "./data_a/"
        self.data_b_path = "./data_b/"
        self.results_path = "./results/"
        self.root = root

    # --------------------------------------------------------------------#
    # --------------------- DATA LOAD/DELETE------------------------------#
    # --------------------------------------------------------------------#

    def update_listbox(self, loaded_listbox, path):
        # UPDATE LISTBOX FUNCTION
        loaded_listbox.delete(0, tk.END)
        for file_name in os.listdir(path):
            loaded_listbox.insert(tk.END, file_name)
        loaded_listbox.update()

    
    def load_data_a(self, loaded_data_a_listbox):
        print("A Loading data procedure started")
        file_paths = filedialog.askopenfilenames(initialdir = "/", title = "Select data A folder", filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        if file_paths: # if user selected a folder
            destination_path = self.data_a_path
            for file_path in file_paths:
                file_name = file_path.split("/")[-1]
                shutil.copy(file_path, destination_path + file_name) 
            
            # UPDATE LISTBOX FUNCTION
            self.update_listbox(loaded_data_a_listbox, self.data_a_path)

    def load_data_b(self, loaded_data_b_listbox):
        print("B Loading data procedure started")
        file_paths = filedialog.askopenfilenames(initialdir = "/", title = "Select data A folder", filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        if file_paths: # if user selected a folder
            destination_path = self.data_b_path
            for file_path in file_paths:
                file_name = file_path.split("/")[-1]
                shutil.copy(file_path, destination_path + file_name)
            
            # UPDATE LISTBOX FUNCTION
            self.update_listbox(loaded_data_b_listbox, self.data_b_path)

    def delete_data_a(self, loaded_data_a_listbox):
        print("A Deleting data procedure started")
        file_list = os.listdir(self.data_a_path)
        for file_name in file_list:
            file_path = os.path.join(self.data_a_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)

        # UPDATE LISTBOX FUNCTION
        self.update_listbox(loaded_data_a_listbox, self.data_a_path)

    def delete_data_b(self, loaded_data_b_listbox):
        print("B Deleting data procedure started")
        file_list = os.listdir(self.data_b_path)
        for file_name in file_list:
            file_path = os.path.join(self.data_b_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
        
        # UPDATE LISTBOX FUNCTION
        self.update_listbox(loaded_data_b_listbox, self.data_a_path)

    
    