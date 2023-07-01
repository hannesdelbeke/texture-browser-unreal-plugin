"""
an icon browser for the unreal engine project resources
"""
from PySide2 import QtWidgets, QtCore, QtGui, QtUiTools
from PySide2.QtWidgets import QApplication, QLabel, QDialog, QWidget, QProgressBar
from pathlib import Path


# create a widget showing all icons in the icon folder
class IconWidget(QWidget):
    def __init__(self, *args):
        super(IconWidget, self).__init__(*args)

        layout = QtWidgets.QVBoxLayout(self)

        # ' tabs
        self.tab_widget = QtWidgets.QTabWidget()
        image_types = ["png", "bmp", "svg", "tps", "ttf"]

        self.lists = []
        for img_type in image_types:
            thumbnail_list = QtWidgets.QListWidget(self)
            thumbnail_list.setResizeMode(QtWidgets.QListWidget.Adjust)
            if img_type not in ["tps", "ttf"]:
                thumbnail_list.setViewMode(QtWidgets.QListView.IconMode)
                thumbnail_list.setIconSize(QtCore.QSize(64, 64))

            has_a_stylesheet = thumbnail_list.styleSheet() == ""
            if has_a_stylesheet:
                thumbnail_list.setStyleSheet("background-color: rgb(50, 50, 50); color: rgb(255, 255, 255);")

            thumbnail_list.setDragEnabled(False)

            self.lists.append(thumbnail_list)

            tab = QtWidgets.QWidget()
            tab.layout = QtWidgets.QVBoxLayout()
            tab.setLayout(tab.layout)

            tab.layout.addWidget(thumbnail_list)

            self.tab_widget.addTab(tab, f"{img_type}")

            # connect click
            thumbnail_list.itemClicked.connect(self.click_icon)

            # connect tab change
            self.tab_widget.currentChanged.connect(self.search_current_tab)

        # textfield to search for icons
        self.search_field = QtWidgets.QLineEdit()
        self.search_field.textChanged.connect(self.search)
        layout.addWidget(self.search_field)
        self.setLayout(layout)
        layout.addWidget(self.tab_widget)

        self.selected_field = QtWidgets.QLineEdit()
        layout.addWidget(self.selected_field)

        # # Loading bar
        # self.loading_bar = QProgressBar(self)
        # self.loading_bar.setMinimum(0)
        # self.loading_bar.setMaximum(1)
        # layout.addWidget(self.loading_bar)

        # Load icons
        self.load_icons()

    def load_icons(self):
        content_path = Path(r"C:\Program Files\Epic Games\UE_5.0\Engine\Content\\")
        image_types = ["png", "bmp", "svg", "tps", "ttf"]

        total_icons = 0

        # Count the total number of icons
        for img_type in image_types:
            icon_paths = content_path.glob(f"**/*.{img_type}")
            icon_count = sum(1 for _ in icon_paths)
            total_icons += icon_count

        try:
            import unreal

            nr_of_steps = total_icons
            with unreal.ScopedSlowTask(nr_of_steps, "loading icons") as slow_task:
                slow_task.make_dialog(True)
                for x in self.load_icons_iter(image_types=image_types, content_path=content_path):
                    if slow_task.should_cancel():
                        break
                    slow_task.enter_progress_frame(1, f"loaded icon {x}/{nr_of_steps}")
                    # do the thing
        except:
            for _ in self.load_icons_iter(image_types=image_types, content_path=content_path):
                pass


    def load_icons_iter(self, image_types, content_path):

        loaded_icons = 0

        # Load icons and update the progress
        for index, img_type in enumerate(image_types):
            thumbnail_list = self.lists[index]

            icon_paths = content_path.glob(f"**/*.{img_type}")
            icon_count = 0
            for thumbnail_path in icon_paths:
                icon = QtGui.QIcon(str(thumbnail_path))
                name = ""
                if img_type in ["tps", "ttf"]:
                    name = thumbnail_path.stem
                item = QtWidgets.QListWidgetItem(icon, name)
                item.setToolTip(str(thumbnail_path))
                thumbnail_list.addItem(item)
                icon_count += 1

                loaded_icons += 1
                yield loaded_icons

            if icon_count == 0:
                print(f"no icons found for {img_type}")
                continue

            # Update the tab label with the icon count
            self.tab_widget.setTabText(index, f"{img_type}({icon_count})")

    def search_current_tab(self, index):
        # get tab from index
        tab = self.tab_widget.widget(index)
        self.search(self.search_field.text())

    def search(self, text=None):
        if text is None:
            text = self.search_field.text()

        active_tab = self.tab_widget.currentWidget()
        active_list = active_tab.layout.itemAt(0).widget()

        for i in range(active_list.count()):
            item = active_list.item(i)
            if text.lower() in item.toolTip().lower():
                item.setHidden(False)
            else:
                item.setHidden(True)

    def click_icon(self, item):
        self.selected_field.setText(item.toolTip())


window = None


def show():
    global window
    window = IconWidget()
    window.resize(1000, 800)
    window.show()

    # app = QApplication([])
    import unreal
    unreal.parent_external_window_to_slate(window.winId())
    # app.exec_()


show()
