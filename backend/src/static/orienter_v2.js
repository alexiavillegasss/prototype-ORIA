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
    'POLICE': '#3b82f6',
    'PRADO': '#ec4899',
    'MISAS': '#10b981',
    "fil d'argent": '#f43f5e',
    'CONSULTATION MÉMOIRE': '#8b5cf6',
    'COMPAGNONS_BATISSEURS': '#64748b'
};

// Dictionnaire complet des 30 critères COMID pour la traçabilité clinique dans l'interface
const COMID_LABELS = {
    'multimorbidite': 'Plusieurs maladies chroniques (>2) et/ou symptôme(s) inexpliqué(s)',
    'douleurs': 'Douleurs chroniques',
    'allergies': 'Allergie et/ou intolérance médicamenteuse',
    'polymedication': 'Polymédication (>5)',
    'troubles_cognitifs': 'Troubles cognitifs',
    'precarite_financiere': 'Difficultés financières et/ou incapacité à supporter financièrement des prestations d\'aide et de soins',
    'epuisement_aidant': 'Absence ou épuisement du proche aidant et/ou tensions familiales',
    'litteratie_faible': 'Faible niveau de littératie (alphabétisation et/ou barrière linguistique/culturelle)',
    'isolement_social': 'Isolement social',
    'logement_inadapte': 'Logement inadapté et/ou barrière environnementale',
    'depression': 'Dépression et/ou idées suicidaires',
    'psychiatrie': 'Maladie psychiatrique et/ou troubles psychiques (délires, hallucination, etc.)',
    'addiction': 'Addiction',
    'anxiete': 'Anxiété ou angoisse rendant le tableau clinique confus',
    'fluctuation_mentale': 'Fonctions mentales variant au cours de la journée',
    'sollicitations_recurrentes': 'Sollicitations récurrentes du réseau primaire et/ou secondaire',
    'conflit_reseau': 'Communication ambivalente et/ou conflictuelle avec l\'un des membres du réseau primaire et/ou secondaire',
    'inquietude_sante': 'Inquiétude face à ses symptômes et/ou état de santé et/ou aux informations médicales reçues',
    'agressivite': 'Agressivité (verbale et/ou physique) ou mutisme',
    'opposition_soins': 'Résistance ou opposition aux soins, qu\'elles soient actives ou passives',
    'degradation_recente': 'Dégradation récente de l\'état de santé ressentie par le client',
    'perte_autonomie_recente': 'Changement global du degré d\'indépendance (AVQ/AIVQ) lors du dernier mois',
    'transition_parcours': 'Période de transition (annonce diagnostic, retour hospitalisation, décès proche aidant, divorce, travail, etc.)',
    'trouble_cognitif_aigu': 'Changement aigu des capacités cognitives',
    'imprevisibilite': 'Non prévisibilité de l\'état de santé',
    'multitude_intervenants': 'Multitude d\'intervenants dans le réseau secondaire (médecin traitant, spécialiste, soignant, curateur, etc.)',
    'manque_partenariat': 'Absence ou faible degré de partenariat entre les différents intervenants du réseau primaire et/ou secondaire',
    'incoherence_soins': 'Incohérence thérapeutique et/ou perte de sens dans la prise en charge du point de vue du professionnel',
    'probleme_assurance': 'Problème d\'assurance (limitation du remboursement de prise en charge)',
    'lourdeur_reseau': 'Lourdeur émotionnelle et/ou physique de la prise en charge ressentie par les membres du réseau secondaire (médecins, soignants)'
};

// Variables d'état globales de la session de diagnostic
let orientations = [];
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

    // Gestion du Menu Hamburger
    const menuToggle = document.getElementById('menu-toggle');
    const dropdownMenu = document.getElementById('dropdown-menu');
    
    if (menuToggle && dropdownMenu) {
        menuToggle.addEventListener('click', (e) => {
            e.stopPropagation(); // Empêche la fermeture immédiate
            dropdownMenu.classList.toggle('hidden');
        });

        // Fermer le menu si on clique ailleurs
        document.addEventListener('click', (e) => {
            if (!dropdownMenu.contains(e.target) && !menuToggle.contains(e.target)) {
                dropdownMenu.classList.add('hidden');
            }
        });
    }

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
        structuresTitle.style.display = "";
        structuresTitle.textContent = `Proposition d'orientation (${currentIndex + 1} sur ${orientations.length}) :`;

        const card = document.createElement('div');
        card.className = 'struct-card fadeInUp';
        const color = STRUCTURE_COLORS[struct.structure_type] || '#64748b';
        const formatConseilLink = (text) => {
            if (!text) return '';
            let formatted = text.replace(
                /\[([^\]]+)\]\((https?:\/\/[^\)]+)\)/g, 
                '<a href="$2" target="_blank" rel="noopener noreferrer" class="conseil-link-badge" style="display: inline-flex; align-items: center; gap: 0.3rem; background: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; border-radius: 6px; padding: 3px 9px; font-weight: 600; font-size: 0.84rem; text-decoration: none; margin: 2px 0; transition: all 0.2s ease;"><span style="font-size: 0.8rem;">🔗</span> $1</a>'
            );
            return formatted;
        };

        const conseilsHtml = (struct.conseils && struct.conseils.length > 0) ? `
            <div class="conseils-container" style="margin: 1.25rem 0; padding: 1.1rem; background: linear-gradient(135deg, rgba(239, 246, 255, 0.95) 0%, rgba(240, 249, 255, 0.85) 100%); border: 1px solid rgba(191, 219, 254, 0.9); border-left: 4px solid #2563eb; border-radius: 12px; box-shadow: 0 4px 12px rgba(37, 99, 235, 0.05);">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.85rem;">
                    <div style="display: inline-flex; align-items: center; gap: 0.4rem; background: #dbeafe; color: #1e40af; padding: 4px 10px; border-radius: 20px; font-size: 0.78rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.04em;">
                        <span>💡</span> Preconisations & Conseils
                    </div>
                    <span style="font-size: 0.76rem; color: #64748b; font-weight: 500;">Actions complémentaires</span>
                </div>
                <div style="display: flex; flex-direction: column; gap: 0.55rem;">
                    ${struct.conseils.map(c => `
                        <div class="conseil-item" style="background: #ffffff; border: 1px solid rgba(226, 232, 240, 0.95); border-radius: 8px; padding: 0.75rem 0.95rem; font-size: 0.88rem; line-height: 1.45; color: #1e293b; display: flex; align-items: flex-start; gap: 0.6rem; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
                            <span style="color: #2563eb; font-weight: 900; font-size: 1.1rem; line-height: 1.2; flex-shrink: 0;">•</span>
                            <div style="flex: 1;">${formatConseilLink(c)}</div>
                        </div>
                    `).join('')}
                </div>
            </div>
        ` : '';

        card.innerHTML = `
            <div class="struct-card-header">
                <span class="struct-badge" style="background-color: ${color}20; color: ${color}; border: 1px solid ${color}40;">
                    ${struct.structure_type}
                </span>
                <!--<span class="priority-badge">Indice de Priorité : <strong>${struct.priorite}</strong></span>-->
            </div>
            <h4 class="struct-name" style="margin-bottom: 0.75rem;">${struct.label}</h4>
            <p class="struct-objective" style="margin-bottom: 0.75rem;"><strong>Mission de la structure :</strong> ${struct.objectif || 'Non renseigné'}</p>
            
            ${conseilsHtml}

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
                            <span class="signal-title">Besoin principal</span>
                            <span>${formatBesoinPrincipal(schemaPivot["demande.besoin_principal"])}</span>
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

                <!-- Section Attribution des Points & Phrases -->
                <div class="explain-section" style="border-top: 1px solid var(--border-glass); padding-top: 1rem;">
                    <span class="explain-subtitle">Attribution des points (Besoins & Phrases identifiés)</span>
                    <div id="points-needs-list" style="display: flex; flex-direction: column; gap: 0.6rem; margin-top: 0.5rem;">
                        <!-- Rempli dynamiquement -->
                    </div>
                </div>

                <!-- Section Scores des structures -->
                <div class="explain-section" style="border-top: 1px solid var(--border-glass); padding-top: 1rem;">
                    <span class="explain-subtitle">Scores et exclusions des structures</span>
                    <div id="points-scores-grid" class="signals-grid" style="grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 0.5rem; margin-top: 0.5rem;">
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
                renderPointsExplanation(card);
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
     * Renseigne l'attribution des points et scores dans le conteneur HTML
     */
    function renderPointsExplanation(card) {
        const needsContainer = card.querySelector('#points-needs-list');
        const scoresContainer = card.querySelector('#points-scores-grid');
        
        if (!needsContainer || !scoresContainer) return;
        
        needsContainer.innerHTML = '';
        scoresContainer.innerHTML = '';
        
        const priorisations = schemaPivot["evaluation.moteur_points.priorisations_declenchees"] || [];
        const exclusions = schemaPivot["evaluation.moteur_points.exclusions_declenchees"] || [];
        const besoins = schemaPivot["evaluation.moteur_points.besoins_identifies"] || [];
        const scores = schemaPivot["evaluation.moteur_points.scores"] || {};
        
        // 1. Rendu des besoins
        if (priorisations.length > 0) {
            needsContainer.innerHTML = `
                <div style="font-size: 0.88rem; color: #f87171; font-weight: 600;">
                    ⚡ Garde-fou prioritaire déclenché pour : ${priorisations.join(', ')} (Calcul par points court-circuité)
                </div>
            `;
        } else if (besoins.length === 0) {
            needsContainer.innerHTML = `
                <div style="font-size: 0.85rem; color: var(--text-muted); font-style: italic;">
                    Aucun besoin identifié dans le récit pour le calcul des points.
                </div>
            `;
        } else {
            besoins.forEach(b => {
                const item = document.createElement('div');
                item.style.padding = '0.5rem';
                item.style.background = 'rgba(255, 255, 255, 0.02)';
                item.style.border = '1px solid var(--border-glass)';
                item.style.borderRadius = '6px';
                item.style.fontSize = '0.85rem';
                item.innerHTML = `
                    <div style="font-weight: 600; color: var(--text-primary);">${b.detaille}</div>
                    <div style="font-size: 0.78rem; color: var(--text-muted); margin-top: 2px;">
                        Catégorie : ${b.categorie} | <span style="color: var(--accent-blue);">+1 pt</span> pour : ${b.structures_cochees.join(', ')}
                    </div>
                `;
                needsContainer.appendChild(item);
            });
        }
        
        // 2. Rendu des scores des structures
        const sortedScores = Object.entries(scores).sort((a, b) => b[1] - a[1]);
        
        sortedScores.forEach(([struct, score]) => {
            const item = document.createElement('div');
            item.className = 'signal-item';
            item.style.display = 'flex';
            item.style.flexDirection = 'row';
            item.style.justifyContent = 'space-between';
            item.style.alignItems = 'center';
            item.style.padding = '0.5rem 0.75rem';
            
            const isExcluded = exclusions.includes(struct) || score === -9999;
            const color = STRUCTURE_COLORS[struct] || '#64748b';
            
            let scoreBadge = '';
            if (isExcluded) {
                scoreBadge = `<span style="color: #ef4444; font-weight: 700; font-size: 0.75rem; background: rgba(239, 68, 68, 0.1); padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(239, 68, 68, 0.3);">EXCLU</span>`;
                item.style.opacity = '0.5';
            } else {
                scoreBadge = `<span style="color: ${color}; font-weight: 700; font-size: 0.9rem;">${score} pts</span>`;
            }
            
            item.innerHTML = `
                <span class="signal-title" style="color: ${color}; font-size: 0.82rem;">${struct}</span>
                ${scoreBadge}
            `;
            scoresContainer.appendChild(item);
        });
    }

    /**
     * Valide l'orientation en cours auprès de l'API FastApi
     */
    /**
     * Valide l'orientation en cours auprès de l'API FastApi
     */
    window.validateCurrentOrientation = async function(label, type, options = {}) {
        label = label || "Orientation";
        type = type || "";

        if (dossierId) {
            try {
                await fetch(`/api/dossiers/${dossierId}/validate`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        status: `Validé - ${type}`,
                        structure_choisie: label
                    })
                });
            } catch (error) {
                console.error("Erreur enregistrement validation:", error);
            }
        }

        // Rendu de l'écran de validation finale
        if (structuresTitle) structuresTitle.style.display = "none";
        
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
        } else if (options && options.showClicProvenceVertePdf) {
            pdfButtonHtml = `
                <button onclick="downloadClicProvenceVertePdf()" class="btn-primary" style="background: #10b981; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3); margin-top: 1rem; margin-left: 0.5rem;">
                    📄 Visualiser la fiche d'orientation CLIC Provence Verte
                </button>
            `;
        } else if (options && options.showClicHadagePdf) {
            pdfButtonHtml = `
                <button onclick="downloadClicHadagePdf()" class="btn-primary" style="background: #f59e0b; box-shadow: 0 4px 12px rgba(245, 158, 11, 0.3); margin-top: 1rem; margin-left: 0.5rem;">
                    📄 Visualiser la fiche d'orientation CLIC Hadage
                </button>
            `;
        }
        let displayLabel = String(label);
        if (displayLabel.includes("DAC - Situation de complexité")) {
            displayLabel = "DAC (Dispositif d'appui à la coordination)";
        }
        if (displayLabel.includes("CLIC")) {
            displayLabel = displayLabel.replace(" (Sénior)", "").replace(" (Senior)", "");
        }

        if (structuresList) {
            structuresList.innerHTML = `
                <div class="success-card fadeInUp">
                    <h4 style="font-size: 1.2rem; font-weight: 700; color: #22c55e; margin-bottom: 0.5rem;">Dossier validé et enregistré</h4>
                    <p style="color: var(--text-primary); max-width: 480px; font-size: 1.05rem; line-height: 1.5; margin: 0 auto;">
                        Orientation : <strong>${displayLabel}</strong>
                    </p>
                    <div style="display: flex; justify-content: center; gap: 0.5rem; flex-wrap: wrap;">
                        <button onclick="resetAnalysis()" class="btn-primary" style="background: #22c55e; box-shadow: 0 4px 12px rgba(34, 197, 94, 0.3); margin-top: 1rem;">
                            Traiter un nouveau cas
                        </button>
                        ${pdfButtonHtml}
                    </div>
                </div>
            `;
        }
    };

    /**
     * Intercepte la validation pour le type DAC ou CLIC avec PDF, ou valide directement
     */
    window.handleOuiElleConvient = function(label, type, structData = null) {
        label = label || "Orientation";
        type = type || "";
        const commune = (schemaPivot && schemaPivot["usager.localisation.commune_residence"]) ? String(schemaPivot["usager.localisation.commune_residence"]).toLowerCase() : "";
        const nomLocal = structData && structData.nom_local ? String(structData.nom_local).toLowerCase() : "";
        const safeLabel = String(label).toLowerCase();

        if (type.startsWith('DAC')) {
            window.validateCurrentOrientation(label, type, { showDacPdf: true });
        } else if (type.startsWith('CLIC') && (safeLabel.includes('seyne') || nomLocal.includes('seyne') || commune.includes('seyne'))) {
            window.validateCurrentOrientation(label, type, { showClicPdf: true });
        } else if (type.startsWith('CLIC') && (safeLabel.includes('toulon') || nomLocal.includes('toulon') || commune.includes('toulon'))) {
            window.validateCurrentOrientation(label, type, { showClicToulonPdf: true });
        } else if (type.startsWith('CLIC') && (safeLabel.includes('provence verte') || nomLocal.includes('provence verte') || commune.includes('brignoles') || commune.includes('bras') || commune.includes('cotignac'))) {
            window.validateCurrentOrientation(label, type, { showClicProvenceVertePdf: true });
        } else if (type.startsWith('CLIC') && (safeLabel.includes('hadage') || nomLocal.includes('hadage') || commune.includes('hyères') || commune.includes('hyeres') || commune.includes('bormes'))) {
            window.validateCurrentOrientation(label, type, { showClicHadagePdf: true });
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
        window.validateCurrentOrientation(label, type, { showDacPdf: true });
    };

    /**
     * Gère le questionnaire pas-à-pas CLIC La Seyne
     */
    window.showClicWizard = function(label, type) {
        window.validateCurrentOrientation(label, type, { showClicPdf: true });
    };

    /**
     * Gère le questionnaire pas-à-pas CLIC Toulon
     */
    window.showClicToulonWizard = function(label, type) {
        window.validateCurrentOrientation(label, type, { showClicToulonPdf: true });
    };

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

    /**
     * Télécharge la fiche d'orientation CLIC Provence Verte sous format PDF
     */
    window.downloadClicProvenceVertePdf = async function() {
        const analyzeBtn = document.getElementById('analyze-btn');
        const text = document.getElementById('situation-input').value.trim();

        const btn = document.querySelector('[onclick="downloadClicProvenceVertePdf()"]');
        const originalText = btn.innerHTML;
        btn.innerHTML = '⏳ Génération en cours...';
        btn.disabled = true;

        try {
            const response = await fetch('/api/orientation/clic_provence_verte/generate_pdf', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: text })
            });

            if (!response.ok) {
                throw new Error("Erreur réseau");
            }

            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'fiche_orientation_clic_provence_verte.pdf';
            document.body.appendChild(a);
            a.click();
            a.remove();
            window.URL.revokeObjectURL(url);
        } catch (error) {
            console.error("Erreur PDF:", error);
            alert("Une erreur est survenue lors de la génération du PDF CLIC Provence Verte.");
        } finally {
            btn.innerHTML = originalText;
            btn.disabled = false;
        }
    };

    /**
     * Télécharge la fiche d'orientation CLIC Hadage sous format PDF
     */
    window.downloadClicHadagePdf = async function() {
        const analyzeBtn = document.getElementById('analyze-btn');
        const text = document.getElementById('situation-input').value.trim();

        const btn = document.querySelector('[onclick="downloadClicHadagePdf()"]');
        const originalText = btn.innerHTML;
        btn.innerHTML = '⏳ Génération en cours...';
        btn.disabled = true;

        try {
            const response = await fetch('/api/orientation/clic_hadage/generate_pdf', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: text })
            });

            if (!response.ok) {
                throw new Error("Erreur réseau");
            }

            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'fiche_orientation_clic_hadage.pdf';
            document.body.appendChild(a);
            a.click();
            a.remove();
            window.URL.revokeObjectURL(url);
        } catch (error) {
            console.error("Erreur PDF:", error);
            alert("Une erreur est survenue lors de la génération du PDF CLIC Hadage.");
        } finally {
            btn.innerHTML = originalText;
            btn.disabled = false;
        }
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

function formatBesoinPrincipal(besoin) {
    if (!besoin || besoin === 'indetermine') {
        return 'Aucun besoin principal trouvé';
    }
    return besoin;
}
// ========================================================
// DICTÉE VOCALE EN TEMPS RÉEL (NATIVE NAVIGATEUR)
// ========================================================
let activeRecognition = null;
let isDictating = false;

window.toggleVoiceDictation = function() {
    const btn = document.getElementById('btn-voice-toggle');
    const label = document.getElementById('voice-btn-label');
    const textarea = document.getElementById('situation-input');

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

    if (isDictating) {
        // STOP DICTÉE
        isDictating = false;
        if (activeRecognition) {
            try { 
                activeRecognition.abort(); 
                activeRecognition.stop(); 
            } catch(e){}
            activeRecognition = null;
        }
        if (btn) {
            btn.style.background = "rgba(239, 68, 68, 0.12)";
            btn.style.borderColor = "rgba(239, 68, 68, 0.35)";
            btn.style.color = "#f87171";
        }
        if (label) label.textContent = "Dictée vocale";
        return;
    }

    if (!SpeechRecognition) {
        alert("La reconnaissance vocale nécessite un navigateur compatible comme Google Chrome ou Microsoft Edge.");
        return;
    }

    try {
        activeRecognition = new SpeechRecognition();
        activeRecognition.lang = 'fr-FR';
        activeRecognition.continuous = true;
        activeRecognition.interimResults = true;

        let initialText = textarea ? textarea.value : '';

        activeRecognition.onstart = () => {
            isDictating = true;
            if (btn) {
                btn.style.background = "rgba(239, 68, 68, 0.3)";
                btn.style.borderColor = "#ef4444";
                btn.style.color = "#ffffff";
            }
            if (label) label.textContent = "🔴 Écoute en direct... (Clic pour stopper)";
        };

        activeRecognition.onresult = (event) => {
            let currentTranscript = '';
            for (let i = 0; i < event.results.length; i++) {
                currentTranscript += event.results[i][0].transcript;
            }
            if (textarea) {
                textarea.value = initialText ? (initialText.trim() + ' ' + currentTranscript) : currentTranscript;
            }
        };

        activeRecognition.onerror = (err) => {
            console.error('Erreur reconnaissance vocale:', err);
            if (err.error === 'no-speech' && isDictating) {
                // Silence détecté, on conserve l'écoute active
                return;
            }
            isDictating = false;
            activeRecognition = null;
            if (btn) {
                btn.style.background = "rgba(239, 68, 68, 0.12)";
                btn.style.borderColor = "rgba(239, 68, 68, 0.35)";
                btn.style.color = "#f87171";
            }
            if (label) label.textContent = "Dictée vocale";
        };

        activeRecognition.onend = () => {
            if (isDictating) {
                // Si l'utilisateur n'a pas cliqué sur Stop, relancer l'écoute immédiatement
                if (textarea) initialText = textarea.value;
                try {
                    activeRecognition.start();
                } catch(e) {
                    console.warn("Relance de l'écoute vocale:", e);
                }
            } else {
                activeRecognition = null;
                if (btn) {
                    btn.style.background = "rgba(239, 68, 68, 0.12)";
                    btn.style.borderColor = "rgba(239, 68, 68, 0.35)";
                    btn.style.color = "#f87171";
                }
                if (label) label.textContent = "Dictée vocale";
            }
        };

        activeRecognition.start();
    } catch (err) {
        console.error('Erreur accès micro:', err);
        alert("Impossible de démarrer le microphone. Veuillez vérifier les autorisations de votre navigateur.");
    }
};

document.addEventListener('DOMContentLoaded', () => {
    const voiceBtn = document.getElementById('btn-voice-toggle');
    if (voiceBtn) {
        voiceBtn.addEventListener('click', (e) => {
            e.preventDefault();
            window.toggleVoiceDictation();
        });
    }
});
