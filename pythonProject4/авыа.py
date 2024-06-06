import tkinter as tk
from tkinter import ttk, messagebox

# Function to apply styling to widgets
def apply_styles():
    # Define colors
    bg_color = "#f0f0f0"  # Light gray background
    fg_color = "#333333"  # Dark gray foreground
    button_bg = "#008c08"  # Green button background
    button_fg = "white"    # White button foreground

    # Apply styles to widgets
    summary_frame.configure(bg=bg_color)
    clients_label.configure(bg=bg_color, fg=fg_color, font=("Arial", 12))
    detail_label.configure(bg=bg_color, fg=fg_color, font=("Arial", 12))
    select_client_button.configure(bg=button_bg, fg=button_fg, font=("Arial", 10))
    selected_client_frame.configure(bg="white", bd=2, relief=tk.GROOVE)
    selected_client_text.configure(bg="white", fg=fg_color, font=("Arial", 12))
    parts_tree.configure(bg="white", fg=fg_color, font=("Arial", 10))
    button_frame.configure(bg=bg_color)
    add_detail_button.configure(bg=button_bg, fg=button_fg, font=("Arial", 10))
    remove_button.configure(bg="#b80000", fg=button_fg, font=("Arial", 10))
    selected_parts_listbox.configure(bg="white", fg=fg_color, font=("Arial", 10))

# Create summary tab
def create_summary_tab(tab, tree):
    global summary_frame, clients_label, detail_label, select_client_button
    global selected_client_frame, selected_client_text, parts_tree, button_frame
    global add_detail_button, remove_button, selected_parts_listbox

    # Create frame for summary tab
    summary_frame = tk.Frame(tab)
    summary_frame.pack(expand=True, fill='both')

    # Create label for selecting clients
    clients_label = tk.Label(summary_frame, text="Выберите клиента для формирования заказа:", padx=10, pady=10)
    clients_label.pack()

    # Create button for selecting client
    select_client_button = tk.Button(summary_frame, text="Выбрать клиента", command=select_client)
    select_client_button.pack()

    # Create frame for displaying selected client and problem
    selected_client_frame = tk.Frame(summary_frame, bd=2, relief=tk.GROOVE)
    selected_client_frame.pack(fill=tk.BOTH, padx=10, pady=10)

    # Create text widget for displaying selected client and problem
    selected_client_text = tk.Text(selected_client_frame, wrap="word", height=5)
    selected_client_text.pack(fill=tk.BOTH, expand=True)

    # Create label for selecting details
    detail_label = tk.Label(summary_frame, text="Выберите необходимые для ремонта запчасти:", padx=10, pady=10)
    detail_label.pack()

    # Create treeview for displaying parts
    parts_tree = ttk.Treeview(summary_frame, columns=("ID", "Company", "Article", "Description", "Quantity", "Price"), show="headings")
    parts_tree.pack(fill=tk.BOTH, expand=True)

    # Create frame for buttons
    button_frame = tk.Frame(summary_frame)
    button_frame.pack(pady=10)

    # Create button for adding detail
    add_detail_button = tk.Button(button_frame, text="Добавить деталь", command=add_detail)
    add_detail_button.pack(side=tk.LEFT, padx=5)

    # Create button for removing detail
    remove_button = tk.Button(button_frame, text="Удалить деталь", command=remove_detail)
    remove_button.pack(side=tk.LEFT, padx=5)

    # Create listbox for displaying selected parts
    selected_parts_listbox = tk.Listbox(summary_frame, height=5)
    selected_parts_listbox.pack(fill=tk.BOTH, expand=True)

    # Apply styles to widgets
    apply_styles()

# Function to select client
def select_client():
    messagebox.showinfo("Info", "Select client functionality not implemented yet.")

# Function to add detail
def add_detail():
    messagebox.showinfo("Info", "Add detail functionality not implemented yet.")

# Function to remove detail
def remove_detail():
    messagebox.showinfo("Info", "Remove detail functionality not implemented yet.")
