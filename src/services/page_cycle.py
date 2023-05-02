from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QLabel


def go_to_next_page(self):
    print("NEXT")
    current_index = self.stackedWidget_2.currentIndex()
    if current_index < self.stackedWidget_2.count() - 1:
        self.stackedWidget_2.setCurrentIndex(current_index + 1)


def go_to_previous_page(self):
    print("PREV")
    current_index = self.stackedWidget_2.currentIndex()
    if current_index > 0:
        self.stackedWidget_2.setCurrentIndex(current_index - 1)
