
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

# Classe permettant d'afficher la fenêtre de visualisation des données
class AppTablesPartie3S1(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/partie_3_1.ui", self)
        self.data = data
        self.refreshAllTablesV1()

    ####################################################################################################################
    # Méthodes permettant de rafraichir les différentes tables
    ####################################################################################################################
    def addButton(self):
        try:
            cursor = self.data.cursor()
            cursor.execute(
                f"INSERT INTO LesInscriptions (numIn, numEp) VALUES ({self.ui.numInIn.text()}, {self.ui.numEpIn.text()})")
            self.refreshAllTablesV1()
            self.data.commit()
        except Exception as e:
            display.refreshLabel(self.ui.errorLabel, "Impossible d'afficher les résultats : " + repr(e))

    def removeButton(self):
        cursor = self.data.cursor()
        cursor.execute(f"DELETE FROM LesInscriptions WHERE numIn={self.ui.numInIn.text()} and numEp={self.ui.numEpIn.text()}")
        self.refreshAllTablesV1()
        self.data.commit()

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
        self.refreshTable(self.ui.tableWidget, "SELECT * from LesInscriptions;")
        pass

