import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *    

class MainWindow(QMainWindow):
#generating the main window
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navbar
        navbar=QToolBar()
        self.addToolBar(navbar)


        #BACK BUTTOON
        back_button=QAction('Back',self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        
        #FORWARD BUTTON
        forward_button=QAction('Forward',self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)


        #RELOAD BUTTON
        reload_button=QAction('Reload',self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)

           

        #HOMEBUTTON   
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)


        #WRITE  A URL 
        self.url_bar=QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)


        #UPDATE URL'safter user has surfed
        self.browser.urlChanged.connect(self.update_url)

    #fucntion to navigate home
    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))    

    
    #function to navigate url
    def navigate_to_url(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    
    #fucntion to navigatefrom updated url
    
    def update_url(self,q):
        self.url_bar.setText(q.toString())  

app=QApplication(sys.argv)
QApplication.setApplicationName('MyBrowser')
window=MainWindow()
app.exec_()



