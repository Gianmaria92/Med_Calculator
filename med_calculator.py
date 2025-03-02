# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 18:51:16 2025

@author: user
"""

import tkinter as tk
from tkinter import ttk
import numpy as np

class MedicationCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medication Dosage Calculator")
        self.root.geometry("600x500")
        self.num_elements = 13


        # Add this line to set the window icon:
        self.root.iconbitmap('med_calculator.ico')  # On Windows
        # OR for cross-platform support:
        try:
            self.root.iconbitmap('path_to_your_icon.ico')
        except:
            # For non-Windows platforms
            pass
        
        
        # Create a main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="Medication Dosage Calculator", font=("Arial", 16, "bold"))
        title_label.pack(pady=(0, 20))
        
        # Active Ingredient Selection
        ingredient_frame = ttk.Frame(main_frame)
        ingredient_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(ingredient_frame, text="Active Ingredient:").pack(side=tk.LEFT, padx=(0, 10))
        
        # Sample list of active ingredients (can be expanded)
        self.ingredients = [
            "Dexdemetomidina",
            "Acetaminophen",
            "Amoxicillin",
            "Ibuprofen",
            "Azithromycin",
            "Cephalexin",
            "Doxycycline",
            "Metformin"
        ]
        
        self.ingredient_var = tk.StringVar()
        ingredient_dropdown = ttk.Combobox(ingredient_frame, textvariable=self.ingredient_var, values=self.ingredients, width=30)
        ingredient_dropdown.pack(side=tk.LEFT)
        ingredient_dropdown.current(0)  # Set default selection
        
        # Patient Weight Entry
        weight_frame = ttk.Frame(main_frame)
        weight_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(weight_frame, text="Patient Weight (kg):").pack(side=tk.LEFT, padx=(0, 10))
        
        self.weight_var = tk.StringVar()
        weight_entry = ttk.Entry(weight_frame, textvariable=self.weight_var, width=10)
        weight_entry.pack(side=tk.LEFT)
        
        # Number of Vials Entry
        vials_frame = ttk.Frame(main_frame)
        vials_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(vials_frame, text="Number of vials:").pack(side=tk.LEFT, padx=(0, 10))
        
        self.vials_var = tk.StringVar()
        vials_entry = ttk.Entry(vials_frame, textvariable=self.vials_var, width=10)
        vials_entry.pack(side=tk.LEFT)
        self.vials_var.set("1")  # Default value
        
        
        # Calculate Button
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=20)
        
        calculate_button = ttk.Button(button_frame, text="Calculate Dosage", command=self.calculate_dosage)
        calculate_button.pack()
        
        # Results Section
        self.results_frame = ttk.LabelFrame(main_frame, text="Results", padding="10")
        self.results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollable text widget for results
        self.results_text = tk.Text(self.results_frame, height=15, width=70, wrap=tk.WORD)
        self.results_text.pack(fill=tk.BOTH, expand=True)
        
    def calculate_dosage(self):
        # Clear previous results
        self.results_text.delete(1.0, tk.END)
        n_elements = self.num_elements
        try:
            # Get the patient weight
            weight = float(self.weight_var.get())
            # Get number of vials
            try:
               num_vials = int(self.vials_var.get())
               if num_vials <= 0:
                   self.results_text.insert(tk.END, "Error: Number of vials must be a positive integer.")
                   return
            except ValueError:
               self.results_text.insert(tk.END, "Error: Number of vials must be a valid integer.")
               return
            
            if weight <= 0:
                self.results_text.insert(tk.END, "Error: Weight must be greater than zero.")
                return
                
            # Get selected ingredient
            ingredient = self.ingredient_var.get()
            
            if ingredient == "Dexdemetomidina":
                
                # Generate a calculated vector based on weight and ingredient
                # This is a sample calculation - in a real application, this would use proper medical formulas
                calculated_vector = self.generate_calculated_vector(weight, ingredient, num_vials)
                
                # Generate fixed vector (0.2 to 1.4 in steps of 0.1)
                fixed_vector = np.linspace(0.2, 1.4, n_elements).round(1)
                
                # Display results
                self.results_text.insert(tk.END, f"Active Ingredient: {ingredient}\n")
                self.results_text.insert(tk.END, f"Patient Weight: {weight} kg\n\n")
                self.results_text.insert(tk.END, "Calculated Dosage Vector and Reference Values:\n\n")
                
                # Display the vectors side by side
                self.results_text.insert(tk.END, "| Calculated Dosage | Reference Value |\n")
                self.results_text.insert(tk.END, "|------------------|----------------|\n")
                
                for calc, fixed in zip(calculated_vector, fixed_vector):
                    self.results_text.insert(tk.END, f"| {calc:.2f} ml/h        | {fixed:.1f} mcg/kg/min        |\n")
            else: 
                self.results_text.insert(tk.END, f"{ingredient} not supported yet\n")
                
        except ValueError:
            self.results_text.insert(tk.END, "Error: Please enter a valid number for weight.")
    
    def generate_calculated_vector(self, weight, ingredient, num_vials):
        """
        Generate a vector of calculated dosages based on patient weight and active ingredient.
        
        This is a simplified example - in a real application, you would use proper medical formulas
        specific to each medication. The current implementation uses a basic formula that varies 
        slightly by ingredient.
        """
        # Number of elements to match the fixed vector (0.2 to 1.4 in steps of 0.1)
        n_elements = self.num_elements
        
        # Base multiplier that depends on the ingredient (would be based on actual medical guidelines)
        if ingredient == "Acetaminophen":
            base_multiplier = 0.15
        elif ingredient == "Amoxicillin":
            base_multiplier = 0.12
        elif ingredient == "Ibuprofen":
            base_multiplier = 0.10
        elif ingredient == "Azithromycin":
            base_multiplier = 0.08
        elif ingredient == "Cephalexin":
            base_multiplier = 0.14
        elif ingredient == "Doxycycline":
            base_multiplier = 0.11
        elif ingredient == "Metformin":
            base_multiplier = 0.09
        elif ingredient == "Dexdemetomidina":
            base_multiplier = 1/(num_vials * 4) 
        else:
            base_multiplier = 0.10
        
        # Generate a vector where each value is calculated based on weight and ingredient
        # and scaled to roughly match the range of the fixed vector
        calculated_vector = np.linspace(0.2, 1.4, n_elements, endpoint=True) * weight * base_multiplier
        
        return calculated_vector

def main():
    root = tk.Tk()
    app = MedicationCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()