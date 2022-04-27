from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
import message as Message
import time
import features_matching as Features


def browse_files(self):
    global file_path

    file_name = QFileDialog.getOpenFileName(
        self, "Open file", "./test", "*.jpg;;" " *.png;;" "*.jpeg;;"
    )
    file_path = file_name[0]
    extensionsToCheck = (".jpg", ".png", ".jpeg", ".jfif")
    if file_name[0].endswith(extensionsToCheck):
        start(self)
    elif file_name[0] != "":
        Message.error(self, "Invalid format.")
        return
    else:
        return


def start(self):
    plot_image(self, file_path, "original")
    enable_actions(self)


def plot_image(self, image_path, image_type):
    if image_type == "original":
        self.original_image.setPhoto(QPixmap(image_path))
    if image_type == "output":
        self.output_image.setPhoto(QPixmap(image_path))


def enable_actions(self):
    self.features_combobox.setEnabled(True)


def choose_feature(self, text):
    start = time.time()
    # Features.
    end = time.time()
    Message.info(self, f"Time taken equals {round(end - start, 2)} seconds")
    plot_image(self, file_path, "output")
