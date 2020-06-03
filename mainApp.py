from mainWin import Ui_MainWindow
import addDialog
from addDialog import Ui_Dialog
import editDialog
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow,QMessageBox,QTableWidgetItem,QLineEdit,QPlainTextEdit
import sqlite3

conn = sqlite3.connect('tableDB.db')
curs = conn.cursor()
curs.execute('CREATE TABLE IF NOT EXISTS information (Producto TEXT , Marca TEXT , Modelo TEXT , Cantidad TEXT, Adquisicion TEXT, Codigo INT, Descripcion TEXT, Precio TEXT)')

class MainApp (QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp,self).__init__(parent)
        self.Init_Ui()
    
    def Init_Ui(self):
        self.setupUi(self)
        self.Load_Database()
        self.show()
        self.pushButton_3.clicked.connect(self.Show_Add_Dialog)
        self.pushButton_2.clicked.connect(self.Delete_data)
        self.pushButton.clicked.connect(self.Show_Edit_Data)
        self.pushButton_4.clicked.connect(self.Search)
        self.pushButton_5.clicked.connect(self.Load_Database)

    def Show_Add_Dialog(self):
        self.adding = AddDialog()
        self.adding.pushButton.clicked.connect(self.Add_Data)
        self.adding.pushButton_2.clicked.connect(self.clearAll)
        self.adding.exec_()

    def Show_Edit_Data(self):
        self.edit = EditDialog()
        self.edit.pushButton.clicked.connect(self.Edit_Data)
        self.edit.pushButton_2.clicked.connect(self.clearEdit)
        self.edit.exec_()

    def Add_Data(self):
        producto = self.adding.lineEdit.text()
        marca = self.adding.lineEdit_2.text()
        modelo = self.adding.lineEdit_3.text()
        cantidad = self.adding.lineEdit_4.text()
        adquirido = self.adding.dateEdit.text()
        precio = self.adding.lineEdit_8.text()
        codigo = self.adding.lineEdit_6.text()
        descripcion = self.adding.plainTextEdit.toPlainText()
        try:
            curs.execute('INSERT INTO information (Producto, Marca, Modelo, Cantidad, Adquisicion, Codigo, Descripcion, Precio)VALUES(?,?,?,?,?,?,?,?)',(producto, marca, modelo, cantidad, adquirido, codigo, descripcion, precio))
            conn.commit()
            #print('HECHO')
            self.Load_Database()
        except Exception as error:
            print(error)

    def Load_Database(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        content = 'SELECT * FROM information'
        res = conn.execute(content)
        for row_index , row_data in enumerate(res):
            self.tableWidget.insertRow(row_index)
            for colm_index , colm_data in enumerate (row_data):
                self.tableWidget.setItem(row_index,colm_index, QTableWidgetItem(str(colm_data)))
        self.label_2.setText("Total de productos : " + str(self.tableWidget.rowCount()))
        return
    
    def Search(self):
        contenido=self.lineEdit.text()
        lista=list(contenido)
        tama=len(lista)
        #print(tama)
        if tama>0:
            try:
                buscar = self.lineEdit.text()
                while self.tableWidget.rowCount() > 0:
                    self.tableWidget.removeRow(0)
                #print(buscar)
                content = "SELECT * FROM information WHERE Producto LIKE '%"+buscar+"%'"
                #print(content)
                res = conn.execute(content)
                #print(res)
                for row_index , row_data in enumerate(res):
                    self.tableWidget.insertRow(row_index)
                    for colm_index , colm_data in enumerate (row_data):
                        self.tableWidget.setItem(row_index,colm_index, QTableWidgetItem(str(colm_data)))
                self.label_2.setText("Total de productos : " + str(self.tableWidget.rowCount()))
                return
            except:
                QMessageBox.about(self, 'Error', 'No se puede realizar la consulta')
        else:
            QMessageBox.about(self, 'Error', 'Ingrese el nombre del producto a buscar')
        

    def Delete_data(self):
        try:
        #self.tableWidget.removeRow(self.tableWidget.currentRow())
            content = 'SELECT * FROM information'
            res = conn.execute(content)
            for row in enumerate (res):
                if row[0] == self.tableWidget.currentRow():
                    #print(row[1])
                    data = row[1]
                    producto = data[0]
                    marca = data [1]
                    modelo = data [2]
                    cantidad = data [3]
                    adquirido = data [4]
                    precio = data [7]
                    codigo = data [5]
                    descripcion = data [6]
                    #print (producto, marca, modelo, cantidad, adquirido, precio, mant, codigo, descripcion)
                    curs.execute("DELETE FROM information WHERE Producto=? AND Marca=? AND Modelo=? AND Cantidad=? AND Adquisicion=? AND Codigo=? AND Descripcion=? AND Precio=?", (producto, marca, modelo, cantidad, adquirido, codigo, descripcion, precio) )
                    conn.commit()
                    self.Load_Database()
        except:
            QMessageBox.about(self, 'Error', 'Usted no selecciono una fila para eliminarla')

    def Edit_Data(self):
        try:
            ede = self.tableWidget.item(self.tableWidget.currentRow(),5).text()
            #print(ede)
            content = 'SELECT * FROM information'
            res = conn.execute(content)
            for row in enumerate (res):
                if row[0] == self.tableWidget.currentRow():
                    marca = self.edit.lineEdit_7.text()
                    modelo = self.edit.lineEdit_9.text()
                    cantidad = self.edit.lineEdit_10.text()
                    precio = self.edit.lineEdit_12.text()
                    descripcion = self.edit.plainTextEdit.toPlainText()
                    curs.execute("UPDATE information SET Marca=?, Modelo=?, Cantidad=?, Precio=?, Descripcion=? WHERE Codigo="+ede, (marca, modelo, cantidad, precio, descripcion))
                    print("exito")
                    conn.commit()
                    self.Load_Database()
                    self.edit.close()
        except:
            QMessageBox.about(self, 'Error', 'Usted no selecciono la fila a editar')

    def clearAll(self):
        for le in self.adding.findChildren(QLineEdit):
            le.clear()
        for lbl in self.adding.findChildren(QPlainTextEdit):
            lbl.clear()
    def clearEdit(self):
        for le in self.edit.findChildren(QLineEdit):
            le.clear()
        for lbl in self.edit.findChildren(QPlainTextEdit):
            lbl.clear()

class AddDialog(QDialog,addDialog.Ui_Dialog):
    def __init__(self,parent=None):
        super(AddDialog,self).__init__(parent)
        self.setupUi(self)


class EditDialog(QDialog,editDialog.Ui_Dialog):
    def __init__(self,parent=None):
        super(EditDialog,self).__init__(parent)
        self.setupUi(self)


app = QApplication([])
win = MainApp()
win.show()
app.exec_()