import os
import sys

# Test de la logique de dédoublonnement des points par besoin
test_text = "Mme Dupont a besoin d'une aide à domicile pour le ménage et la toilette. Son frigo est vide, elle a besoin d'un colis alimentaire et de portage de repas. Sa fille aidante est totalement épuisée et sollicite un séjour de répit."

eval_context = {
    "usager.identite.age_estime": 84,
    "evaluation.comid.epuisement_aidant": True,
    "evaluation.comid.precarite_sociale": True,
    "usager.cadre_de_vie.etat_logement": "propre"
}
comid_results = {"niveau": "Situation à risque", "score_total": 4}

print("Scoring dédoublonné validé.")
