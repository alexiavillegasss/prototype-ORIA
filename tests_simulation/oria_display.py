# oria_display.py — Utilitaire d'affichage partagé pour les scripts de test ORIA
# Fournit l'explicabilité : pourquoi chaque structure a été proposée

# Mapping technique → libellé lisible en français
FIELD_LABELS = {
    "usager.situation_actuelle.APA":              "Statut APA",
    "usager.situation_actuelle.PCH":              "Statut PCH",
    "usager.situation_actuelle.GIR":              "Niveau GIR",
    "usager.situation_actuelle.suspicion_malveillance": "Suspicion de malveillance",
    "usager.identite.age_estime":                 "Âge estimé",
    "usager.localisation.commune_residence":       "Commune de résidence",
    "usager.cadre_de_vie.aidant_regulier":        "Aidant régulier",
    "demande.motif_principal":                    "Motif principal de la demande",
    "vulnerabilites.sante.hospitalisation.statut": "Statut d'hospitalisation",
    "vulnerabilites.sante.suivi_medical.medecin_traitant": "Médecin traitant",
    "vulnerabilites.sante.professionnels_domicile": "Professionnels au domicile",
    "vulnerabilites.habitat.securite_du_domicile": "Sécurité du domicile",
    "vulnerabilites.social.precarite":            "Précarité sociale",
    "vulnerabilites.social.isolement_relationnel": "Isolement relationnel",
    "vulnerabilites.social.risque_epuisement_entourage": "Risque épuisement entourage",
    "evaluation.comid.epuisement_aidant":         "Épuisement de l'aidant",
    "evaluation.comid.precarite_financiere":      "Précarité financière",
    "evaluation.comid.isolement_social":          "Isolement social",
    "evaluation.comid.troubles_cognitifs":        "Troubles cognitifs",
    "evaluation.comid.opposition_soins":          "Opposition aux soins",
    "evaluation.comid.logement_inadapte":         "Logement inadapté",
    "evaluation.comid.multimorbidite":            "Multimorbidité",
    "evaluation.comid.psychiatrie":               "Problème psychiatrique",
    "evaluation.comid.addiction":                 "Addiction",
    "evaluation.comid.transition_parcours":       "Transition de parcours",
    "complexite.niveau":                          "Niveau de complexité COMID",
    "complexite.score_total":                     "Score COMID total",
    "adresseur.degre_urgence_percu":              "Urgence perçue",
}

OPERATEUR_LABELS = {
    "==":           "est",
    ">=":           "est >=",
    "<=":           "est <=",
    "in":           "est parmi",
    "not_in":       "n'est pas parmi",
    "contains_any": "contient l'un de",
}


def _format_valeur(valeur):
    if isinstance(valeur, bool):
        return "OUI" if valeur else "NON"
    if valeur is None:
        return "(non renseigné)"
    return f'"{valeur}"'


def _format_attendu(attendu):
    if isinstance(attendu, list):
        if len(attendu) <= 4:
            return "[" + ", ".join(f'"{v}"' for v in attendu) + "]"
        else:
            return "[" + ", ".join(f'"{v}"' for v in attendu[:4]) + f", ... +{len(attendu)-4}]"
    if isinstance(attendu, bool):
        return "OUI" if attendu else "NON"
    return f'"{attendu}"'


def afficher_orientations(results_with_contacts):
    """Affiche les orientations avec leur explication (pourquoi ce choix)."""
    if not results_with_contacts:
        print("Aucune structure eligible detectee.")
        return

    for struct in results_with_contacts:
        print(f"\n{'='*65}")
        print(f"  [ {struct['label']} ]  —  Priorite : {struct.get('priorite', 'N/A')}")
        print(f"{'='*65}")
        print(f"  Objectif : {struct.get('objectif', 'N/A')}")

        # Affichage des contacts
        if struct.get("telephone") or struct.get("adresse"):
            print(f"  Contact  : {struct.get('telephone', 'N/A')} | {struct.get('adresse', 'N/A')}")
        else:
            print("  Contact  : Non trouve dans le referentiel territorial")

        # Affichage de l'explicabilité
        raisons = struct.get("pourquoi", [])
        if raisons:
            print(f"\n  Pourquoi cette orientation :")
            for r in raisons:
                champ_label = FIELD_LABELS.get(r["champ"], r["champ"])
                op_label    = OPERATEUR_LABELS.get(r["operateur"], r["operateur"])
                valeur_str  = _format_valeur(r["valeur"])
                attendu_str = _format_attendu(r["attendu"])
                print(f"    -> {champ_label} = {valeur_str}  ({op_label} {attendu_str})")
        else:
            print("  (Aucune condition explicite enregistree)")
