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
    //const jsonOutput = document.getElementById('raw-json-output');

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
            resScore.textContent = `${data.evaluation_complexe.score_total} / ${Object.keys(COMID_LABELS).length}`;
            resLevel.textContent = data.evaluation_complexe.label;
            resCommune.textContent = schemaPivot["usager.localisation.commune_residence"] || "Non spécifiée";
            resLevel.className = 'kpi-value ' + getComplexityClass(data.evaluation_complexe.score_total);

            // Données JSON brutes
            //jsonOutput.textContent = JSON.stringify(schemaPivot, null, 2);

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
                <!--<span class="priority-badge">Indice de Priorité : <strong>${struct.priorite}</strong></span>-->
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
                    <button id="btn-validate-yes" class="btn-success">
                        <span>✅ Oui, elle convient</span>
                    </button>
                    <button onclick="proposeNextOrientation()" class="btn-warning-action">
                        <span>❌ Non, autre solution</span>
                    </button>
                </div>
            </div>
        `;

        structuresList.appendChild(card);

        // Liaison programmatic event for Yes validation button (avoids quote escaping issues with labels like d'Appui)
        const btnYes = card.querySelector('#btn-validate-yes');
        if (btnYes) {
            btnYes.addEventListener('click', () => {
                handleOuiElleConvient(struct.label, struct.structure_type);
            });
        }

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
    /**
     * Valide l'orientation en cours auprès de l'API FastApi
     */
    window.validateCurrentOrientation = async function(label, type, options = {}) {
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
            
            let pdfButtonHtml = '';
            if (options && options.showDacPdf) {
                pdfButtonHtml = `
                    <button onclick="downloadDacPdf()" class="btn-primary" style="background: var(--accent-blue); box-shadow: 0 4px 12px rgba(74, 109, 245, 0.3); margin-top: 1rem; margin-left: 0.5rem;">
                        📄 Visualiser la fiche d'orientation DAC
                    </button>
                `;
            } else if (options && options.showClicPdf) {
                pdfButtonHtml = `
                    <button onclick="downloadClicPdf()" class="btn-primary" style="background: #0ea5e9; box-shadow: 0 4px 12px rgba(14, 165, 233, 0.3); margin-top: 1rem; margin-left: 0.5rem;">
                        📄 Visualiser la fiche d'orientation CLIC La Seyne
                    </button>
                `;
            } else if (options && options.showClicToulonPdf) {
                pdfButtonHtml = `
                    <button onclick="downloadClicToulonPdf()" class="btn-primary" style="background: #38bdf8; box-shadow: 0 4px 12px rgba(56, 189, 248, 0.3); margin-top: 1rem; margin-left: 0.5rem;">
                        📄 Visualiser la fiche d'orientation CLIC Toulon
                    </button>
                `;
            }

            structuresList.innerHTML = `
                <div class="success-card fadeInUp">
                    <div class="success-icon">🎉</div>
                    <h4 style="font-size: 1.2rem; font-weight: 700; color: #22c55e;">Dossier Validé & Enregistré</h4>
                    <p style="color: var(--text-secondary); max-width: 480px; font-size: 0.92rem; line-height: 1.5; margin: 0 auto;">
                        L'orientation finale vers <strong>${label}</strong> a été enregistrée avec succès. Les données de diagnostic pivot et de traçabilité COMID sont sauvegardées dans votre base locale.
                    </p>
                    <div style="display: flex; justify-content: center; gap: 0.5rem; flex-wrap: wrap;">
                        <button onclick="resetAnalysis()" class="btn-primary" style="background: #22c55e; box-shadow: 0 4px 12px rgba(34, 197, 94, 0.3); margin-top: 1rem;">
                            Traiter un nouveau cas
                        </button>
                        ${pdfButtonHtml}
                    </div>
                </div>
            `;

        } catch (error) {
            console.error(error);
            alert("Erreur lors de la sauvegarde de la validation.");
        }
    };

    /**
     * Intercepte la validation pour le type DAC pour poser les questions de fiche
     */
    window.handleOuiElleConvient = function(label, type) {
        if (type === 'DAC') {
            window.showDacWizard(label, type);
        } else if (type === 'CLIC' && (label.toLowerCase().includes('seyne') || (schemaPivot && schemaPivot["usager.localisation.commune_residence"] && schemaPivot["usager.localisation.commune_residence"].toLowerCase().includes('seyne')))) {
            window.showClicWizard(label, type);
        } else if (type === 'CLIC' && (label.toLowerCase().includes('toulon') || (schemaPivot && schemaPivot["usager.localisation.commune_residence"] && schemaPivot["usager.localisation.commune_residence"].toLowerCase().includes('toulon')))) {
            window.showClicToulonWizard(label, type);
        } else {
            window.validateCurrentOrientation(label, type);
        }
    };

    function ensureWizardStyles() {
        if (!document.getElementById('dac-modal-styles')) {
            const style = document.createElement('style');
            style.id = 'dac-modal-styles';
            style.textContent = `
                .modal-overlay {
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background: rgba(15, 23, 42, 0.4);
                    backdrop-filter: blur(8px);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    z-index: 1000;
                    animation: modalFadeIn 0.25s ease-out;
                }
                .modal-card {
                    background: var(--bg-secondary, #ffffff);
                    border: 1px solid var(--border-glass, rgba(74, 109, 245, 0.3));
                    border-radius: var(--radius, 16px);
                    padding: 2.25rem;
                    max-width: 500px;
                    width: 90%;
                    box-shadow: 0 20px 40px rgba(15, 23, 42, 0.15), var(--shadow-glow, 0 0 24px rgba(74, 109, 245, 0.15));
                    animation: modalScaleUp 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
                    display: flex;
                    flex-direction: column;
                    gap: 1.5rem;
                }
                @keyframes modalFadeIn {
                    from { opacity: 0; }
                    to { opacity: 1; }
                }
                @keyframes modalScaleUp {
                    from { transform: scale(0.9); opacity: 0; }
                    to { transform: scale(1); opacity: 1; }
                }
                .modal-header {
                    display: flex;
                    align-items: center;
                    gap: 0.75rem;
                }
                .modal-logo {
                    font-size: 2rem;
                }
                .modal-header h3 {
                    font-size: 1.25rem;
                    font-weight: 700;
                    color: var(--text-primary);
                    margin: 0;
                }
                .modal-body {
                    font-size: 0.98rem;
                    color: var(--text-secondary);
                    line-height: 1.6;
                }
                .modal-footer {
                    display: flex;
                    justify-content: flex-end;
                    gap: 1rem;
                }
                .btn-modal-primary {
                    background: linear-gradient(135deg, var(--accent-blue, #4a6df5) 0%, var(--accent-purple, #234cb3) 100%);
                    color: #ffffff;
                    border: none;
                    border-radius: var(--radius-sm, 10px);
                    padding: 0.75rem 1.5rem;
                    font-family: 'Inter', sans-serif;
                    font-weight: 600;
                    font-size: 0.95rem;
                    cursor: pointer;
                    transition: all 0.2s;
                    box-shadow: 0 4px 12px rgba(74, 109, 245, 0.2);
                }
                .btn-modal-primary:hover {
                    transform: translateY(-1px);
                    box-shadow: 0 6px 16px rgba(74, 109, 245, 0.4);
                }
                .btn-modal-secondary {
                    background: rgba(15, 23, 42, 0.05);
                    color: var(--text-secondary);
                    border: 1px solid var(--border-glass, rgba(74, 109, 245, 0.3));
                    border-radius: var(--radius-sm, 10px);
                    padding: 0.75rem 1.5rem;
                    font-family: 'Inter', sans-serif;
                    font-weight: 600;
                    font-size: 0.95rem;
                    cursor: pointer;
                    transition: all 0.2s;
                }
                .btn-modal-secondary:hover {
                    background: rgba(15, 23, 42, 0.1);
                    color: var(--text-primary);
                }
            `;
            document.head.appendChild(style);
        }
    }

    /**
     * Gère le questionnaire pas-à-pas DAC
     */
    window.showDacWizard = function(label, type) {
        let modal = document.getElementById('dac-wizard-modal');
        if (!modal) {
            modal = document.createElement('div');
            modal.id = 'dac-wizard-modal';
            modal.className = 'modal-overlay';
            document.body.appendChild(modal);
        }
        
        ensureWizardStyles();

        showStep1(modal, label, type);
    };

    function showStep1(modal, label, type) {
        modal.style.display = 'flex';
        modal.innerHTML = `
            <div class="modal-card">
                <div class="modal-header">
                    <span class="modal-logo">🧭</span>
                    <h3>Fiche d'Orientation DAC</h3>
                </div>
                <div class="modal-body">
                    <p style="margin-bottom: 0.75rem; font-weight: 600; color: var(--accent-blue);">Orientation détectée : ${label}</p>
                    <p>Voulez-vous remplir la fiche d'orientation du DAC ?</p>
                </div>
                <div class="modal-footer">
                    <button id="btn-step1-non" class="btn-modal-secondary">Non</button>
                    <button id="btn-step1-oui" class="btn-modal-primary">Oui</button>
                </div>
            </div>
        `;

        document.getElementById('btn-step1-non').onclick = () => {
            modal.style.display = 'none';
            // Non = normal validation as before
            window.validateCurrentOrientation(label, type);
        };

        document.getElementById('btn-step1-oui').onclick = () => {
            showStep2(modal, label, type);
        };
    }

    function showStep2(modal, label, type) {
        modal.innerHTML = `
            <div class="modal-card">
                <div class="modal-header">
                    <span class="modal-logo">📋</span>
                    <h3>Fiche d'Orientation DAC</h3>
                </div>
                <div class="modal-body">
                    <p>Voulez-vous remplir les informations manquantes ?</p>
                </div>
                <div class="modal-footer">
                    <button id="btn-step2-non" class="btn-modal-secondary">Non</button>
                    <button id="btn-step2-oui" class="btn-modal-primary">Oui</button>
                </div>
            </div>
        `;

        document.getElementById('btn-step2-non').onclick = () => {
            modal.style.display = 'none';
            // Non = validate and show success with visualising button (semi-filled with current info)
            window.validateCurrentOrientation(label, type, { showDacPdf: true });
        };

        document.getElementById('btn-step2-oui').onclick = () => {
            modal.innerHTML = `
                <div class="modal-card">
                    <div class="modal-header">
                        <span class="modal-logo">💡</span>
                        <h3>Saisie à venir</h3>
                    </div>
                    <div class="modal-body">
                        <p style="margin-bottom: 0.75rem;">Le module de saisie des informations manquantes sera disponible prochainement.</p>
                        <p>La fiche d'orientation va être visualisée avec les informations déjà extraites et présentes.</p>
                    </div>
                    <div class="modal-footer">
                        <button id="btn-step2-oui-continue" class="btn-modal-primary" style="width: 100%;">Visualiser la fiche</button>
                    </div>
                </div>
            `;
            document.getElementById('btn-step2-oui-continue').onclick = () => {
                modal.style.display = 'none';
                window.validateCurrentOrientation(label, type, { showDacPdf: true });
            };
        };
    }

    /**
     * Gère le questionnaire pas-à-pas CLIC
     */
    window.showClicWizard = function(label, type) {
        let modal = document.getElementById('dac-wizard-modal'); // on réutilise la modale DAC
        if (!modal) {
            modal = document.createElement('div');
            modal.id = 'dac-wizard-modal';
            modal.className = 'modal-overlay';
            document.body.appendChild(modal);
        }
        
        ensureWizardStyles();
        showClicStep1(modal, label, type);
    };

    function showClicStep1(modal, label, type) {
        modal.style.display = 'flex';
        modal.innerHTML = `
            <div class="modal-card">
                <div class="modal-header">
                    <span class="modal-logo">🧭</span>
                    <h3>Fiche d'Orientation CLIC</h3>
                </div>
                <div class="modal-body">
                    <p style="margin-bottom: 0.75rem; font-weight: 600; color: #0ea5e9;">Orientation détectée : ${label}</p>
                    <p>Voulez-vous remplir la fiche d'orientation du CLIC de La Seyne-sur-Mer ?</p>
                </div>
                <div class="modal-footer">
                    <button id="btn-clic-step1-non" class="btn-modal-secondary">Non</button>
                    <button id="btn-clic-step1-oui" class="btn-modal-primary" style="background: linear-gradient(135deg, #38bdf8 0%, #0ea5e9 100%);">Oui</button>
                </div>
            </div>
        `;

        document.getElementById('btn-clic-step1-non').onclick = () => {
            modal.style.display = 'none';
            window.validateCurrentOrientation(label, type);
        };

        document.getElementById('btn-clic-step1-oui').onclick = () => {
            showClicStep2(modal, label, type);
        };
    }

    function showClicStep2(modal, label, type) {
        modal.innerHTML = `
            <div class="modal-card">
                <div class="modal-header">
                    <span class="modal-logo">💡</span>
                    <h3>Saisie à venir</h3>
                </div>
                <div class="modal-body">
                    <p style="margin-bottom: 0.75rem;">Le module de saisie des informations manquantes pour le CLIC sera disponible prochainement.</p>
                    <p>La fiche d'orientation va être générée avec les informations déjà extraites et présentes.</p>
                </div>
                <div class="modal-footer">
                    <button id="btn-clic-step2-oui-continue" class="btn-modal-primary" style="background: linear-gradient(135deg, #38bdf8 0%, #0ea5e9 100%); width: 100%;">Visualiser la fiche</button>
                </div>
            </div>
        `;
        document.getElementById('btn-clic-step2-oui-continue').onclick = () => {
            modal.style.display = 'none';
            window.validateCurrentOrientation(label, type, { showClicPdf: true });
        };
    }

    /**
     * Gère le questionnaire pas-à-pas CLIC Toulon
     */
    window.showClicToulonWizard = function(label, type) {
        let modal = document.getElementById('dac-wizard-modal');
        if (!modal) {
            modal = document.createElement('div');
            modal.id = 'dac-wizard-modal';
            modal.className = 'modal-overlay';
            document.body.appendChild(modal);
        }
        ensureWizardStyles();
        showClicToulonStep1(modal, label, type);
    };

    function showClicToulonStep1(modal, label, type) {
        modal.style.display = 'flex';
        modal.innerHTML = `
            <div class="modal-card">
                <div class="modal-header">
                    <span class="modal-logo">🧭</span>
                    <h3>Fiche d'Orientation CLIC Toulon</h3>
                </div>
                <div class="modal-body">
                    <p style="margin-bottom: 0.75rem; font-weight: 600; color: #0ea5e9;">Orientation détectée : ${label}</p>
                    <p>Voulez-vous remplir la fiche d'orientation du CLIC de Toulon ?</p>
                </div>
                <div class="modal-footer">
                    <button id="btn-clic-toulon-step1-non" class="btn-modal-secondary">Non</button>
                    <button id="btn-clic-toulon-step1-oui" class="btn-modal-primary" style="background: linear-gradient(135deg, #38bdf8 0%, #0ea5e9 100%);">Oui</button>
                </div>
            </div>
        `;

        document.getElementById('btn-clic-toulon-step1-non').onclick = () => {
            modal.style.display = 'none';
            window.validateCurrentOrientation(label, type);
        };

        document.getElementById('btn-clic-toulon-step1-oui').onclick = () => {
            showClicToulonStep2(modal, label, type);
        };
    }

    function showClicToulonStep2(modal, label, type) {
        modal.innerHTML = `
            <div class="modal-card">
                <div class="modal-header">
                    <span class="modal-logo">📋</span>
                    <h3>Fiche d'Orientation CLIC Toulon</h3>
                </div>
                <div class="modal-body">
                    <p>Voulez-vous remplir les informations manquantes ?</p>
                </div>
                <div class="modal-footer">
                    <button id="btn-clic-toulon-step2-non" class="btn-modal-secondary">Non</button>
                    <button id="btn-clic-toulon-step2-oui" class="btn-modal-primary" style="background: linear-gradient(135deg, #38bdf8 0%, #0ea5e9 100%);">Oui</button>
                </div>
            </div>
        `;

        document.getElementById('btn-clic-toulon-step2-non').onclick = () => {
            modal.style.display = 'none';
            window.validateCurrentOrientation(label, type, { showClicToulonPdf: true });
        };

        document.getElementById('btn-clic-toulon-step2-oui').onclick = () => {
            showClicToulonStep3(modal, label, type);
        };
    }

    function showClicToulonStep3(modal, label, type) {
        modal.innerHTML = `
            <div class="modal-card">
                <div class="modal-header">
                    <span class="modal-logo">💡</span>
                    <h3>Saisie à venir</h3>
                </div>
                <div class="modal-body">
                    <p style="margin-bottom: 0.75rem;">Le module de saisie des informations manquantes pour le CLIC de Toulon sera disponible prochainement.</p>
                    <p>La fiche d'orientation va être générée avec les informations déjà extraites et présentes.</p>
                </div>
                <div class="modal-footer">
                    <button id="btn-clic-toulon-step3-continue" class="btn-modal-primary" style="background: linear-gradient(135deg, #38bdf8 0%, #0ea5e9 100%); width: 100%;">Visualiser la fiche</button>
                </div>
            </div>
        `;
        document.getElementById('btn-clic-toulon-step3-continue').onclick = () => {
            modal.style.display = 'none';
            window.validateCurrentOrientation(label, type, { showClicToulonPdf: true });
        };
    }

    /**
     * Télécharge la fiche d'orientation DAC sous format PDF
     */
    window.downloadDacPdf = async function() {
        const text = document.getElementById('situation-input').value.trim();
        if (!text) return;

        const btn = document.querySelector('[onclick="downloadDacPdf()"]');
        let originalHtml = "";
        if (btn) {
            originalHtml = btn.innerHTML;
            btn.innerHTML = `<span>⏳ Remplissage...</span>`;
            btn.disabled = true;
        }

        try {
            const response = await fetch('/api/orientation/dac/generate_pdf', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: text })
            });

            if (!response.ok) {
                throw new Error("Erreur de téléchargement");
            }

            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'fiche_orientation_dac.pdf';
            document.body.appendChild(a);
            a.click();
            a.remove();
            window.URL.revokeObjectURL(url);
        } catch (err) {
            console.error(err);
            alert("Une erreur est survenue lors de la génération du PDF.");
        } finally {
            if (btn) {
                btn.innerHTML = originalHtml;
                btn.disabled = false;
            }
        }
    };

    /**
     * Télécharge la fiche d'orientation CLIC La Seyne sous format PDF
     */
    window.downloadClicPdf = async function() {
        const text = document.getElementById('situation-input').value.trim();
        if (!text) return;

        const btn = document.querySelector('[onclick="downloadClicPdf()"]');
        let originalHtml = "";
        if (btn) {
            originalHtml = btn.innerHTML;
            btn.innerHTML = `<span>⏳ Remplissage...</span>`;
            btn.disabled = true;
        }

        try {
            const response = await fetch('/api/orientation/clic/generate_pdf', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: text })
            });

            if (!response.ok) {
                throw new Error("Erreur de téléchargement");
            }

            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'fiche_orientation_clic_laseyne.pdf';
            document.body.appendChild(a);
            a.click();
            a.remove();
            window.URL.revokeObjectURL(url);
        } catch (err) {
            console.error(err);
            alert("Une erreur est survenue lors de la génération du PDF CLIC.");
        } finally {
            if (btn) {
                btn.innerHTML = originalHtml;
                btn.disabled = false;
            }
        }
    };

    /**
     * Télécharge la fiche d'orientation CLIC Toulon sous format PDF
     */
    window.downloadClicToulonPdf = async function() {
        const text = document.getElementById('situation-input').value.trim();
        if (!text) return;

        const btn = document.querySelector('[onclick="downloadClicToulonPdf()"]');
        let originalHtml = "";
        if (btn) {
            originalHtml = btn.innerHTML;
            btn.innerHTML = `<span>⏳ Remplissage...</span>`;
            btn.disabled = true;
        }

        try {
            const response = await fetch('/api/orientation/clic_toulon/generate_pdf', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: text })
            });

            if (!response.ok) {
                throw new Error("Erreur de téléchargement");
            }

            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'fiche_orientation_clic_toulon.pdf';
            document.body.appendChild(a);
            a.click();
            a.remove();
            window.URL.revokeObjectURL(url);
        } catch (err) {
            console.error(err);
            alert("Une erreur est survenue lors de la génération du PDF CLIC Toulon.");
        } finally {
            if (btn) {
                btn.innerHTML = originalHtml;
                btn.disabled = false;
            }
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
