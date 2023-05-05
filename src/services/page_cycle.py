from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QLabel


def go_to_next_page(self):
    # print("NEXT")
    current_index = self.stackedWidget_2.currentIndex()
    if current_index < self.stackedWidget_2.count() - 1:
        self.stackedWidget_2.setCurrentIndex(current_index + 1)
        self.nextBtn.setText(str(next_page_name(self)))
        self.previousBtn.setText(str(previous_page_name(self)))


def go_to_previous_page(self):
    # print("PREV")
    current_index = self.stackedWidget_2.currentIndex()
    if current_index > 0:
        self.stackedWidget_2.setCurrentIndex(current_index - 1)
        self.previousBtn.setText(str(previous_page_name(self)))
        self.nextBtn.setText(str(next_page_name(self)))


def next_page_name(self):
    current_index = self.stackedWidget_2.currentIndex()
    if current_index < self.stackedWidget_2.count() - 1:
        next_page = self.stackedWidget_2.widget(current_index + 1)
        # print(next_page.objectName())
        self.nextBtn.setEnabled(True)
        return next_page.objectName()
    else:
        self.nextBtn.setEnabled(False)
        # print("NO MORE PAGES")
        return None


def previous_page_name(self):
    current_index = self.stackedWidget_2.currentIndex()
    # Checks to ensure the current page is not on the first page (index bigger than 0 as 0 is the first page)
    if current_index > 0:
        previous_page = self.stackedWidget_2.widget(current_index - 1)
        # print(previous_page.objectName())
        self.previousBtn.setEnabled(True)
        return previous_page.objectName()
    else:
        self.previousBtn.setEnabled(False)
        # print("NO MORE PAGES")
        return None
