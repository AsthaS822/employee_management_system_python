# 📚 Employee Management System

## Project Overview

This is a simple desktop application for managing employee records, built using **Python** and the **Tkinter** library. It allows users to perform basic **CRUD** (Create, Read, Update, Delete) operations on employee data, which is stored in memory during runtime.

### Key Features

* **Add Employee:** Quickly add new employee records with name, age, and department.
* **View Table:** Displays all current employee data in a clean, scrollable table view (`ttk.Treeview`).
* **Update Records:** Select an employee from the table and modify their details.
* **Delete Records:** Remove employees from the list.
* **Search Functionality:** Filter employees by name.

***

## 💻 Technical Stack

| Category | Technology |
| :--- | :--- |
| **Language** | Python 3.x |
| **Framework** | Tkinter (Standard Python GUI Library) |
| **Styling** | ttk (Themed Tkinter Widgets) |

***

## 🚀 Getting Started

Follow these steps to get the application up and running on your local machine.

### Prerequisites

You need a working Python environment; **Anaconda/Miniconda** should be installed.

1.  **Activate your environment** (if not already active):
    ```bash
    conda activate base
    # OR if you created a separate environment, use that environment name
    ```

### Installation

No external libraries (like `requests` or `pandas`) are needed, as this project uses the standard **Tkinter** library, which is included with most Python installations (including Anaconda).

1.  **Clone the Repository:**
    ```bash
    git clone [YOUR_GITHUB_REPO_LINK]
    cd EmployeeManagementSystemPython
    ```
2.  **Ensure Tkinter is available:** Tkinter is usually included, but if you get an error, you may need to install it manually:
    ```bash
    conda install tk
    ```

### Running the Application

Execute the main Python script directly from your terminal:

```bash
python employeemanagementsystem.py
