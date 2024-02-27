import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QPushButton, QLabel, QVBoxLayout, QWidget
import requests
import json
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.list_widget = QListWidget()
        self.button = QPushButton("Fetch Posts")
        self.status_label = QLabel("")
        self.save_button = QPushButton("Save Posts")

        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.list_widget)
        layout.addWidget(self.button)
        layout.addWidget(self.status_label)
        layout.addWidget(self.save_button)

        self.button.clicked.connect(self.fetch_posts)
        self.save_button.clicked.connect(self.save_posts)

        self.show()

    def fetch_posts(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        if response.status_code == 200:
            posts = response.json()
            self.list_widget.clear()
            for post in posts:
                self.list_widget.addItem(str(post))
            self.status_label.setText("Fetched posts successfully.")
        else:
            self.status_label.setText("Failed to fetch posts.")

    def save_posts(self):
        folder_path = "posts"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        if response.status_code == 200:
            posts = response.json()
            for idx, post in enumerate(posts):
                with open(f"{folder_path}/post_{idx}.json", "w") as f:
                    json.dump(post, f)
            self.status_label.setText("Saved posts successfully.")
        else:
            self.status_label.setText("Failed to save posts.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())