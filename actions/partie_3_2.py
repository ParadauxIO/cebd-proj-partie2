
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
        # TODO fix request
        pass
        # self.refreshTable(self.ui.tableWidget, '''
        # WITH nEquipes AS (
        # SELECT LesAgesSportifs.ageSp AS Age, numEq AS nEquipe
        #     FROM LesAgesSportifs JOIN LesSportifsEQ ON (LesAgesSportifs.numSp = LesSportifsEQ.numSp)
        # )
        # SELECT nEquipe AS numEq, ROUND(AVG(Age)) AS AvgAge
        # FROM nEquipes JOIN LesResultats ON (nEquipe = gold)
        # GROUP BY nEquipe;
        # ''')
