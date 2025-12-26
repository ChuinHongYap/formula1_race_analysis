import tkinter as tk
import pandas as pd
import os

allRace_folder = './races_all'

class RaceViewer:
    def __init__(self, root, folder_path):
        self.root = root
        self.root.title("F1 Race Data Viewer")
        self.folder_path = folder_path
        self.csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
        self.current_index = 0
        self.dataframes = {}
        
        # Load all CSV files
        for csv_file in self.csv_files:
            file_path = os.path.join(folder_path, csv_file)
            self.dataframes[csv_file] = pd.read_csv(file_path, encoding='latin1')
        
        # Create GUI elements
        self.label = tk.Label(root, text="", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.text_widget = tk.Text(root, wrap=tk.NONE, width=100, height=30)
        self.text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Scrollbars
        h_scroll = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=self.text_widget.xview)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        v_scroll = tk.Scrollbar(root, orient=tk.VERTICAL, command=self.text_widget.yview)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_widget.config(xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)
        
        # Navigation buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        
        self.prev_button = tk.Button(button_frame, text="<", command=self.prev_csv, width=10)
        self.prev_button.pack(side=tk.LEFT, padx=5)
        
        self.next_button = tk.Button(button_frame, text=">", command=self.next_csv, width=10)
        self.next_button.pack(side=tk.LEFT, padx=5)
        
        # Bind arrow keys
        self.root.bind('<Left>', lambda event: self.prev_csv())
        self.root.bind('<Right>', lambda event: self.next_csv())
        
        # Display first CSV
        if self.csv_files:
            self.display_csv()
    
    def display_csv(self):
        if not self.csv_files:
            self.label.config(text="No CSV files found")
            return
        
        current_file = self.csv_files[self.current_index]
        self.label.config(text=f"File {self.current_index + 1}/{len(self.csv_files)}: {current_file}")
        
        df = self.dataframes[current_file]
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(1.0, df.to_string())
    
    def prev_csv(self):
        if self.csv_files:
            self.current_index = (self.current_index - 1) % len(self.csv_files)
            self.display_csv()
    
    def next_csv(self):
        if self.csv_files:
            self.current_index = (self.current_index + 1) % len(self.csv_files)
            self.display_csv()

# Create and run the application
root = tk.Tk()
app = RaceViewer(root, allRace_folder)
root.mainloop()