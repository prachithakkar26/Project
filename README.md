# QR Code Generator

This repository contains a Python script that generates QR codes based on user input. The script utilizes the qrcode library for QR code generation and the tkinter library for creating a graphical user interface (GUI).

## Prerequisites

- Python 3.x
- *qrcode* library
- *tkinter* library

## Installation

1. Ensure that Python is installed on your system.
2. Install the required libraries by running the following command:

```python
pip install qrcode
```

## Usage

1. Run the Python script using the Python interpreter.
2. A GUI window will appear.
3. Enter the desired text or URL in the corresponding text field.
4. Specify the directory path where you want to save the QR code.
5. Provide a name for the QR code.
6. Set the size of the QR code (from 1 to 40, where 1 represents 21x21 pixels).
7. Click the "Get Code" button.
8. The QR code will be generated and saved as a PNG image in the specified location.
9. A success message box will appear, confirming the successful generation of the QR code.

## Code Explanation

The code begins by importing the necessary libraries: qrcode for generating QR codes and tkinter for creating the GUI.

The handle() function is defined, which is triggered when the user clicks the "Get Code" button. It creates a QRCode object with the specified version, box size, and border. The user input (text or URL) is added to the QR code, and the best_fit() method optimizes the size of the QR code.

The QR code image is then generated using the make_image() method. The file path for saving the QR code is constructed based on the user input. The image is saved as a PNG file in the specified location.

Finally, a success message box is displayed using the messagebox.showinfo() method.

The code creates a GUI window using the Tk() constructor and configures its properties, such as the title, size, and background color.

Various labels and entry fields are added to the GUI window to capture user input. The "Get Code" button is created with a command that triggers the handle() function when clicked.

The mainloop() method is called to start the GUI event loop, allowing the user to interact with the application.

Feel free to customize the code according to your specific requirements.
