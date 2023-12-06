## Inventory Management System

This is a simple product management system developed in Python using the pandas library. It allows for the addition, updating, and viewing of products in a DataFrame.

## Requirements

- Python 3.x
- pandas

## Installation

1. Clone the repository to your local environment:

bash
git clone https://github.com/your-username/product-management-system.git

2. Make sure you have Pandas installed:

pip install pandas (in PowerShell)

## Usage

1. Run the 'main.py' script.

Choose the desired option from the menu:

1 - Add: Adds a new product to the system.
2 - Update: Updates information for an existing product.
3 - Reorder Alerts: Displays alerts to reorder products (not working yet).
4 - Supplier Management: Manages suppliers (not working yet).
0 - Exit: Exits the program.
Follow the on-screen instructions to input or update information.

## Example Data

The system is initialized with a set of example data, but you can customize it in the 'main.py' file.

data = {'Product': ['Strip', 'Form', 'Rubber'],
        'Type': ['Smooth', 'Metallic', '90/10'],
        'Model': ['Aviator', 'Regular', 'Common'],
        'Color': ['White', '--', 'Blue/Red'],
        'Size': ['22', '22', '90cm'],
        'Quantity': [10, 1, 2]
        }

## Contributing
Feel free to contribute to the development of this project. Open an issue to report problems or suggest improvements through pull requests.
