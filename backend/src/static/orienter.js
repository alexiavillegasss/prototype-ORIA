// Couleurs des badges de structure pour garder une cohérence visuelle haut de gamme
const STRUCTURE_COLORS = {
    'CRT': '#a78bfa',
    'CEV': '#f87171',
    'PSCG_SS_APA': '#c084fc',
    'CLIC': '#38bdf8',
    'UTS': '#2dd4bf',
    'CCAS': '#34d399',
    'DAC': '#fb923c',
    'CPTS': '#fbbf24',
    'SERVICE_SOCIAL_HOPITAL': '#fb7185',
    'POLICE': '#3b82f6'
};

// Dictionnaire complet des 30 critères COMID pour la traçabilité clinique dans l'interface
const COMID_LABELS = {
    'multimorbidite': 'Multimorbidité (≥ 3 pathologies chroniques)',
    'douleurs': 'Douleurs chroniques ou mal contrôlées',
    'allergies': 'Allergies complexes ou sévères',
    'polymedication': 'Polymédication (≥ 5 médicaments distincts)',
    'troubles_cognitifs': 'Troubles cognitifs (Alzheimer ou apparentés)',
    'precarite_financiere': 'Précarité financière / Ressources faibles',
    'epuisement_aidant': 'Épuisement critique de l\'aidant régulier',
    'litteratie_faible': 'Faible littératie en santé / Barrière de langue',
    'isolement_social': 'Isolement social ou familial prononcé',
    'logement_inadapte': 'Logement inadapté ou insalubre (ex: incurie)',
    'depression': 'Troubles de l\'humeur, dépression avérée',
    'psychiatrie': 'Suivi psychiatrique ou trouble psy actif',
    'addiction': 'Addiction ou dépendance (alcool, substances)',
    'anxiete': 'Anxiété majeure ou angoisses exprimées',
    'fluctuation_mentale': 'Fluctuations rapides de l\'état mental',
    'sollicitations_recurrentes': 'Sollicitations récurrentes (urgences / médecins)',
    'conflit_reseau': 'Conflit au sein du réseau d\'intervenants',
    'inquietude_sante': 'Inquiétude majeure pour sa propre santé',
    'agressivite': 'Agressivité ou hostilité verbale/physique',
    'opposition_soins': 'Refus de soins ou d\'aide active à domicile',
    'degradation_recente': 'Dégradation rapide de la situation (< 1 mois)',
    'perte_autonomie_recente': 'Perte d\'autonomie motrice ou physique récente',
    'transition_parcours': 'Rupture ou transition de parcours (sortie hôpital)',
    'trouble_cognitif_aigu': 'Confusion ou trouble cognitif aigu récent',
    'imprevisibilite': 'Grande imprévisibilité de l\'état de santé',
    'multitude_intervenants': 'Multitude d\'intervenants sans coordination',
    'manque_partenariat': 'Manque de partenariat ou rupture avec les pro',
    'incoherence_soins': 'Incohérence majeure dans le plan de soins',
    'probleme_assurance': 'Difficultés de couverture d\'assurance maladie',
    'lourdeur_reseau': 'Lourdeur administrative ou réseau complexe'
};

// Variables d'état globales de la session de diagnostic
let orientations = [];
let currentIndex = 0;
let dossierId = null;
let schemaPivot = null;

document.addEventListener('DOMContentLoaded', () => {
    const btnSubmit = document.getElementById('btn-submit');
    const inputArea = document.getElementById('situation-input');
    const spinner = document.getElementById('btn-spinner');
    
    const placeholder = document.getElementById('results-placeholder');
    const resultsContent = document.getElementById('results-content');
    
    // Champs de diagnostic global
    const resScore = document.getElementById('res-score');
    const resLevel = document.getElementById('res-level');
    const resCommune = document.getElementById('res-commune');
    const structuresTitle = document.getElementById('structures-title');
    const structuresList = document.getElementById('structures-list');
    const jsonOutput = document.getElementById('raw-json-output');

    btnSubmit.addEventListener('click', async () => {
        const text = inputArea.value.trim();
        if (!text) {
            alert("Veuillez saisir la description d'une situation avant de lancer l'analyse.");
            return;
        }

        // 1. Passage en état de chargement
        btnSubmit.disabled = true;
        spinner.style.display = 'inline-block';
        btnSubmit.querySelector('.btn-text').textContent = 'Analyse IA en cours (Ollama)...';

        try {
            // 2. Appel à l'API /analyze de FastAPI
            const response = await fetch('/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: text })
            });

            if (!response.ok) {
                throw new Error("Erreur serveur lors de l'analyse.");
            }

            const data = await response.json();

            if (data.error) {
                alert("Erreur de l'extraction IA : " + data.error);
                return;
            }

            // 3. Initialisation de l'état local
            orientations = data.orientation_suggeree || [];
            currentIndex = 0;
            dossierId = data.id_dossier;
            schemaPivot = data.schema_pivot;

            // Remplissage des KPIs globaux
            resScore.textContent = `${data.evaluation_complexe.score_total} / 20`;
            resLevel.textContent = data.evaluation_complexe.label;
            resCommune.textContent = schemaPivot["usager.localisation.commune_residence"] || "Non spécifiée";
            resLevel.className = 'kpi-value ' + getComplexityClass(data.evaluation_complexe.score_total);

            // Données JSON brutes
            jsonOutput.textContent = JSON.stringify(schemaPivot, null, 2);

            // Affichage de l'interface de résultat
            placeholder.style.display = 'none';
            resultsContent.style.display = 'block';

            // 4. Rendu de l'orientation courante
            renderOrientation();

        } catch (error) {
            console.error(error);
            alert("Une erreur est survenue lors de l'analyse du cas. Vérifiez que votre serveur local et Ollama sont bien actifs.");
        } finally {
            btnSubmit.disabled = false;
            spinner.style.display = 'none';
            btnSubmit.querySelector('.btn-text').textContent = 'Lancer l\'Analyse';
        }
    });

    /**
     * Rentre l'orientation courante ou l'état de fallback si aucune n'est disponible
     */
    window.renderOrientation = function() {
        structuresList.innerHTML = '';
        
        // S'il n'y a aucune structure éligible ou qu'on a épuisé la liste
        if (orientations.length === 0 || currentIndex >= orientations.length) {
            structuresTitle.textContent = "Recherche d'informations supplémentaires :";
            structuresList.innerHTML = `
                <div class="empty-state card fadeInUp" style="padding: 2.5rem; text-align: center; border: 1px dashed var(--accent-purple); border-radius: var(--radius);">
                    <div class="empty-icon" style="font-size: 3rem; margin-bottom: 1rem;">🧭</div>
                    <h4 style="font-size: 1.15rem; font-weight: 600; color: var(--text-primary); margin-bottom: 0.75rem;">Plus d'informations cliniques requises</h4>
                    <p style="color: var(--text-secondary); margin-bottom: 1.5rem; line-height: 1.5; font-size: 0.92rem;">
                        Aucune autre structure d'orientation n'est disponible pour ce cas. Afin d'affiner le diagnostic et de débloquer de nouvelles éligibilités, veuillez enrichir votre description de situation clinique à gauche (précisez si chute récente, dénutrition, épuisement de l'aidant régulier, hospitalisation, ou opposition aux aides).
                    </p>
                    <button onclick="focusInput()" class="btn-primary" style="margin: 0 auto; max-width: 250px;">Modifier la description</button>
                </div>
            `;
            return;
        }

        // On extrait l'orientation courante
        const struct = orientations[currentIndex];
        structuresTitle.textContent = `Proposition d'orientation (${currentIndex + 1} sur ${orientations.length}) :`;

        const card = document.createElement('div');
        card.className = 'struct-card fadeInUp';
        const color = STRUCTURE_COLORS[struct.structure_type] || '#64748b';

        card.innerHTML = `
            <div class="struct-card-header">
                <span class="struct-badge" style="background-color: ${color}20; color: ${color}; border: 1px solid ${color}40;">
                    ${struct.structure_type}
                </span>
                <span class="priority-badge">Indice de Priorité : <strong>${struct.priorite}</strong></span>
            </div>
            <h4 class="struct-name" style="margin-bottom: 0.75rem;">${struct.label}</h4>
            <p class="struct-objective" style="margin-bottom: 1.25rem;"><strong>Mission de la structure :</strong> ${struct.objectif || 'Non renseigné'}</p>
            
            <!-- Bouton "Pourquoi ?" -->
            <button id="btn-why" class="btn-explain">
                <span class="icon">🔍</span> Pourquoi cette orientation ?
            </button>

            <!-- Volet des explications cliniques (masqué par défaut) -->
            <div id="explanation-pane" class="explanation-pane" style="display: none;">
                
                <!-- Section Signaux du Schéma Pivot -->
                <div class="explain-section">
                    <span class="explain-subtitle">Variables clés extraites</span>
                    <div class="signals-grid">
                        <div class="signal-item">
                            <span class="signal-title">Motif principal</span>
                            <span>${schemaPivot["demande.motif_principal"] || 'Maintien standard'}</span>
                        </div>
                        <div class="signal-item">
                            <span class="signal-title">Médecin traitant</span>
                            <span>${formatMedecin(schemaPivot["vulnerabilites.sante.suivi_medical.medecin_traitant"])}</span>
                        </div>
                        <div class="signal-item">
                            <span class="signal-title">Malveillance</span>
                            <span>${formatMalveillance(schemaPivot["usager.situation_actuelle.suspicion_malveillance"])}</span>
                        </div>
                        <div class="signal-item">
                            <span class="signal-title">Hospitalisation</span>
                            <span>${formatHospitalisation(schemaPivot["vulnerabilites.sante.hospitalisation.statut"])}</span>
                        </div>
                    </div>
                </div>

                <!-- Section Critères COMID Justifiés -->
                <div class="explain-section">
                    <span class="explain-subtitle">Preuves COMID avérées (Justifications textuelles)</span>
                    <div class="comid-proof-list" id="comid-proof-list">
                        <!-- Rempli dynamiquement -->
                    </div>
                </div>
            </div>
            
            <!-- Bloc des coordonnées territoriales -->
            <div class="struct-contact" style="margin-top: 1.5rem; margin-bottom: 1.5rem;">
                <div class="contact-item">
                    <span class="icon">📞</span>
                    <span>${struct.telephone || 'Aucun numéro territorial répertorié'}</span>
                </div>
                <div class="contact-item">
                    <span class="icon">📍</span>
                    <span>${struct.adresse || 'Aucune adresse enregistrée pour cette commune'}</span>
                </div>
            </div>

            <!-- Boucle de feedback d'orientation -->
            <div class="feedback-pane">
                <span class="feedback-title">Cette orientation convient-elle à la situation de l'usager ?</span>
                <div class="feedback-buttons">
                    <button onclick="validateCurrentOrientation('${struct.label}', '${struct.structure_type}')" class="btn-success">
                        <span>✅ Oui, elle convient</span>
                    </button>
                    <button onclick="proposeNextOrientation()" class="btn-warning-action">
                        <span>❌ Non, autre solution</span>
                    </button>
                </div>
            </div>
        `;

        structuresList.appendChild(card);

        // Liaison de l'animation de toggle d'explications
        const btnWhy = card.querySelector('#btn-why');
        const explainPane = card.querySelector('#explanation-pane');
        btnWhy.addEventListener('click', () => {
            if (explainPane.style.display === 'none') {
                renderComidJustifications(card.querySelector('#comid-proof-list'));
                explainPane.style.display = 'flex';
                btnWhy.innerHTML = '<span class="icon">✕</span> Masquer les détails';
            } else {
                explainPane.style.display = 'none';
                btnWhy.innerHTML = '<span class="icon">🔍</span> Pourquoi cette orientation ?';
            }
        });
    };

    /**
     * Renseigne les justifications COMID dans le conteneur HTML
     */
    function renderComidJustifications(container) {
        container.innerHTML = '';
        const justifications = schemaPivot["evaluation.comid.justifications"] || [];

        if (justifications.length === 0) {
            container.innerHTML = `
                <div style="font-size: 0.85rem; color: var(--text-muted); font-style: italic;">
                    Aucun facteur de complexité COMID spécifique validé pour ce cas.
                </div>
            `;
            return;
        }

        justifications.forEach(j => {
            const card = document.createElement('div');
            card.className = 'comid-proof-card';
            const label = COMID_LABELS[j.code] || j.code;

            card.innerHTML = `
                <span class="comid-proof-label">📋 ${label}</span>
                <span class="comid-proof-quote">« ${j.justification} »</span>
            `;
            container.appendChild(card);
        });
    }

    /**
     * Valide l'orientation en cours auprès de l'API FastApi
     */
    window.validateCurrentOrientation = async function(label, type) {
        if (!dossierId) return;

        try {
            const response = await fetch(`/api/dossiers/${dossierId}/validate`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    status: `Validé - ${type}`,
                    structure_choisie: label
                })
            });

            if (!response.ok) {
                throw new Error("Erreur de validation.");
            }

            const data = await response.json();

            // Rendu de l'écran de validation finale
            structuresTitle.textContent = "Orientation validée avec succès :";
            structuresList.innerHTML = `
                <div class="success-card fadeInUp">
                    <div class="success-icon">🎉</div>
                    <h4 style="font-size: 1.2rem; font-weight: 700; color: #22c55e;">Dossier Validé & Enregistré</h4>
                    <p style="color: var(--text-secondary); max-width: 480px; font-size: 0.92rem; line-height: 1.5; margin: 0 auto;">
                        L'orientation finale vers <strong>${label}</strong> a été enregistrée avec succès. Les données de diagnostic pivot et de traçabilité COMID sont sauvegardées dans votre base locale.
                    </p>
                    <button onclick="resetAnalysis()" class="btn-primary" style="background: #22c55e; box-shadow: 0 4px 12px rgba(34, 197, 94, 0.3); margin-top: 1rem;">
                        Traiter un nouveau cas
                    </button>
                </div>
            `;

        } catch (error) {
            console.error(error);
            alert("Erreur lors de la sauvegarde de la validation.");
        }
    };

    /**
     * Passe à l'orientation de priorité inférieure
     */
    window.proposeNextOrientation = function() {
        currentIndex++;
        renderOrientation();
    };

    /**
     * Remet le curseur sur le champ de saisie
     */
    window.focusInput = function() {
        inputArea.focus();
    };

    /**
     * Réinitialise l'interface pour un nouveau diagnostic
     */
    window.resetAnalysis = function() {
        inputArea.value = '';
        placeholder.style.display = 'flex';
        resultsContent.style.display = 'none';
        orientations = [];
        currentIndex = 0;
        dossierId = null;
        schemaPivot = null;
        inputArea.focus();
    };
});

/**
 * Attribue une classe CSS en fonction du score COMID
 */
function getComplexityClass(score) {
    if (score <= 5) return 'text-simple';
    if (score <= 10) return 'text-warning';
    return 'text-danger';
}

// Utilitaires de formatage de l'affichage Pivot
function formatMedecin(status) {
    if (status === 'identifie') return 'Identifié (Suivi actif)';
    if (status === 'absent') return 'Absent (Recherche active)';
    return 'Incertain';
}

function formatMalveillance(type) {
    if (type === 'spoliation_financiere') return 'Suspicion de spoliation financière';
    if (type === 'violences_physiques') return 'Suspicion de violences physiques';
    if (type === 'negligence') return 'Suspicion de négligence';
    return 'Aucune suspicion';
}

function formatHospitalisation(status) {
    if (status === 'en_cours') return 'En cours';
    if (status === 'recente') return 'Récente (< 10 jours)';
    return 'Aucune hospitalisation';
}
