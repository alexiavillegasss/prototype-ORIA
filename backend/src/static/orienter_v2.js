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
let scoreBreakdown = [];
let currentIndex = 0;
let dossierId = null;
let schemaPivot = null;

document.addEventListener('DOMContentLoaded', () => {
    // Gestion du thème clair/sombre
    const themeToggle = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme') || 'dark';
    
    const iconMoon = `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>`;
    const iconSun = `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>`;
    
    if (currentTheme === 'light') {
        document.documentElement.setAttribute('data-theme', 'light');
        themeToggle.innerHTML = iconMoon; // Affiche la lune pour passer en mode sombre
    } else {
        document.documentElement.removeAttribute('data-theme');
        themeToggle.innerHTML = iconSun; // Affiche le soleil pour passer en mode clair
    }

    themeToggle.addEventListener('click', () => {
        if (document.documentElement.hasAttribute('data-theme')) {
            document.documentElement.removeAttribute('data-theme');
            localStorage.setItem('theme', 'dark');
            themeToggle.innerHTML = iconSun;
        } else {
            document.documentElement.setAttribute('data-theme', 'light');
            localStorage.setItem('theme', 'light');
            themeToggle.innerHTML = iconMoon;
        }
    });

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
            scoreBreakdown = data.score_breakdown || [];
            currentIndex = 0;
            dossierId = data.id_dossier;
            schemaPivot = data.schema_pivot;

            // Remplissage des KPIs globaux
            // resScore, resLevel et resCommune supprimés de l'interface

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

                <!-- Section Score Breakdown Clinique -->
                <div class="explain-section" style="border-top: 1px solid var(--border-glass); padding-top: 1rem;">
                    <span class="explain-subtitle">🔍 Détail des points par phrase/critère relevé</span>
                    <div class="score-breakdown-list" id="score-breakdown-list" style="display: flex; flex-direction: column; gap: 0.75rem;">
                        <!-- Rempli dynamiquement -->
                    </div>
                </div>

                <!-- Section Tableau des Scores Finaux de Toutes les Structures -->
                <div class="explain-section" style="border-top: 1px solid var(--border-glass); padding-top: 1rem;">
                    <span class="explain-subtitle">📊 Scores totaux de toutes les structures</span>
                    <div id="structures-score-comparison" style="display: flex; flex-direction: column; gap: 0.6rem;">
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
                handleOuiElleConvient(struct.label, struct.structure_type, struct);
            });
        }

        // Liaison de l'animation de toggle d'explications
        const btnWhy = card.querySelector('#btn-why');
        const explainPane = card.querySelector('#explanation-pane');
        btnWhy.addEventListener('click', () => {
            if (explainPane.style.display === 'none') {
                renderComidJustifications(card.querySelector('#comid-proof-list'));
                renderScoreBreakdown(card.querySelector('#score-breakdown-list'));
                renderScoreComparison(card.querySelector('#structures-score-comparison'));
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
     * Renseigne le détail du calcul des scores cliniques par phrase
     */
    function renderScoreBreakdown(container) {
        container.innerHTML = '';
        if (scoreBreakdown.length === 0) {
            container.innerHTML = `
                <div style="font-size: 0.85rem; color: var(--text-muted); font-style: italic;">
                    Aucune règle de score clinique n'a été appliquée pour ce cas.
                </div>
            `;
            return;
        }

        scoreBreakdown.forEach(item => {
            const card = document.createElement('div');
            card.className = 'score-breakdown-card';
            
            let pointsHtml = '';
            for (const [stype, pts] of Object.entries(item.points)) {
                const color = STRUCTURE_COLORS[stype] || '#64748b';
                pointsHtml += `
                    <span class="score-badge" style="background-color: ${color}15; color: ${color}; border: 1px solid ${color}35;">
                        ${stype} : +${pts} pts
                    </span>
                `;
            }

            card.innerHTML = `
                <div class="score-breakdown-header">
                    <span style="font-weight: 700; color: var(--text-primary); font-size: 0.88rem;">📌 ${item.description}</span>
                </div>
                <div class="score-breakdown-quote">« ${item.justification} »</div>
                <div class="score-breakdown-points">${pointsHtml}</div>
            `;
            container.appendChild(card);
        });
    }

    /**
     * Affiche le tableau comparatif des scores totaux de toutes les structures
     */
    function renderScoreComparison(container) {
        container.innerHTML = '';
        
        let maxScore = 0;
        orientations.forEach(o => {
            if (o.priorite > maxScore) {
                maxScore = o.priorite;
            }
        });

        orientations.forEach(struct => {
            const row = document.createElement('div');
            row.className = 'score-row-bar-container';
            const color = STRUCTURE_COLORS[struct.structure_type] || '#64748b';
            
            const maxRange = Math.max(maxScore, 100);
            const percentage = Math.min(Math.max((struct.priorite / maxRange) * 100, 0), 100);
            
            const isWinner = struct.priorite === maxScore && maxScore > 0;
            const winnerBadge = isWinner ? '<span class="winner-badge">Recommandé (Top 1)</span>' : '';

            row.innerHTML = `
                <div class="score-row-label">
                    <span style="font-weight: 600; color: var(--text-primary);">${struct.structure_type}</span>
                    ${winnerBadge}
                </div>
                <div class="score-row-progress-wrapper">
                    <div class="score-row-progress-bar" style="width: ${percentage}%; background-color: ${color};"></div>
                </div>
                <div class="score-row-value">${struct.priorite} pts</div>
            `;
            container.appendChild(row);
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
    window.handleOuiElleConvient = function(label, type, structData = null) {
        const commune = (schemaPivot && schemaPivot["usager.localisation.commune_residence"]) ? schemaPivot["usager.localisation.commune_residence"].toLowerCase() : "";

        if (type === 'DAC') {
            window.showDacWizard(label, type);
        } else if (type === 'CLIC' && (label.toLowerCase().includes('seyne') || commune.includes('seyne'))) {
            window.showClicWizard(label, type);
        } else if (type === 'CLIC' && (label.toLowerCase().includes('toulon') || commune.includes('toulon'))) {
            window.showClicToulonWizard(label, type);
        } else if (structData && structData.email) {
            window.showGenericMailWizard(structData);
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
                .mini-kpi-card {
    background: var(--bg-card);
    border: 1px solid var(--border-glass);
    border-radius: var(--radius-sm);
    padding: 1rem;
    display: flex;
    flex-direction: column;
    align-items: center !important;
    justify-content: center !important;
    text-align: center !important;
    gap: 4px;
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
     * Gère la génération de mail pour toutes les structures ayant un email (CCAS, CPTS, CLIC sans PDF...)
     */
    window.showGenericMailWizard = function(structData) {
        let modal = document.getElementById('dac-wizard-modal');
        if (!modal) {
            modal = document.createElement('div');
            modal.id = 'dac-wizard-modal';
            modal.className = 'modal-overlay';
            document.body.appendChild(modal);
        }
        ensureWizardStyles();
        
        const destinationEmail = structData.email || "";
        const nomStructure = structData.nom_local || structData.label;

        const nom = (schemaPivot && schemaPivot["usager.identite.nom_naissance"]) || "[Nom de l'usager]";
        const prenom = (schemaPivot && schemaPivot["usager.identite.prenoms"]) || "";
        const nomComplet = `${prenom} ${nom}`.trim();
        const situationText = document.getElementById('situation-input').value.trim() || "[Résumé de la situation]";

        const mailSubject = `Demande d'orientation - ${nomComplet}`;
        const resumeText = (schemaPivot && schemaPivot["demande.resume_structuré"]) ? schemaPivot["demande.resume_structuré"] : situationText;

        const introGreeting = `Bonjour,

Je vous contacte concernant la situation de ${nomComplet}.
`;

        let mailBody = "";
        if (schemaPivot && schemaPivot["demande.proposition_mail"]) {
            let aiText = schemaPivot["demande.proposition_mail"].trim();
            // Remove any leading greeting (Bonjour, Bonsoir, Bonjour ORIA, etc.)
            aiText = aiText.replace(/^(?:bonjour|bonsoir)[^.,\n]*[.,\n]?\s*/i, '');
            if (aiText.length > 0) {
                aiText = aiText.charAt(0).toUpperCase() + aiText.slice(1);
            }

            mailBody = `${introGreeting}
${aiText}

Je reste à votre disposition pour tout complément d'information.

Cordialement,`;
        } else {
            mailBody = `${introGreeting}
Adresse : ${(schemaPivot && schemaPivot["usager.localisation.adresse_complete"]) || "[Adresse]"}
Téléphone : ${(schemaPivot && schemaPivot["usager.contact.numero_telephone_1"]) || "[Téléphone]"}

Voici un résumé de la situation :
${resumeText}

Je reste à votre disposition pour tout complément d'information.

Cordialement,`;
        }

        modal.style.display = 'flex';
        modal.innerHTML = `
            <div class="modal-card" style="max-width: 600px;">
                <div class="modal-header">
                    <h3>Générer un mail d'orientation</h3>
                </div>
                <div class="modal-body">
                    <p style="margin-bottom: 0.75rem; font-weight: 600; color: #f59e0b;">Orientation détectée : ${nomStructure}</p>
                    <p>Il n'y a pas de fiche d'orientation PDF pour cette structure. Voici un mail pré-rempli avec les informations extraites :</p>
                    
                    <div style="margin-top: 1rem; text-align: left;">
                        <label style="font-weight: 600; font-size: 0.85rem;">À :</label>
                        <input type="text" id="mail-to" value="${destinationEmail}" style="width: 100%; padding: 0.5rem; border: 1px solid #e2e8f0; border-radius: 4px; margin-bottom: 0.5rem;" />
                        
                        <label style="font-weight: 600; font-size: 0.85rem;">Objet :</label>
                        <input type="text" id="mail-subject" value="${mailSubject}" style="width: 100%; padding: 0.5rem; border: 1px solid #e2e8f0; border-radius: 4px; margin-bottom: 0.5rem;" />
                        
                        <label style="font-weight: 600; font-size: 0.85rem;">Message :</label>
                        <textarea id="mail-body" rows="8" style="width: 100%; padding: 0.5rem; border: 1px solid #e2e8f0; border-radius: 4px; font-family: inherit; resize: vertical;">${mailBody}</textarea>
                    </div>
                </div>
                <div class="modal-footer" style="justify-content: space-between;">
                    <button id="btn-mail-ignorer" class="btn-modal-secondary">Ignorer et valider</button>
                    <div style="display: flex; gap: 0.5rem;">
                        <button id="btn-mail-copier" class="btn-modal-secondary" style="background: #f1f5f9; color: #0f172a;">Copier le texte</button>
                        <button id="btn-mail-ouvrir" class="btn-modal-primary" style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);">Ouvrir dans la messagerie</button>
                    </div>
                </div>
            </div>
        `;

        document.getElementById('btn-mail-ignorer').onclick = () => {
            modal.style.display = 'none';
            window.validateCurrentOrientation(structData.label, structData.structure_type);
        };

        document.getElementById('btn-mail-copier').onclick = () => {
            const bodyText = document.getElementById('mail-body').value;
            navigator.clipboard.writeText(bodyText).then(() => {
                const btn = document.getElementById('btn-mail-copier');
                const originalText = btn.innerText;
                btn.innerText = "✓ Copié !";
                setTimeout(() => btn.innerText = originalText, 2000);
            });
        };

        document.getElementById('btn-mail-ouvrir').onclick = () => {
            const to = document.getElementById('mail-to').value;
            const subject = encodeURIComponent(document.getElementById('mail-subject').value);
            const body = encodeURIComponent(document.getElementById('mail-body').value);
            window.location.href = `mailto:${to}?subject=${subject}&body=${body}`;
            
            setTimeout(() => {
                modal.style.display = 'none';
                window.validateCurrentOrientation(structData.label, structData.structure_type);
            }, 1000);
        };
    };

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
