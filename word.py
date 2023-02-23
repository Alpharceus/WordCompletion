import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QListView, QPushButton, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class Autocorrect(QWidget):

    def __init__(self):
        super().__init__()

        # set up the user interface
        self.setWindowTitle('Autocorrect')
        self.setGeometry(100, 100, 500, 300)

        # create the input field
        self.input_label = QLabel("Enter some text:")
        self.input_field = QLineEdit()

        # create the word list view
        self.word_list_model = QStandardItemModel()
        self.word_list_view = QListView()
        self.word_list_view.setModel(self.word_list_model)

        # create the add button
        self.add_button = QPushButton("Add Word")

        # create the layout and add the elements
        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.word_list_view)
        layout.addWidget(self.add_button)
        self.setLayout(layout)

        # connect the input field to the word list
        self.input_field.textChanged.connect(self.update_word_list)

        # connect the add button to the add_word function
        self.add_button.clicked.connect(self.add_word)

        # load the word list from file
        self.load_word_list()

    def update_word_list(self, text):
        # clear the word list
        self.word_list_model.clear()

        # add matching words to the word list
        for word in self.word_list:
            if word.startswith(text):
                item = QStandardItem(word)
                self.word_list_model.appendRow(item)

    def load_word_list(self):
        # read the word list from file
        try:
            with open("word_list.txt", "r") as f:
                self.word_list = [line.strip() for line in f]
        except FileNotFoundError:
            self.word_list = []

    def save_word_list(self):
        # write the word list to file
        with open("word_list.txt", "w") as f:
            for word in self.word_list:
                f.write(word + "\n")

    def add_word(self):
        # get the new word from the input field
        new_word = self.input_field.text()

        # check if the word is already in the list
        if new_word in self.word_list:
            QMessageBox.warning(self, "Duplicate Word", "This word is already in the list.")
            return

        # add the word to the list and update the view
        self.word_list.append(new_word)
        item = QStandardItem(new_word)
        self.word_list_model.appendRow(item)
        self.input_field.clear()

        # save the updated word list to file
        self.save_word_list()

if __name__ == '__main__':
    # create the application and run the main loop
    app = QApplication(sys.argv)
    autocorrect = Autocorrect()
    autocorrect.show()
    sys.exit(app.exec_())

