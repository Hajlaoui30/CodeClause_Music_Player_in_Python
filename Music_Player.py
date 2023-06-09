
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStyle
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import *


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 218)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 120, 151))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 118, 149))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.MusicList = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.MusicList.setGeometry(QtCore.QRect(0, 0, 121, 141))
        self.MusicList.setObjectName("MusicList")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(150, 10, 661, 161))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.CurrentMusic = QtWidgets.QLabel(self.frame_2)
        self.CurrentMusic.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentMusic.setObjectName("CurrentMusic")
        self.verticalLayout.addWidget(self.CurrentMusic)
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Current_time = QtWidgets.QLabel(self.frame)
        self.Current_time.setObjectName("Current_time")
        self.horizontalLayout.addWidget(self.Current_time)
        self.Music_Slider = QtWidgets.QSlider(self.frame)
        self.Music_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Music_Slider.setObjectName("Music_Slider")
        self.horizontalLayout.addWidget(self.Music_Slider)
        self.Music_length = QtWidgets.QLabel(self.frame)
        self.Music_length.setObjectName("Music_length")
        self.horizontalLayout.addWidget(self.Music_length)
        self.verticalLayout.addWidget(self.frame)
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pervious = QtWidgets.QPushButton(self.widget)
        self.pervious.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\perv.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pervious.setIcon(icon)
        self.pervious.setObjectName("pervious")
        self.horizontalLayout_2.addWidget(self.pervious)
        # Create player

        self.player = QMediaPlayer()

        # Create button play
        self.play = QtWidgets.QPushButton(self.widget, clicked=self.PlayAudio)
        self.play.setText("")
        # Set icon play
        global icon_play
        icon_play = QtGui.QIcon()
        icon_play.addPixmap(QtGui.QPixmap(
            ".\\play-button-arrowhead.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.play.setIcon(icon_play)
        # Set icon pause
        global icon_pause
        icon_pause = QtGui.QIcon()
        icon_pause.addPixmap(QtGui.QPixmap(
            ".\\pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.play.setIcon(icon_pause)

        self.play.setObjectName("play")
        self.horizontalLayout_2.addWidget(self.play)

        self.next = QtWidgets.QPushButton(self.widget)
        self.next.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            ".\\next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next.setIcon(icon2)
        self.next.setObjectName("next")
        self.horizontalLayout_2.addWidget(self.next)

        self.mute = QtWidgets.QPushButton(self.widget)
        self.mute.setText("")
        global mute_icon
        mute_icon = QtGui.QIcon()
        mute_icon.addPixmap(QtGui.QPixmap(
            ".\\mute.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        global unmute_icon
        unmute_icon = QtGui.QIcon()
        unmute_icon.addPixmap(QtGui.QPixmap(
            ".\\unmute.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mute.setIcon(unmute_icon)
        self.mute.setObjectName("mute")
        self.horizontalLayout_2.addWidget(self.mute)

        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.VolumeSlider = QtWidgets.QSlider(self.widget)
        self.VolumeSlider.setMaximumSize(QtCore.QSize(150, 16777215))
        self.VolumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VolumeSlider.setObjectName("VolumeSlider")
        self.horizontalLayout_2.addWidget(self.VolumeSlider)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAudio = QtWidgets.QMenu(self.menubar)
        self.menuAudio.setObjectName("menuAudio")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_Folder = QtWidgets.QAction(MainWindow)

        self.actionOpen_Folder.setObjectName("actionOpen_Folder")
        self.actionOpen_Folder.triggered.connect(self.Open_Folder_clicked)

        self.actionOpen_Music = QtWidgets.QAction(MainWindow)
        self.actionOpen_Music.setObjectName("actionOpen_Music")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionClose.triggered.connect(self.close)
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menuFile.addAction(self.actionOpen_Music)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAudio.menuAction())

        self.MusicList.currentItemChanged.connect(self.ChangeMusic)
        self.next.clicked.connect(self.NextMusic)
        self.pervious.clicked.connect(self.PreviousMusic)
        self.retranslateUi(MainWindow)
        self.mute.clicked.connect(self.ToggleMute)

        self.VolumeSlider.sliderMoved.connect(self.SetVolume)
        self.player.volumeChanged.connect(self.SetCurrentVolume)
        self.Music_Slider.sliderMoved.connect(self.SetPosition)
        self.player.durationChanged.connect(self.SetDuration)
        self.player.positionChanged.connect(self.SetCurrentPosition)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def closeEvent(self, event):
        # prompt the user to confirm the close action
        reply = QtWidgets.QMessageBox.question(self, 'Message', "Are you sure you want to quit?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        
        # if the user confirms, close the window
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            sys.exit()
            
        else:
            event.ignore()





# Set Volume

    def SetVolume(self, volume):
        self.player.setVolume(volume)
# display current volume

    def SetCurrentVolume(self, volume):
        self.VolumeSlider.setValue(volume)


# Mute fonction

    def ToggleMute(self):
        if self.player.isMuted():
            self.player.setMuted(False)
            self.mute.setIcon(mute_icon)
        else:
            self.player.setMuted(True)
            self.mute.setIcon(unmute_icon)

# Set duration
    def SetDuration(self, duration):
        self.Music_Slider.setMaximum(duration)
        minutes, seconds = divmod(duration / 1000, 60)
        self.Music_length.setText("%02d:%02d" % (minutes, seconds))
# display current position of player

    def SetCurrentPosition(self, position):
        self.Music_Slider.setValue(position)
        minutes, seconds = divmod(position / 1000, 60)
        self.Current_time.setText("%02d:%02d" % (minutes, seconds))

# Set position of the player

    def SetPosition(self, position):
        self.player.setPosition(position)

# play and stop the audio
    def PlayAudio(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.play.setIcon(icon_play)

        else:
            self.player.play()
            self.play.setIcon(icon_pause)
# change the current music

    def ChangeMusic(self, item):
        item = item.text()
        print(item)
        self.CurrentMusic.setText(item)
        path = self.allSongs[item]

        print(path)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(path)))
        self.play.setIcon(icon_play)
        self.player.play()

    def NextMusic(self):
        currentRow = self.MusicList.currentRow()
        self.MusicList.setCurrentRow(currentRow + 1)
        item = self.MusicList.currentItem()
        self.ChangeMusic(item)

    def PreviousMusic(self):
        currentRow = self.MusicList.currentRow()
        self.MusicList.setCurrentRow(currentRow - 1)
        item = self.MusicList.currentItem()
        self.ChangeMusic(item)

    # add directory of folder
    def Open_Folder_clicked(self):
        global dname
        dname = QFileDialog.getExistingDirectory(
            self, 'choose music directory')
        print(dname)
        self.add_to_list(dname)
# Loops through all the mp3 files in the music folder and appends them to the self.allSongs array;

    def add_to_list(self, dname):
        self.allSongs = {}
        self.MusicList.clear()
        if dname!="":
            for file in os.listdir(dname):
                if file.endswith(('.mp3', '.wav', '.flac')):
                    self.allSongs[file] = (str(dname)+"/"+str(file))

                    print(self.allSongs)
                    self.item = QListWidgetItem(file)
                    self.MusicList.addItem(self.item)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CurrentMusic.setText(_translate("MainWindow", "Current Music"))
        self.Current_time.setText(_translate("MainWindow", "00:00"))
        self.Music_length.setText(_translate("MainWindow", "00:00"))
        self.label_4.setText(_translate("MainWindow", "Volume"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAudio.setTitle(_translate("MainWindow", "Audio"))
        self.actionOpen_Folder.setText(_translate("MainWindow", "Open Folder"))
        self.actionOpen_Music.setText(_translate("MainWindow", "Open Music"))
        self.actionClose.setText(_translate("MainWindow", "Close "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
