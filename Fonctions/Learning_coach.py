import csv
import docx
import os 
from docx.shared import Cm

import Fonctions.Decimaux as Decimaux
import Fonctions.Fractions as Fractions
import Fonctions.GrandsNombres as GrandsNombres


def Learning_coach(CSV_notes) :
    with open(str(CSV_notes), mode="r") as csvfile :
        notes = csv.reader(csvfile, delimiter=";")
        liste_du_reader = list(notes)
    liste_du_reader.pop(0)

    for liste in liste_du_reader :
        plan_perso = docx.Document()
        
        section = plan_perso.sections[0]
        header = section.header
        header_para = header.paragraphs[0]      
        header_para.text = 'Plan de travail %s' % (liste[0])
        
        sections = plan_perso.sections
        for section in sections:
            section.top_margin = Cm(1.27)
            section.bottom_margin = Cm(1.27)
            section.left_margin = Cm(1.27)
            section.right_margin = Cm(1.27)

        Decimaux.CompleterDecimaux(liste,plan_perso)
        GrandsNombres.CompleterGrandsNombres(liste,plan_perso)
        Fractions.CompleterFractions(liste,plan_perso)

        ###PRENDRE 18cm de large et 12cm de haut###

        os.chdir('Plans_de_travail') 
        plan_perso.save('Plan de travail %s.docx' % (liste[0]))
        os.chdir('..')
