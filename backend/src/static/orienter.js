// On récupère les couleurs définies dans le tableau de bord pour garder une cohérence visuelle
const STRUCTURE_COLORS = {
    'CRT': '#a78bfa',
    'CEV': '#f87171',
    'PSCG_SS_APA': '#c084fc',
    'CLIC': '#38bdf8',
    'UTS': '#2dd4bf',
    'CCAS': '#34d399',
    'DAC': '#fb923c',
    'CPTS': '#fbbf24',
    'SERVICE_SOCIAL_HOPITAL': '#fb7185'
};

document.addEventListener('DOMContentLoaded', () => {
    const btnSubmit = document.getElementById('btn-submit');
    const inputArea = document.getElementById('situation-input');
    const spinner = document.getElementById('btn-spinner');
    
    const placeholder = document.getElementById('results-placeholder');
    const resultsContent = document.getElementById('results-content');
    
    // Champs de résultat
    const resScore = document.getElementById('res-score');
    const resLevel = document.getElementById('res-level');
    const resCommune = document.getElementById('res-commune');
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
        btnSubmit.querySelector('.btn-text').textContent = 'Analyse IA en cours...';

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

            // 3. Remplissage des résultats
            placeholder.style.display = 'none';
            resultsContent.style.display = 'block';

            // KPIs principaux
            resScore.textContent = `${data.evaluation_complexe.score_total} / 20`;
            resLevel.textContent = data.evaluation_complexe.label;
            resCommune.textContent = data.schema_pivot["usager.localisation.commune_residence"] || "Non spécifiée";

            // Coloration du label de complexité en fonction de sa gravité
            resLevel.className = 'kpi-value ' + getComplexityClass(data.evaluation_complexe.score_total);

            // Construction de la liste des structures
            structuresList.innerHTML = '';
            
            if (data.orientation_suggeree.length === 0) {
                structuresList.innerHTML = `
                    <div class="empty-state" style="padding: 2rem;">
                        <p>Aucune structure éligible trouvée pour cette situation.</p>
                    </div>
                `;
            } else {
                data.orientation_suggeree.forEach(struct => {
                    const structCard = createStructureCard(struct);
                    structuresList.appendChild(structCard);
                });
            }

            // Données brutes sous l'accordéon pour le débug
            jsonOutput.textContent = JSON.stringify(data.schema_pivot, null, 2);

        } catch (error) {
            console.error(error);
            alert("Une erreur est survenue lors de l'analyse du cas. Vérifiez que votre serveur local et Ollama sont bien actifs.");
        } finally {
            // 4. Sortie de l'état de chargement
            btnSubmit.disabled = false;
            spinner.style.display = 'none';
            btnSubmit.querySelector('.btn-text').textContent = 'Lancer l\'Analyse';
        }
    });
});

/**
 * Attribue une classe CSS en fonction du score COMID pour colorer le texte
 */
function getComplexityClass(score) {
    if (score <= 5) return 'text-simple';
    if (score <= 10) return 'text-warning';
    return 'text-danger';
}

/**
 * Crée un élément HTML de carte de structure préconisée
 */
function createStructureCard(struct) {
    const card = document.createElement('div');
    card.className = 'struct-card fadeInUp';
    
    // Détermination de la couleur associée au type de structure
    const color = STRUCTURE_COLORS[struct.structure_type] || '#64748b';

    card.innerHTML = `
        <div class="struct-card-header">
            <span class="struct-badge" style="background-color: ${color}20; color: ${color}; border: 1px solid ${color}40;">
                ${struct.structure_type}
            </span>
            <span class="priority-badge">Priorité ${struct.priorite}</span>
        </div>
        <h4 class="struct-name">${struct.label}</h4>
        <p class="struct-objective"><strong>Mission :</strong> ${struct.objectif || 'Non renseigné'}</p>
        
        <!-- Bloc contact territorialisé -->
        <div class="struct-contact">
            <div class="contact-item">
                <span class="icon">📞</span>
                <span>${struct.telephone || 'Aucun numéro disponible'}</span>
            </div>
            <div class="contact-item">
                <span class="icon">📍</span>
                <span>${struct.adresse || 'Aucune adresse renseignée pour ce secteur'}</span>
            </div>
        </div>
    `;
    return card;
}
