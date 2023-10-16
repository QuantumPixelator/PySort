# A simple PySide6 GUI application to organize files in a folder
# Author: Quantum Pixelator
# License: MIT

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt
import os
import shutil
import sys

# Create a dictionary of file extensions and corresponding subfolder names
file_types = {
    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".jpeg": "Images",
    ".svg": "Images",
    ".bmp": "Images",
    ".ico": "Images",
    ".tif": "Images",
    ".tiff": "Images",
    ".webp": "Images",
    "avif": "Images",
    ".mp3": "Music",
    ".wav": "Music",
    ".ogg": "Music",
    ".flac": "Music",
    ".zip": "Compressed",
    ".rar": "Compressed",
    ".tar": "Compressed",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".exe": "Programs",
    ".msi": "Programs",
    ".apk": "Programs",
    ".py": "Scripts",
    ".js": "Scripts",
    ".css": "Scripts",
    ".html": "Scripts",
    ".php": "Scripts",
    ".iso": "Disk Images",
    ".dmg": "Disk Images",
    ".img": "Disk Images",
    ".vcd": "Disk Images",
    ".bin": "Disk Images",
    ".cue": "Disk Images",
    ".mdf": "Disk Images",
    ".mds": "Disk Images",
    ".nrg": "Disk Images",
    ".toast": "Disk Images",
    ".vmdk": "Disk Images",
    ".vdi": "Disk Images",
    ".vhd": "Disk Images",
    ".vhdx": "Disk Images",
    ".wim": "Disk Images",
    ".csv": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".xls": "Spreadsheets",
    ".ods": "Documents",
    ".odt": "Documents",
    ".odp": "Documents",
    ".odg": "Documents",
    ".odf": "Documents",
    ".odc": "Documents",
    ".odb": "Documents",
    ".odi": "Documents",
    ".odm": "Documents",
    ".ott": "Documents",
    ".ots": "Documents",
    ".otp": "Documents",
    ".otg": "Documents",
    ".otf": "Documents",
    ".otc": "Documents",
    ".otb": "Documents",
    ".oti": "Documents",
    ".oth": "Documents",
    ".rtf": "Documents",
    ".xml": "Documents",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".doc": "Documents",
    ".txt": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",
}

def organize_files():
    folder_path = QFileDialog.getExistingDirectory(caption="Select the folder to organize")
    if folder_path:
        for file_type, subfolder_name in file_types.items():
            if not os.path.exists(os.path.join(folder_path, subfolder_name)):
                os.makedirs(os.path.join(folder_path, subfolder_name))

        for file in os.listdir(folder_path):
            file_extension = os.path.splitext(file)[1]
            if file_extension in file_types.keys():
                shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, file_types[file_extension], file))
        
        msg_label.setText("Files organized successfully!")

app = QApplication(sys.argv)

# Create a main window
main_window = QMainWindow()
main_window.setWindowTitle("File Organizer")
main_window.setGeometry(100, 100, 400, 200)

# Create a QWidget for the central widget
central_widget = QWidget()
main_window.setCentralWidget(central_widget)

# Create a vertical layout
layout = QVBoxLayout()

# Create a label to display messages
msg_label = QLabel("Select a folder to organize.")
msg_label.setAlignment(Qt.AlignCenter)

# Create a button for the file dialog
organize_button = QPushButton("Organize Files")
organize_button.clicked.connect(organize_files)

# Add widgets to layout
layout.addWidget(msg_label)
layout.addWidget(organize_button)

# Styling
app.setStyleSheet("""
    QWidget {
        font: 16px;
    }
    QLabel {
        color: #333;
    }
    QPushButton {
        background-color: #34ABDB;
        color: white;
        padding: 14px 20px;
        border: none;
        border-radius: 4px;
    }
    QPushButton:hover {
        background-color: #2D90B8;
    }
""")

# Set layout to central widget
central_widget.setLayout(layout)

main_window.show()

sys.exit(app.exec())
