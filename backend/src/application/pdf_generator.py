import fitz
import io
import datetime

class PDFGenerator:
    def __init__(self, dac_template_path: str = None, clic_template_path: str = None, clic_toulon_template_path: str = None, clic_provence_verte_template_path: str = None, clic_hadage_template_path: str = None):
        self.dac_template_path = dac_template_path
        self.clic_template_path = clic_template_path
        self.clic_toulon_template_path = clic_toulon_template_path
        self.clic_provence_verte_template_path = clic_provence_verte_template_path
        self.clic_hadage_template_path = clic_hadage_template_path

    def generate_dac_pdf(self, extracted_data: dict) -> bytes:
        if not self.dac_template_path:
            raise ValueError("DAC template path not configured")
        doc = fitz.open(self.dac_template_path)

        field_values = {}
        
        # ADRESSEUR (Page 1 en haut)
        field_values["Texte1"] = extracted_data.get("emetteur_structure", "")
        field_values["Texte2"] = extracted_data.get("emetteur_service", "")
        field_values["Texte3"] = extracted_data.get("emetteur_fonction", "")
        field_values["Texte4"] = extracted_data.get("emetteur_nom", "")
        field_values["Texte5"] = extracted_data.get("emetteur_prenom", "")
        field_values["Texte6"] = datetime.datetime.now().strftime("%d/%m/%Y")
        field_values["Texte7"] = extracted_data.get("emetteur_telephone", "")
        field_values["Texte8"] = extracted_data.get("emetteur_mail", "")
        
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
        field_values["Oui"] = False
        field_values["Non"] = False
        field_values["A domicile"] = False
        field_values["En établissement"] = False
        
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
        detailed_motif = extracted_data.get("motif_or_description", "")
        short_desc = extracted_data.get("description_situation", "")
        
        # On injecte le résumé le plus détaillé possible dans la Description Factuelle
        if len(short_desc) < 200:
            field_values["Texte20"] = detailed_motif
        else:
            field_values["Texte20"] = short_desc
            
        field_values["Texte21"] = extracted_data.get("actions_entreprises", "")
        field_values["Texte22"] = extracted_data.get("attentes_dac", "")
        
        # Alertes (Page 2 checkboxes)
        alertes = extracted_data.get("alertes", {})
        checkbox_mappings = []
        if alertes.get("pb_actes_essentiels"): checkbox_mappings.append(("actes essentiels", True))
        if alertes.get("pb_activites_domestiques"): checkbox_mappings.append(("domestiques", True))
        if alertes.get("pathologies_chroniques"): checkbox_mappings.append(("chronique", True))
        if alertes.get("pb_memoire_decision"): checkbox_mappings.append(("autonomie", True))
        if alertes.get("conduites_addictives"): checkbox_mappings.append(("addictives", True))
        if alertes.get("medocs_plus_de_5"): checkbox_mappings.append(("5", True))
        if alertes.get("troubles_psy"): checkbox_mappings.append(("psychiatriques", True))
        if alertes.get("risque_chute"): checkbox_mappings.append(("chute", True))
        if alertes.get("hospit_recente"): 
            checkbox_mappings.append(("Hospitalisation", True))
            date_h = alertes.get("hospit_date", "")
            motif_h = alertes.get("hospit_motif", "")
            if date_h or motif_h:
                field_values["Texte25"] = f"{date_h} - {motif_h}".strip(" -")
        if alertes.get("isolement_social"): checkbox_mappings.append(("Isolement social", True))
        if alertes.get("epuisement_aidant"): checkbox_mappings.append(("Epuisement", True))
        if alertes.get("diff_gestion_admin_fin"): checkbox_mappings.append(("administrative", True))
        if alertes.get("risque_precarite"): checkbox_mappings.append(("Risque de pr", True))
        if alertes.get("dettes_impayes"): checkbox_mappings.append(("Dettes", True))
        if alertes.get("perte_acces_droit"): checkbox_mappings.append(("droit", True))
        if alertes.get("logement_inadapte"): checkbox_mappings.append(("Logement inadapt", True))
        if alertes.get("incurie_insalubrite"): checkbox_mappings.append(("Incurie", True))
            
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
                # Mapping normal (Textes et quelques cases exactes)
                if fname in field_values:
                    val = field_values[fname]
                    if widget.field_type == fitz.PDF_WIDGET_TYPE_CHECKBOX:
                        if val is True:
                            widget.field_value = True
                        elif val is False:
                            widget.field_value = False
                    else:
                        widget.field_value = str(val)
                    widget.update()
                
                # Mapping substring (spécifique aux Alertes pour contrer les bugs d'encodage PDF)
                if widget.field_type == fitz.PDF_WIDGET_TYPE_CHECKBOX:
                    for substring, val in checkbox_mappings:
                        if substring in fname:
                            if val is True:
                                widget.field_value = True
                                widget.update()
                            break
        
        pdf_bytes = doc.write()
        doc.close()
        return pdf_bytes

    def generate_clic_pdf(self, extracted_data: dict) -> bytes:
        if not self.clic_template_path:
            raise ValueError("CLIC template path not configured")
        doc = fitz.open(self.clic_template_path)
        page = doc[0]

        def draw_text(text: str, x: float, y0: float):
            if text and str(text).upper() != "INCONNU":
                page.insert_text(fitz.Point(x, y0 + 10), str(text), fontsize=10, fontname="helv", color=(0, 0, 0))

        # Emetteur
        draw_text(extracted_data.get("emetteur_date"), 57, 99)
        draw_text(extracted_data.get("emetteur_nom"), 57, 114)
        draw_text(extracted_data.get("emetteur_prenom"), 376, 114)
        draw_text(extracted_data.get("emetteur_service"), 179, 130)
        draw_text(extracted_data.get("emetteur_telephone"), 91, 146)
        draw_text(extracted_data.get("emetteur_email"), 67, 162)

        # Usager
        draw_text(extracted_data.get("usager_nom_usage"), 106, 226)
        draw_text(extracted_data.get("usager_nom_naissance"), 136, 241)
        draw_text(extracted_data.get("usager_sexe"), 60, 257)
        draw_text(extracted_data.get("usager_date_naissance"), 137, 273)
        draw_text(extracted_data.get("usager_adresse"), 363, 225)
        draw_text(extracted_data.get("usager_prenoms"), 425, 241)
        draw_text(extracted_data.get("usager_telephone"), 425, 257)
        draw_text(extracted_data.get("usager_email"), 400, 273)

        # Motifs & Aides
        draw_text(extracted_data.get("motif_1"), 21, 514)
        draw_text(extracted_data.get("motif_2"), 21, 533)
        draw_text(extracted_data.get("motif_3"), 21, 552)

        # Famille / Aidant
        draw_text(extracted_data.get("aidant_nom"), 58, 389)
        draw_text(extracted_data.get("aidant_tel"), 49, 405)
        draw_text(extracted_data.get("aidant_email"), 66, 421)
        draw_text(extracted_data.get("aidant_lien"), 340, 389)
        draw_text(extracted_data.get("aidant_adresse"), 362, 405)

        draw_text(extracted_data.get("aide_1"), 21, 657)
        draw_text(extracted_data.get("aide_2"), 21, 674)

        for widget in page.widgets():
            if "cocher4" in widget.field_name and extracted_data.get("usager_vit_seul") is True:
                widget.field_value = True
                widget.update()
            elif "cocher5" in widget.field_name and extracted_data.get("usager_vit_seul") is False:
                widget.field_value = True
                widget.update()

        pdf_bytes = doc.write()
        doc.close()
        return pdf_bytes

    def generate_clic_toulon_pdf(self, extracted_data: dict) -> bytes:
        if not self.clic_toulon_template_path:
            raise ValueError("CLIC Toulon template path not configured")
        doc = fitz.open(self.clic_toulon_template_path)

        field_values = {}
        
        # Helper to split phone numbers
        def split_phone(phone_str, fields_list):
            import re
            digits = re.sub(r"\D", "", phone_str)
            chunks = [digits[i:i+2] for i in range(0, len(digits), 2)]
            for i, fname in enumerate(fields_list):
                if i < len(chunks):
                    field_values[fname] = chunks[i]

        # Emetteur
        field_values["Vos coordonnées nom prénom"] = f"{extracted_data.get('emetteur_nom', '')} {extracted_data.get('emetteur_prenom', '')}".strip()
        field_values["Mail"] = extracted_data.get("emetteur_email", "")
        field_values["Texte14"] = extracted_data.get("emetteur_date", "")
        split_phone(extracted_data.get("emetteur_telephone", ""), ["Texte1", "Texte2", "Texte3", "Texte4", "Texte5"])

        # Usager
        sexe = str(extracted_data.get("usager_sexe", "")).lower()
        if "f" in sexe:
            field_values["Mme"] = True
        else:
            # We match by substring in widget mapping for Monsieur
            pass

        nom = extracted_data.get('usager_nom_usage', '').strip()
        prenom = extracted_data.get('usager_prenoms', '').strip()
        em_nom = extracted_data.get('emetteur_nom', '').strip()
        em_prenom = extracted_data.get('emetteur_prenom', '').strip()
        
        if nom.lower() == em_nom.lower() and prenom.lower() == em_prenom.lower() and prenom:
            prenom = ""

        field_values["nom et prenom"] = f"{nom} {prenom}".strip()
        field_values["Adresse complète 1"] = extracted_data.get("usager_adresse", "")
        
        split_phone(extracted_data.get("usager_telephone", ""), ["Texte9", "Texte10", "Texte11", "Texte12", "Texte13"])
        
        naissance = str(extracted_data.get("usager_date_naissance", "")).strip()
        if len(naissance) == 4:
            field_values["Texte8"] = naissance
        else:
            parts = naissance.replace("-", "/").split("/")
            if len(parts) == 3:
                field_values["Texte6"] = parts[0]
                field_values["Texte7"] = parts[1]
                field_values["Texte8"] = parts[2]
            else:
                field_values["Texte6"] = naissance
            
        lien = extracted_data.get("aidant_lien", "")
        if lien:
            field_values["autres demandeur"] = f"Famille - {lien}"
        elif "famille" in str(extracted_data.get("emetteur_service", "")).lower():
            field_values["autres demandeur"] = "Famille"

        # Hospitalisation (Par défaut: Non)
        field_values["Non_2"] = True

        # Motifs
        field_values["Compléments dinformation 1"] = extracted_data.get("motif_1", "")
        field_values["Compléments dinformation 2"] = extracted_data.get("motif_2", "")
        field_values["Compléments dinformation 3"] = extracted_data.get("motif_3", "")

        # Clean INCONNU everywhere
        for k, v in field_values.items():
            if isinstance(v, str) and v.upper() == "INCONNU":
                field_values[k] = ""

        # Map to widgets
        for page in doc:
            for widget in page.widgets():
                fname = widget.field_name
                # Demandeur "Autre préciser"
                if fname == "Autre prciser" and (extracted_data.get("aidant_lien") or "famille" in str(extracted_data.get("emetteur_service", "")).lower()):
                    widget.field_value = True
                    widget.update()
                
                # Map checkboxes manually
                if fname == "Vit seule" and extracted_data.get("usager_vit_seul") is True:
                    widget.field_value = True
                    widget.update()
                
                if "Monsieur" in fname and "f" not in sexe:
                    widget.field_value = True
                    widget.update()
                
                # Entourage
                if fname == "Avec entourage famille proches" and extracted_data.get("aidant_nom"):
                    widget.field_value = True
                    widget.update()
                
                # Aides
                aides_text = (str(extracted_data.get("aide_1", "")) + " " + str(extracted_data.get("aide_2", ""))).lower()
                if "infirmi" in aides_text or "idel" in aides_text or "soin" in aides_text:
                    if fname == "SSIAD":
                        widget.field_value = True
                        widget.update()
                    if fname == "Oui":  # This is the "Oui" for Services à domicile
                        widget.field_value = True
                        widget.update()
                        
                if "repas" in aides_text or "portage" in aides_text:
                    if fname == "Portage de repas":
                        widget.field_value = True
                        widget.update()
                    if fname == "Oui":
                        widget.field_value = True
                        widget.update()

                if "ménage" in aides_text or "domicile" in aides_text or "apa" in aides_text:
                    if fname == "Aide à domicile":
                        widget.field_value = True
                        widget.update()
                    if fname == "Oui":
                        widget.field_value = True
                        widget.update()
                        
                # Motifs (Cases à cocher) basés sur le texte brut
                raw = str(extracted_data.get("raw_text", "")).lower()
                
                if fname == "Problme de sant" and ("chute" in raw or "santé" in raw or "sante" in raw or "mémoire" in raw or "memoire" in raw or "tête" in raw or "alzheimer" in raw or "malade" in raw or "tombé" in raw):
                    widget.field_value = True
                    widget.update()
                
                if fname == "Personne isole" and ("isolé" in raw or "seul" in raw or "solitude" in raw):
                    widget.field_value = True
                    widget.update()
                    
                if fname == "Troubles du comportement" and ("comportement" in raw or "agressif" in raw or "méchant" in raw or "démence" in raw or "déambule" in raw or "nuit" in raw):
                    widget.field_value = True
                    widget.update()
                    
                if fname == "Possibilit daddiction" and ("alcool" in raw or "addiction" in raw or "drogue" in raw):
                    widget.field_value = True
                    widget.update()
                    
                if fname == "Logement insalubre" and ("insalubre" in raw or "sale" in raw or "inadapté" in raw or "logement" in raw):
                    widget.field_value = True
                    widget.update()

                # Normal mapping
                if fname in field_values:
                    val = field_values[fname]
                    if widget.field_type == fitz.PDF_WIDGET_TYPE_CHECKBOX:
                        if val is True:
                            widget.field_value = True
                    else:
                        widget.field_value = str(val)
                    widget.update()
        
        pdf_bytes = doc.write()
        doc.close()
        return pdf_bytes


    def _fill_clic_hadage(self, extracted_data: dict) -> bytes:
        if not self.clic_hadage_template_path:
            raise ValueError("Hadage template path not configured")
        doc = fitz.open(self.clic_hadage_template_path)
        page = doc[0]
        
        field_values = {
            "date emetteur": extracted_data.get("emetteur_date", ""),
            "nom emetteur": extracted_data.get("emetteur_nom", ""),
            "prenom emetteur": extracted_data.get("emetteur_prenom", ""),
            "service fonction qualite emetteur": extracted_data.get("emetteur_service", ""),
            "telephone emetteur": extracted_data.get("emetteur_telephone", ""),
            "mail emetteur": extracted_data.get("emetteur_email", ""),
            
            "nom personne": extracted_data.get("usager_nom_usage", ""),
            "nom naissance personne": extracted_data.get("usager_nom_naissance", ""),
            "prénom personne": extracted_data.get("usager_prenoms", ""),
            "sexe personne": extracted_data.get("usager_sexe", ""),
            "naissance personne": extracted_data.get("usager_date_naissance", ""),
            "adresse personne": extracted_data.get("usager_adresse", ""),
            "telephone personne": extracted_data.get("usager_telephone", ""),
            "mail personne": extracted_data.get("usager_email", ""),
            
            "nom famille aidant": extracted_data.get("aidant_nom", ""),
            "telephone famille aidant": extracted_data.get("aidant_tel", ""),
            "mail famille aidant": extracted_data.get("aidant_email", ""),
            "lien famille aidant": extracted_data.get("aidant_lien", ""),
            "adresse famille aidant": extracted_data.get("aidant_adresse", ""),
            "motif de la demande": "",
        }
        
        motifs = [str(extracted_data.get(f"motif_{i}", "")).strip() for i in range(1, 4)]
        motifs = [m for m in motifs if m]
        unique_motifs = []
        for m in motifs:
            if m not in unique_motifs and not any(m in other for other in unique_motifs):
                unique_motifs.append(m)
        field_values["motif de la demande"] = "\n".join(unique_motifs)
        
        if extracted_data.get("usager_vit_seul") is True:
            field_values["Vit seul"] = True
            
        aides_text = (str(extracted_data.get("aide_1", "")) + " " + str(extracted_data.get("aide_2", ""))).lower()
        if "infirmi" in aides_text or "idel" in aides_text:
            field_values["ok idel"] = True
            
        if "ssiad" in aides_text or "soins" in aides_text:
            field_values["ok ssiad"] = True
            
        if "portage" in aides_text or "repas" in aides_text:
            field_values["ok portage de repas"] = True
            
        if "apa" in aides_text:
            field_values["ok apa"] = True
            
        if "domicile" in aides_text or "menage" in aides_text or "ménage" in aides_text:
            field_values["ok service a domicile"] = True
            
        cercle = extracted_data.get("cercle_de_soins", [])
        for pro in cercle:
            t = pro.get("type", "")
            nom_pro = pro.get("nom", "")
            tel_pro = pro.get("tel", "")
            mail_pro = pro.get("email", "")
            
            if t == "medecin_traitant":
                field_values["ok medecin traitant"] = True
                field_values["nom medecin"] = nom_pro
                field_values["telephone medecin"] = tel_pro
                field_values["mail medecin"] = mail_pro
                
            elif t == "specialiste":
                # La case à cocher s'appelle "ok medecin generaliste" dans le PDF pour le spécialiste (erreur de nommage du PDF d'origine)
                field_values["ok medecin generaliste"] = True
                field_values["nom medecin spécialiste"] = nom_pro
                field_values["telephone medecin spécialiste"] = tel_pro
                field_values["mail medecin spécialiste"] = mail_pro
                
            elif t == "infirmier":
                field_values["ok idel"] = True
                field_values["IDEL NOM"] = f"{nom_pro} {tel_pro}".strip()
                
            elif t == "ssiad_had":
                field_values["ok ssiad"] = True
                field_values["SSIAD NOM"] = f"{nom_pro} {tel_pro}".strip()
                
            elif t == "pharmacien":
                field_values["ok pharmacien"] = True
                field_values["PHARMACIEN"] = f"{nom_pro} {tel_pro}".strip()
                
            elif t == "saad":
                field_values["ok service a domicile"] = True
                field_values["Service aide a domicile"] = f"{nom_pro} {tel_pro}".strip()
                
            elif t == "social":
                field_values["ok ref social"] = True
                field_values["REFERENT SOC"] = f"{nom_pro} {tel_pro}".strip()
                
            elif t == "autre":
                field_values["ok autres"] = True
                field_values["AUTRES"] = f"{nom_pro} {tel_pro}".strip()
        for widget in page.widgets():
            if widget.field_name in field_values:
                val = field_values[widget.field_name]
                if isinstance(val, bool):
                    widget.field_value = val
                elif val:
                    widget.field_value = str(val)
                widget.update()
                
        out_pdf = io.BytesIO()
        doc.save(out_pdf, garbage=4, deflate=True)
        doc.close()
        return out_pdf.getvalue()

    def _fill_clic_provence_verte(self, extracted_data: dict) -> bytes:
        if not self.clic_provence_verte_template_path:
            raise ValueError("Provence Verte template path not configured")
        doc = fitz.open(self.clic_provence_verte_template_path)
        
        field_values = {
            "declarant nom prenom": f"{extracted_data.get('emetteur_nom', '')} {extracted_data.get('emetteur_prenom', '')}".strip(),
            "declarant service": extracted_data.get("emetteur_service", ""),
            "declarant telephone": extracted_data.get("emetteur_telephone", ""),
            "declarant mail": extracted_data.get("emetteur_email", ""),
            
            "madame nom": extracted_data.get("usager_nom_usage", ""),
            "madame nom de naissance": extracted_data.get("usager_nom_naissance", ""),
            "madame prenom": extracted_data.get("usager_prenoms", ""),
            "madame date de naissance": extracted_data.get("usager_date_naissance", ""),
            "madame telephone": extracted_data.get("usager_telephone", ""),
            
            "NOM et PRENOM lien de parentéRow1": f"{extracted_data.get('aidant_nom', '')} - {extracted_data.get('aidant_lien', '')}".strip(" -"),
            "TéléphoneRow1": extracted_data.get("aidant_tel", ""),
            "ADRESSERow1": extracted_data.get("aidant_adresse", ""),
            
            "Texte3": "",
        }
        
        motifs = [str(extracted_data.get(f"motif_{i}", "")).strip() for i in range(1, 4)]
        motifs = [m for m in motifs if m]
        unique_motifs = []
        for m in motifs:
            if m not in unique_motifs and not any(m in other for other in unique_motifs):
                unique_motifs.append(m)
        motifs_text = "\n".join(unique_motifs)
        field_values["Texte3"] = motifs_text
        
        # Mapping checkboxes "Vous sollicitez le CLIC pour"
        motifs_lower = motifs_text.lower()
        if "ehpad" in motifs_lower or "hébergement" in motifs_lower or "hebergement" in motifs_lower or "structure" in motifs_lower:
            field_values["Des informations  conseils sur les structures dhébergement"] = True
        elif "intervenant" in motifs_lower or "mise en place" in motifs_lower or "aide" in motifs_lower:
            field_values["La mise en place dintervenants Précisez"] = True
            field_values["Texte4"] = "Aides à domicile / Soins"
        else:
            # Default fallback for most cases
            field_values["Une évaluation gérontologique à domicile"] = True
        
        adresse = extracted_data.get("usager_adresse", "")
        if adresse:
            if not any(char.isdigit() for char in adresse):
                field_values["ville"] = adresse
            else:
                field_values["madame adresse"] = adresse
                
        sexe = str(extracted_data.get("usager_sexe", "")).lower()
        if "femme" in sexe:
            field_values["Madame"] = True
        elif "homme" in sexe:
            field_values["Monsieur"] = True
            
        vit_seul = extracted_data.get("usager_vit_seul")
        if vit_seul is True:
            field_values["Oui_2"] = True
        elif vit_seul is False:
            field_values["Non_2"] = True
            
        aides_text = (str(extracted_data.get("aide_1", "")) + " " + str(extracted_data.get("aide_2", ""))).lower()
        if aides_text.strip():
            field_values["Oui"] = True
            field_values["Texte2"] = aides_text.title()
            
        if "infirmi" in aides_text or "idel" in aides_text:
            field_values["fill_16"] = "Infirmier Libéral"
            frequence = ""
            if "matin" in aides_text or "soir" in aides_text or "jour" in aides_text or "quotidien" in aides_text:
                frequence = "Quotidien"
            elif "semaine" in aides_text or "fois" in aides_text:
                frequence = "Hebdomadaire"
            field_values["fill_17"] = frequence
            
        for page in doc:
            for widget in page.widgets():
                if widget.field_name in field_values:
                    val = field_values[widget.field_name]
                    if isinstance(val, bool):
                        widget.field_value = val
                    elif val:
                        widget.field_value = str(val)
                    widget.update()
                
        out_pdf = io.BytesIO()
        doc.save(out_pdf, garbage=4, deflate=True)
        doc.close()
        return out_pdf.getvalue()
