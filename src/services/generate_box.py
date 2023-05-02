import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QHBoxLayout


def generate_basic_layout(index):
    # Create two QLabel widgets with one-line descriptions

    # Card container
    card_container = QWidget()
    card_container.setStyleSheet('''
        QWidget {
            border: 1px solid rgb(200, 200, 200);
            border-radius: 15px;
            padding: 10px;
        }
    ''')

    # Card layout
    card_layout = QVBoxLayout()
    card_layout.setSpacing(5)

    first_layout = QHBoxLayout()
    first_layout.setSpacing(5)

    # Card input
    zoneName = QLineEdit()
    zoneName.setPlaceholderText("Enter Name for Zone")
    zoneName.setStyleSheet('''
        QLineEdit {
            font: 300 10pt "Cascadia Mono Light";
            background-color: rgb(48, 48, 71);
            border: 2px solid white;
            border-radius: 10px;
            color: white;
            min-width: 160px;
            max-width: 160px;
            min-height: 20px;
            padding: 5px;
        }
    ''')
    first_layout.addWidget(zoneName)

    # Card title
    title = QLabel()
    title.setText(f"Objects last seen in Zone {index}")
    title.setObjectName(f"title_{index}")
    title.setWordWrap(True)
    title.setStyleSheet('''
        QLabel {
            color: white;
            font: 700 16px "Cascadia Code";
            min-width: 130px;
            min-height: 20px;
            padding: 5px;
        }
    ''')
    first_layout.addWidget(title)

    card_layout.addLayout(first_layout)

    # Card description
    description = QLabel()
    description.setWordWrap(True)
    description.setObjectName(f"desc_{index}")
    # print(f"ID: desc_{index}")
    description.setText("Object 1, Object 1, Object 1")
    description.setStyleSheet('''
        QLabel {
            color: white;
            font: 700 12px "Cascadia Code";
        }
    ''')
    card_layout.addWidget(description)

    # Set layout to card container
    card_container.setLayout(card_layout)

    return card_container
