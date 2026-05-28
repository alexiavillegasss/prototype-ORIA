import fitz
import io

class PDFGenerator:
    def __init__(self, template_path: str):
        self.template_path = template_path

    def generate_dac_pdf(self, extracted_data: dict) -> bytes:
        doc = fitz.open(self.template_path)

        field_values = {}
        
        # Personne Majeure concernée
        field_values["Texte9"] = extracted_data.get("nom_usage", "")
        field_values["Texte11"] = extracted_data.get("nom_naissance", "")
        field_values["Texte13"] = extracted_data.get("prenoms", "")
        field_values["Texte16"] = extracted_data.get("sexe", "")
        field_values["Texte17"] = extracted_data.get("date_naissance", "")
        field_values["Texte10"] = extracted_data.get("commune_naissance", "")
        field_values["Texte12"] = extracted_data.get("adresse_complete", "")
        field_values["Texte14"] = extracted_data.get("telephone", "")
        
        # Commentaires (bottom of block 1)
        field_values["Texte15"] = extracted_data.get("commentaires", "")
        
        # Checkboxes for "Vit seul" and "Lieu"
        vit_seul_val = str(extracted_data.get("vit_seul", "")).upper()
        if vit_seul_val == "OUI":
            field_values["Oui"] = True
        elif vit_seul_val == "NON":
            field_values["Non"] = True
            
        lieu = extracted_data.get("lieu_actuel", "").lower() if extracted_data.get("lieu_actuel") else ""
        if "domicile" in lieu:
            field_values["A domicile"] = True
        elif "etablissement" in lieu:
            field_values["En établissement"] = True
            
        # APA / GIR / MDPH / ALD
        if str(extracted_data.get("apa", "")).upper() == "OUI":
            field_values["Case à cocher25"] = True
            
        field_values["Texte75"] = extracted_data.get("gir", "")
        
        if extracted_data.get("mdph") is True:
            field_values["Case à cocher74"] = True
            
        if extracted_data.get("ald") is True:
            field_values["Case à cocher27"] = True
            
        # Description
        field_values["Texte20"] = extracted_data.get("description_situation", "")
        field_values["Texte21"] = extracted_data.get("actions_entreprises", "")
        field_values["Texte22"] = extracted_data.get("attentes_dac", "")
        
        # Alertes (Page 2 checkboxes)
        alertes = extracted_data.get("alertes", {})
        if alertes.get("pb_actes_essentiels"):
            field_values["Problèmes liés aux actes essentiels de la vie se nourrir se vêtir se laver se déplacer"] = True
        if alertes.get("pb_activites_domestiques"):
            field_values["Problèmes liés dans les activités de la vie domestiques courses ménages préparation des repas des médicaments"] = True
        if alertes.get("pathologies_chroniques"):
            field_values["Pathologie(s) chronique(s) ou évolutive(s)"] = True
        if alertes.get("pb_memoire_decision"):
            field_values["Problèmes d'autonomie décisionnelle ( troubles de la mémoire, risque d'abus de faiblesse)"] = True
        if alertes.get("conduites_addictives"):
            field_values["Conduites addictives"] = True
        if alertes.get("medocs_plus_de_5"):
            field_values["Prise de médicaments 5"] = True
        if alertes.get("troubles_psy"):
            field_values["Troubles psychiatriques  psychiques"] = True
        if alertes.get("risque_chute"):
            field_values["Risque de chute"] = True
        if alertes.get("hospit_recente"):
            field_values["Hospitalisation récente en urgence"] = True
            date_h = alertes.get("hospit_date", "")
            motif_h = alertes.get("hospit_motif", "")
            if date_h or motif_h:
                field_values["Texte25"] = f"{date_h} - {motif_h}".strip(" -")
        if alertes.get("isolement_social"):
            field_values["Isolement social ou familial ruptures des liens"] = True
        if alertes.get("epuisement_aidant"):
            field_values["Epuisement absence  indisponibilité de laidant"] = True
        if alertes.get("diff_financieres"):
            field_values["Difficultés à la gestion administrative et financière"] = True
        if alertes.get("logement_inadapte"):
            field_values["Logement inadapté problème daccessibilité isolement géographique"] = True
        if alertes.get("incurie_insalubrite"):
            field_values["Incurie encombrement insalubrité"] = True
            
        pro_mapping = {
            "medecin_traitant": ("Texte37", "Texte38", "Texte39"),
            "specialiste": ("Texte40", "Texte41", "Texte42"),
            "infirmier": ("Texte43", "Texte44", "Texte45"),
            "ssiad_had": ("Texte46", "Texte47", "Texte48"),
            "saad": ("Texte49", "Texte50", "Texte51"),
            "aide_a_domicile": ("Texte49", "Texte50", "Texte51"),
            "admr": ("Texte49", "Texte50", "Texte51"),
            "palliatifs": ("Texte52", "Texte53", "Texte54"),
            "pharmacien": ("Texte55", "Texte56", "Texte57"),
            "kine": ("Texte58", "Texte59", "Texte60"),
            "repas": ("Texte61", "Texte62", "Texte63"),
            "telealarme": ("Texte64", "Texte65", "Texte66"),
            "social": ("Texte67", "Texte68", "Texte69"),
            "autre": ("Texte70", "Texte71", "Texte72")
        }
            
        cercle = extracted_data.get("cercle_de_soins", [])
        for pro in cercle:
            pro_type = pro.get("type", "autre")
            nom = pro.get("nom", "")
            tel = pro.get("tel", "")
            email = pro.get("email", "")
            # Clean INCONNU for display
            display_nom = nom if str(nom).upper() != "INCONNU" else ""
            display_tel = tel if str(tel).upper() != "INCONNU" else ""
            display_email = email if str(email).upper() != "INCONNU" else ""
            
            if pro_type in pro_mapping:
                nom_field, tel_field, email_field = pro_mapping[pro_type]
                field_values[nom_field] = display_nom
                field_values[tel_field] = display_tel
                field_values[email_field] = display_email
                
        # Clean INCONNU everywhere
        for k, v in field_values.items():
            if isinstance(v, str) and v.upper() == "INCONNU":
                field_values[k] = ""

        for page in doc:
            for widget in page.widgets():
                fname = widget.field_name
                if fname in field_values:
                    val = field_values[fname]
                    if widget.field_type == fitz.PDF_WIDGET_TYPE_CHECKBOX:
                        if val is True:
                            widget.field_value = True
                    else:
                        widget.field_value = str(val)
                    widget.update()
        
        # Save to bytes
        pdf_bytes = doc.write()
        doc.close()
        return pdf_bytes
