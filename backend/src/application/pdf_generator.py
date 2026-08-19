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
        for widget in page.widgets():
            if widget.field_name in field_values:
                val = field_values[widget.field_name]
                if isinstance(val, bool):
                    widget.field_value = val
                elif val:
                    widget.field_value = str(val)
                widget.update()
                
        out_pdf = io.BytesIO()
        doc.save(out_pdf)
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
        doc.save(out_pdf)
        doc.close()
        return out_pdf.getvalue()

    def generate_comid_pdf(self, comid_data: dict) -> bytes:
        def clean(t):
            if not t: return ""
            s = str(t)
            s = s.replace("’", "'").replace("‘", "'").replace("«", '"').replace("»", '"').replace("–", "-").replace("—", "-")
            # Replace non-latin1 characters if any remain
            return s.encode('latin-1', 'replace').decode('latin-1')

        doc = fitz.open()
        page = doc.new_page(width=595, height=842) # A4 size
        
        # Colors
        blue_dark = (15/255, 23/255, 42/255)
        blue_accent = (59/255, 130/255, 246/255)
        text_dark = (30/255, 41/255, 59/255)
        gray_light = (241/255, 245/255, 249/255)
        gray_border = (203/255, 213/255, 225/255)
        
        # Header box
        page.draw_rect(fitz.Rect(30, 30, 565, 95), color=None, fill=blue_dark)
        page.insert_text(fitz.Point(45, 60), clean("ORIA - RAPPORT D'EVALUATION CLINIQUE COMID"), fontsize=13, color=(1, 1, 1), fontname="helv")
        page.insert_text(fitz.Point(45, 80), clean("Grille de Complexite Multidimensionnelle a Domicile (imad Geneve)"), fontsize=10, color=(0.7, 0.8, 1), fontname="helv")
        
        # Date box
        date_str = clean(comid_data.get("date", datetime.datetime.now().strftime("%d/%m/%Y a %H:%M")))
        total_score = comid_data.get("score", 0)
        level_str = clean(comid_data.get("level", "Non complexe"))
        
        page.draw_rect(fitz.Rect(30, 110, 565, 175), color=gray_border, fill=gray_light, width=0.5)
        page.insert_text(fitz.Point(45, 145), clean(f"Date d'evaluation clinique : {date_str}"), fontsize=11, color=text_dark, fontname="helv")
        
        # Score Badge Box
        score_color = (34/255, 197/255, 94/255) if total_score <= 5 else ((245/255, 158/255, 11/255) if total_score <= 9 else (239/255, 68/255, 68/255))
        page.draw_rect(fitz.Rect(370, 120, 550, 165), color=score_color, fill=score_color)
        page.insert_text(fitz.Point(382, 140), clean(f"SCORE : {total_score} / 30"), fontsize=12, color=(1, 1, 1), fontname="helv")
        page.insert_text(fitz.Point(382, 155), clean(level_str.upper()[:22]), fontsize=8, color=(1, 1, 1), fontname="helv")

        # Table Header
        y = 195
        page.insert_text(fitz.Point(30, y), clean("SYNTHESE PAR DOMAINES CLINIQUES"), fontsize=11, color=text_dark, fontname="helv")
        y += 12
        
        page.draw_rect(fitz.Rect(30, y, 565, y+20), color=None, fill=blue_dark)
        page.insert_text(fitz.Point(40, y+14), clean("Domaine d'Evaluation"), fontsize=9, color=(1,1,1), fontname="helv")
        page.insert_text(fitz.Point(430, y+14), clean("Score (Oui)"), fontsize=9, color=(1,1,1), fontname="helv")
        page.insert_text(fitz.Point(500, y+14), clean("Statut"), fontsize=9, color=(1,1,1), fontname="helv")
        y += 20
        
        domain_scores = comid_data.get("domainScores", {})
        domains_list = [
            ("1. Facteurs de sante / Medicaux", domain_scores.get("sante-medicale", 0)),
            ("2. Facteurs socio-economiques", domain_scores.get("socio-economique", 0)),
            ("3. Facteurs de sante mentale", domain_scores.get("sante-mentale", 0)),
            ("4. Facteurs comportementaux", domain_scores.get("comportementaux", 0)),
            ("5. Facteurs d'instabilite clinique", domain_scores.get("instabilite", 0)),
            ("6. Facteurs lies aux intervenants", domain_scores.get("intervenants", 0)),
        ]
        
        for idx, (d_title, score_val) in enumerate(domains_list):
            bg = (248/255, 250/255, 252/255) if idx % 2 == 0 else (1, 1, 1)
            page.draw_rect(fitz.Rect(30, y, 565, y+20), color=gray_border, fill=bg, width=0.5)
            page.insert_text(fitz.Point(40, y+14), clean(d_title), fontsize=9, color=text_dark, fontname="helv")
            page.insert_text(fitz.Point(440, y+14), clean(f"{score_val} / 5"), fontsize=9, color=text_dark, fontname="helv")
            status = clean("Present" if score_val > 0 else "Aucun")
            page.insert_text(fitz.Point(500, y+14), status, fontsize=9, color=(239/255, 68/255, 68/255) if score_val > 0 else (100/255, 116/255, 139/255), fontname="helv")
            y += 20
            
        y += 20
        page.insert_text(fitz.Point(30, y), clean("DETAILS DES FACTEURS DE COMPLEXITE IDENTIFIES (OUI)"), fontsize=11, color=text_dark, fontname="helv")
        y += 12
        
        checked_items = comid_data.get("checkedItems", [])
        if not checked_items:
            y += 15
            page.insert_text(fitz.Point(30, y), clean("Aucun critere de complexite coche."), fontsize=9, color=(100/255, 116/255, 139/255), fontname="helv")
        else:
            for item in checked_items:
                if y > 780:
                    page = doc.new_page(width=595, height=842)
                    y = 40
                lbl = clean(item.get("label", item.get("code", "")))
                rect_text = fitz.Rect(40, y, 550, y+18)
                page.insert_textbox(rect_text, f"-  {lbl}", fontsize=8.5, color=text_dark, fontname="helv")
                y += 18
                
        # Footer
        footer_y = 815
        page.draw_line(fitz.Point(30, footer_y), fitz.Point(565, footer_y), color=gray_border, width=0.5)
        page.insert_text(fitz.Point(30, footer_y+15), clean("ORIA - Plateforme d'Orientation Clinique et d'Analyse de la Complexite | Referentiel COMID (imad Geneve)"), fontsize=8, color=(148/255, 163/255, 184/255), fontname="helv")
        
        out_pdf = io.BytesIO()
        doc.save(out_pdf)
        doc.close()
        return out_pdf.getvalue()

    def generate_zarit_pdf(self, zarit_data: dict) -> bytes:
        def clean(t):
            if not t: return ""
            s = str(t)
            s = s.replace("’", "'").replace("‘", "'").replace("«", '"').replace("»", '"').replace("–", "-").replace("—", "-")
            return s.encode('latin-1', 'replace').decode('latin-1')

        doc = fitz.open()
        
        blue_dark = (15/255, 23/255, 42/255)
        text_dark = (30/255, 41/255, 59/255)
        gray_light = (241/255, 245/255, 249/255)
        gray_border = (203/255, 213/255, 225/255)
        amber_color = (245/255, 158/255, 11/255)

        senior_nom = clean(zarit_data.get("senior_nom", "Senior non renseigne"))
        aidant_nom = clean(zarit_data.get("aidant_nom", "Aidant"))
        total_score = zarit_data.get("score", 0)
        date_str = clean(zarit_data.get("date", datetime.datetime.now().strftime("%d/%m/%Y a %H:%M")))
        reponses = zarit_data.get("reponses", [0]*22)
        if len(reponses) < 22:
            reponses.extend([0]*(22 - len(reponses)))

        questions = [
            "1. Sentir que votre proche vous demande plus d'aide qu'il n'en a besoin ?",
            "2. Sentir que le temps consacre a votre proche ne vous en laisse pas assez pour vous ?",
            "3. Vous sentir tiraille entre ses besoins et vos autres responsabilites ?",
            "4. Vous sentir embarrasse par le(s) comportement(s) de votre proche ?",
            "5. Vous sentir en colere quand vous etes en presence de votre proche ?",
            "6. Sentir que votre proche nuit a vos relations avec la famille ?",
            "7. Avoir peur de ce que l'avenir reserve a votre proche ?",
            "8. Sentir que votre proche est dependant de vous ?",
            "9. Vous sentir tendu en presence de votre proche ?",
            "10. Sentir que votre sante s'est deterioree a cause de votre implication ?",
            "11. Sentir que vous n'avez pas autant d'intimite que vous aimeriez ?",
            "12. Sentir que votre vie sociale s'est deterioree du fait de soin ?",
            "13. Vous sentir mal a l meaise de recevoir des amis a cause de lui ?",
            "14. Sentir qu'il s'attend a ce que vous soyez la seule personne disponible ?",
            "15. Sentir que vous n'avez pas assez d'argent pour prendre soin de lui ?",
            "16. Sentir que vous ne serez plus capable de prendre soin de lui longtemps ?",
            "17. Sentir que vous avez perdu le controle de votre vie depuis sa maladie ?",
            "18. Souhaiter pouvoir laisser le soin de votre proche a quelqu'un d'autre ?",
            "19. Sentir que vous ne savez pas trop quoi faire pour votre proche ?",
            "20. Sentir que vous devriez en faire plus pour votre proche ?",
            "21. Sentir que vous pourriez donner de meilleurs soins a votre proche ?",
            "22. En fin de compte, sentez-vous que les soins sont une charge, un fardeau ?"
        ]

        cols_x = [30, 315, 365, 415, 465, 515, 565]

        def draw_table_header(p, y_pos):
            p.draw_rect(fitz.Rect(30, y_pos, 565, y_pos+35), color=text_dark, fill=blue_dark)
            p.insert_text(fitz.Point(38, y_pos+16), clean("A quelle frequence vous arrive-t-il de..."), fontsize=9, color=(1, 1, 1), fontname="helv")
            headers = ["Jamais", "Rarement", "Quelques-", "Assez", "Presque"]
            headers_sub = ["(0)", "(1)", "fois (2)", "souvent (3)", "toujours (4)"]
            for idx in range(5):
                cx1 = cols_x[idx+1]
                cx2 = cols_x[idx+2]
                center_x = cx1 + (cx2 - cx1)/2
                p.insert_text(fitz.Point(center_x-15, y_pos+14), clean(headers[idx]), fontsize=7.5, color=(1, 1, 1), fontname="helv")
                p.insert_text(fitz.Point(center_x-12, y_pos+25), clean(headers_sub[idx]), fontsize=7, color=(0.8, 0.9, 1), fontname="helv")
                p.draw_line(fitz.Point(cx1, y_pos), fitz.Point(cx1, y_pos+35), color=(0.3, 0.4, 0.5), width=0.5)
            return y_pos + 35

        # PAGE 1 : Header + Informations + Questions 1 à 11
        page1 = doc.new_page(width=595, height=842)
        page1.draw_rect(fitz.Rect(30, 25, 565, 80), color=None, fill=blue_dark)
        page1.insert_text(fitz.Point(45, 48), clean("GRILLE DE ZARIT - ECHELLE D'EVALUATION DU FARDEAU"), fontsize=12, color=(1, 1, 1), fontname="helv")
        page1.insert_text(fitz.Point(45, 66), clean("Echelle de penibilite et d'evaluation de la charge de l'aidant principal"), fontsize=9, color=(0.8, 0.9, 1), fontname="helv")

        page1.draw_rect(fitz.Rect(30, 90, 565, 130), color=gray_border, fill=gray_light, width=0.5)
        page1.insert_text(fitz.Point(40, 107), clean(f"Senior : {senior_nom}"), fontsize=9.5, color=text_dark, fontname="helv")
        page1.insert_text(fitz.Point(230, 107), clean(f"Aidant : {aidant_nom}"), fontsize=9.5, color=text_dark, fontname="helv")
        page1.insert_text(fitz.Point(420, 107), clean(f"Date : {date_str}"), fontsize=9, color=text_dark, fontname="helv")

        y = 145
        y = draw_table_header(page1, y)

        row_h = 28
        for i in range(11):
            y_end = y + row_h
            bg_fill = gray_light if i % 2 == 1 else (1, 1, 1)
            page1.draw_rect(fitz.Rect(30, y, 565, y_end), color=gray_border, fill=bg_fill, width=0.5)
            for cx in cols_x[1:-1]:
                page1.draw_line(fitz.Point(cx, y), fitz.Point(cx, y_end), color=gray_border, width=0.5)
            
            q_txt = clean(questions[i])
            rect_q = fitz.Rect(34, y+2, 310, y_end-2)
            page1.insert_textbox(rect_q, q_txt, fontsize=7.5, color=text_dark, fontname="helv")

            ans_val = reponses[i]
            if 0 <= ans_val <= 4:
                cx1 = cols_x[ans_val+1]
                cx2 = cols_x[ans_val+2]
                center_x = cx1 + (cx2 - cx1)/2 - 4
                page1.insert_text(fitz.Point(center_x, y+18), "X", fontsize=11, color=amber_color, fontname="helv")
            
            y = y_end

        # Footer Page 1
        page1.insert_text(fitz.Point(30, 820), clean("ORIA - Grille de Zarit (Evaluation du Fardeau) | Page 1 / 2"), fontsize=8, color=(148/255, 163/255, 184/255), fontname="helv")

        # PAGE 2 : Header tableau + Questions 12 à 22 + Totaux + Résultats
        page2 = doc.new_page(width=595, height=842)
        y = 35
        y = draw_table_header(page2, y)

        for i in range(11, 22):
            y_end = y + row_h
            bg_fill = gray_light if i % 2 == 1 else (1, 1, 1)
            page2.draw_rect(fitz.Rect(30, y, 565, y_end), color=gray_border, fill=bg_fill, width=0.5)
            for cx in cols_x[1:-1]:
                page2.draw_line(fitz.Point(cx, y), fitz.Point(cx, y_end), color=gray_border, width=0.5)

            q_txt = clean(questions[i])
            rect_q = fitz.Rect(34, y+2, 310, y_end-2)
            page2.insert_textbox(rect_q, q_txt, fontsize=7.5, color=text_dark, fontname="helv")

            ans_val = reponses[i]
            if 0 <= ans_val <= 4:
                cx1 = cols_x[ans_val+1]
                cx2 = cols_x[ans_val+2]
                center_x = cx1 + (cx2 - cx1)/2 - 4
                page2.insert_text(fitz.Point(center_x, y+18), "X", fontsize=11, color=amber_color, fontname="helv")

            y = y_end

        # Sous-totaux Row
        y_end = y + 22
        page2.draw_rect(fitz.Rect(30, y, 565, y_end), color=text_dark, fill=gray_light, width=0.8)
        page2.insert_text(fitz.Point(40, y+15), clean("Sous-totaux (points par colonne)"), fontsize=8.5, color=text_dark, fontname="helv")
        
        subtotals = [0]*5
        for idx in range(22):
            val = reponses[idx]
            if 0 <= val <= 4:
                subtotals[val] += val

        for val_col in range(5):
            cx1 = cols_x[val_col+1]
            cx2 = cols_x[val_col+2]
            center_x = cx1 + (cx2 - cx1)/2 - 6
            page2.draw_line(fitz.Point(cx1, y), fitz.Point(cx1, y_end), color=text_dark, width=0.8)
            page2.insert_text(fitz.Point(center_x, y+15), str(subtotals[val_col]), fontsize=9, color=text_dark, fontname="helv")
        y = y_end + 10

        # TOTAL Row
        y_end = y + 30
        page2.draw_rect(fitz.Rect(30, y, 565, y_end), color=blue_dark, fill=blue_dark)
        page2.insert_text(fitz.Point(45, y+19), clean("TOTAL SCORE ZARIT (addition de tous les sous-totaux) :"), fontsize=10, color=(1, 1, 1), fontname="helv")
        page2.insert_text(fitz.Point(450, y+20), clean(f"{total_score} / 88"), fontsize=14, color=amber_color, fontname="helv")
        y = y_end + 20

        # Resultats & Interpretation Box
        page2.insert_text(fitz.Point(30, y), clean("RESULTATS ET INTERPRETATION DU FARDEAU :"), fontsize=10, color=text_dark, fontname="helv")
        y += 12

        cats = [
            ("Score <= 20 : Charge faible", "Tout va bien pour vous.", total_score <= 20),
            ("Score 21 a 40 : Charge legere", "Vous semblez maitriser la situation.", 21 <= total_score <= 40),
            ("Score 41 a 60 : Charge moderee", "La fatigue peut vite survenir, aides requises.", 41 <= total_score <= 60),
            ("Score > 60 : Charge severe", "Attention a l'epuisement, demander de l'aide.", total_score > 60)
        ]

        for title, desc, is_active in cats:
            y_end = y + 25
            fill_c = (254/255, 243/255, 199/255) if is_active else (248/255, 250/255, 252/255)
            border_c = amber_color if is_active else gray_border
            page2.draw_rect(fitz.Rect(30, y, 565, y_end), color=border_c, fill=fill_c, width=1.2 if is_active else 0.5)
            
            mark = "[X] " if is_active else "[  ] "
            page2.insert_text(fitz.Point(40, y+16), clean(mark + title), fontsize=9, color=text_dark if not is_active else (180/255, 83/255, 9/255), fontname="helv")
            page2.insert_text(fitz.Point(260, y+16), clean(desc), fontsize=8.5, color=(71/255, 85/255, 105/255), fontname="helv")
            y = y_end + 5

        # Footer Page 2
        page2.insert_text(fitz.Point(30, 820), clean("ORIA - Grille de Zarit (Evaluation du Fardeau) | Page 2 / 2"), fontsize=8, color=(148/255, 163/255, 184/255), fontname="helv")

        out_pdf = io.BytesIO()
        doc.save(out_pdf)
        doc.close()
        return out_pdf.getvalue()
