import tkinter as tk
from tkinter import messagebox, ttk

class EmployeeManagementSystem:
    # 1. FIX: Changed _init_ to __init__
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("800x600")
        self.root.configure(bg="#f8f9fa")

        self.employees = []  # To store employee data

        title_label = tk.Label(root, text="Employee Management System", font=("Arial", 20, "bold"), bg="#007bff", fg="white", pady=10)
        title_label.pack(fill="x")

        # Input Frame
        input_frame = tk.Frame(root, bg="#f8f9fa", padx=20, pady=10)
        input_frame.pack(fill="x")

        # Labels and Entry Widgets
        tk.Label(input_frame, text="Name:", font=("Arial", 12), bg="#f8f9fa").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_name = tk.Entry(input_frame, width=25, font=("Arial", 12))
        self.entry_name.grid(row=1, column=0, padx=5, pady=5)

        tk.Label(input_frame, text="Age:", font=("Arial", 12), bg="#f8f9fa").grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.spin_age = tk.Spinbox(input_frame, from_=18, to=100, font=("Arial", 12), width=5)
        self.spin_age.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Department:", font=("Arial", 12), bg="#f8f9fa").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.entry_department = tk.Entry(input_frame, width=25, font=("Arial", 12))
        self.entry_department.grid(row=1, column=2, padx=5, pady=5)

        # Buttons Frame
        btn_frame = tk.Frame(root, bg="#f8f9fa", pady=10)
        btn_frame.pack(fill="x")

        tk.Button(btn_frame, text="Add Employee", command=self.add_employee, bg="#28a745", fg="white", font=("Arial", 12), width=15).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Update Employee", command=self.update_employee, bg="#ffc107", fg="black", font=("Arial", 12), width=15).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Delete Employee", command=self.delete_employee, bg="#dc3545", fg="white", font=("Arial", 12), width=15).pack(side="left", padx=5)

        # Search Frame
        search_frame = tk.Frame(root, bg="#f8f9fa", pady=10)
        search_frame.pack(fill="x")

        self.entry_search = tk.Entry(search_frame, width=40, font=("Arial", 12))
        self.entry_search.pack(side="left", padx=10)
        tk.Button(search_frame, text="Search Employee", command=self.search_employee, bg="#17a2b8", fg="white", font=("Arial", 12)).pack(side="left", padx=10)

        # Table Frame
        table_frame = tk.Frame(root, bg="#f8f9fa")
        table_frame.pack(fill="both", expand=True)

        columns = ("Name", "Age", "Department")
        self.table = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")
        self.table.heading("Name", text="Name")
        self.table.heading("Age", text="Age")
        self.table.heading("Department", text="Department")
        self.table.pack(fill="both", expand=True)
        
        # Bind double-click event to load selected employee data into inputs
        self.table.bind("<<TreeviewSelect>>", self.load_selected_employee)

    def load_selected_employee(self, event):
        """Loads data of the selected employee into the input fields."""
        selected_item = self.table.selection()
        if selected_item:
            # Get the values from the selected row
            values = self.table.item(selected_item, 'values')
            if values:
                # Clear existing inputs
                self.clear_inputs()
                
                # Insert new values
                self.entry_name.insert(0, values[0])
                self.spin_age.delete(0, tk.END) # Spinbox requires delete then insert
                self.spin_age.insert(0, values[1])
                self.entry_department.insert(0, values[2])


    def add_employee(self):
        name = self.entry_name.get()
        age = self.spin_age.get()
        department = self.entry_department.get()

        if not name or not age or not department:
            messagebox.showerror("Error", "All fields are required!")
            return

        self.employees.append((name, age, department))
        self.refresh_table()
        self.clear_inputs()
        messagebox.showinfo("Success", "Employee added successfully!")

    def update_employee(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an employee to update.")
            return

        name = self.entry_name.get()
        age = self.spin_age.get()
        department = self.entry_department.get()

        if not name or not age or not department:
            messagebox.showerror("Error", "All fields are required!")
            return

        index = self.table.index(selected_item)
        self.employees[index] = (name, age, department)
        self.refresh_table()
        self.clear_inputs()
        messagebox.showinfo("Success", "Employee updated successfully!")

    def delete_employee(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an employee to delete.")
            return

        index = self.table.index(selected_item)
        # Ensure the table index matches the list index before deletion
        del self.employees[index]
        self.refresh_table()
        messagebox.showinfo("Success", "Employee deleted successfully!")

    def search_employee(self):
        search_query = self.entry_search.get().lower()
        if not search_query:
            # If search is empty, show all data
            self.refresh_table() 
            return

        # Filter employees whose name contains the search query
        filtered = [emp for emp in self.employees if search_query in emp[0].lower()]
        self.refresh_table(filtered)

    def refresh_table(self, data=None):
        # Clear all existing entries in the table
        for item in self.table.get_children():
            self.table.delete(item)

        # Insert new data
        data = data if data is not None else self.employees
        for emp in data:
            self.table.insert("", "end", values=emp)

    def clear_inputs(self):
        self.entry_name.delete(0, tk.END)
        self.spin_age.delete(0, tk.END)
        self.spin_age.insert(0, 18) # Reset age to default minimum
        self.entry_department.delete(0, tk.END)

# 2. FIX: Changed "_main_" to "__main__"
if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementSystem(root)
    root.mainloop()