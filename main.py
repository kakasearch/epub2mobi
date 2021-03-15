import sys
import e2m_ui
import time
import os
import xlwt
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
							 QAction, QFileDialog, QApplication,QMessageBox,QWidget)


class ctl(QWidget):
	def __init__(self,ui):
		super(ctl,self).__init__()
		self.ui = ui
		self.xt = ''
		self.zjg = ''
	def warn(self,str_):
		QMessageBox.information(self,                         #使用infomation信息框
									"警告",
									str_,
									QMessageBox.Yes)
	def showDialog(self):
		#self.ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)  
		# 弹出文件选择框。第一个字符串参数是getOpenFileName()方法的标题。第二个字符串参数指定了对话框的工作目录。
		# 默认的，文件过滤器设置成All files (*)。
		fname = QFileDialog.getOpenFileNames(None, '打开文件', '','*.epub;;*')
		# 选中文件后，读出文件的内容，并设置成文本编辑框组件的显示文本
		if fname[0]:
			paths = fname[0]
			if isinstance(paths, list):
				paths = '\n'.join(paths)
			if self.ui.text.toPlainText():
				self.ui.text.setPlainText(self.ui.text.toPlainText()+'\n'+paths)
			else:
				self.ui.text.setPlainText(paths)
	def cal(self):
		try:
			if self.ui.text.toPlainText():
				files = self.ui.text.toPlainText().split('\n')
				self.ui.text.setPlainText('')
				for path in files:
					if path and ('.epub'in path or '.zip' in path):
						self.ui.text.setPlainText(self.ui.text.toPlainText()+'\n正在处理：'+path)
						os.system('kindlegen "'+path+'"')
				QMessageBox.information(self,                         #使用infomation信息框
											"处理完毕",
											'处理完毕啦！！',
											QMessageBox.Yes)
			else:
				self.warn('请输入epub文件路径')
		except Exception as e:
			with open('log.txt','a+',encoding = 'utf-8')as f:
				f.write(string(e))
			QMessageBox.information(self, 
												"未知错误",
												'请关闭软件重新尝试，部分epub无法转码',
												QMessageBox.Yes)

if __name__ == '__main__':
   
		app = QApplication(sys.argv)
		MainWindow = QMainWindow()
		ui = e2m_ui.Ui_mainWindow()
		ui.setupUi(MainWindow)
		MainWindow.show()
		ctl = ctl(ui)
		ui.open.clicked.connect(lambda :ctl.showDialog())
		ui.start.clicked.connect(lambda :ctl.cal())
		sys.exit(app.exec_())
	