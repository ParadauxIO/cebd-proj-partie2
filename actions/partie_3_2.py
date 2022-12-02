
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

# Classe permettant d'afficher la fenêtre de visualisation des données
class AppTablesPartie3S2(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/partie_3_2.ui", self)
        self.data = data

        # On met à jour l'affichage avec les données actuellement présentes dans la base
        self.refreshAllTablesV1()
    ####################################################################################################################
    # Méthodes permettant de rafraichir les différentes tables
    ####################################################################################################################

    def addButton(self):
        try:
            cursor = self.data.cursor()
            cursor.execute(f'''
            INSERT INTO LesResultats (numEp, gold, silver, bronze) 
            VALUES ({self.ui.numEpIn.text()}, {self.ui.goldIn.text()}, {self.ui.silverIn.text()}, {self.ui.bronzeIn.text()})
            ON CONFLICT(numEp) DO UPDATE SET gold=excluded.gold, silver=excluded.silver, bronze=excluded.bronze;
            ''')
            self.refreshAllTablesV1()
            self.data.commit()
        except Exception as e:
            display.refreshLabel(self.ui.errorLabel, "Impossible d'afficher les résultats : " + repr(e))

    def removeButton(self):
        try:
            cursor = self.data.cursor()
            cursor.execute(f"DELETE FROM LesResultats WHERE numEp={self.ui.numEpIn.text()}")
            self.refreshAllTablesV1()
            self.data.commit()
        except Exception as e:
            display.refreshLabel(self.ui.errorLabel, "Impossible d'afficher les résultats : " + repr(e))


    # Fonction de mise à jour de l'affichage d'une seule table
    def refreshTable(self, table, query):
        try:
            cursor = self.data.cursor()
            result = cursor.execute(query)
        except Exception as e:
            print(e)
            table.setRowCount(0)
        else:
            display.refreshGenericData(table, result)

    # Fonction permettant de mettre à jour toutes les tables
    @pyqtSlot()
    def refreshAllTablesV1(self):
        # fix request
        self.refreshTable(self.ui.tableWidget, "SELECT * from LesResultats")
