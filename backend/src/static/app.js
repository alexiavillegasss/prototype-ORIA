/* ===================================================
   ORIA Dashboard – app.js
   Fetches Sankey data from the API and renders the chart.
   Supports dynamic dimension selection via dropdowns.
   =================================================== */

// -- Color palette for Sankey nodes --
const NODE_COLORS = {
    // Communes (bleu-teal)
    'commune': [
        '#38bdf8', '#22d3ee', '#2dd4bf', '#34d399',
        '#67e8f9', '#5eead4', '#6ee7b7', '#a5f3fc'
    ],
    // Niveaux COMID
    'Situation simple': '#4ade80',
    'Situation non complexe': '#4ade80',
    'Situation modérément complexe': '#fbbf24',
    'Situation à risque de complexité': '#fb923c',
    'Situation très complexe': '#f87171',
    'Situation extrêmement complexe': '#ef4444',
    // Structures
    'CRT': '#a78bfa',
    'CEV': '#f87171',
    'PSCG_SS_APA': '#c084fc',
    'CLIC': '#38bdf8',
    'UTS': '#2dd4bf',
    'CCAS': '#34d399',
    'DAC': '#fb923c',
    'CPTS': '#fbbf24',
    'SERVICE_SOCIAL_HOPITAL': '#fb7185',
    // APA
    'APA : Oui': '#4ade80',
    'APA : Non': '#f87171',
    'APA : Non renseigné': '#64748b',
    // Urgence
    'Urgence : Oui': '#ef4444',
    'Urgence : Non': '#4ade80',
    'Urgence : Non renseigné': '#64748b',
    // Médecin traitant
    'Médecin traitant : Oui': '#4ade80',
    'Médecin traitant : Non': '#f87171',
    'Médecin traitant : Non renseigné': '#64748b',
    // Tranches d'âge
    '60-64 ans': '#38bdf8',
    '65-69 ans': '#22d3ee',
    '70-74 ans': '#2dd4bf',
    '75-79 ans': '#fbbf24',
    '80-84 ans': '#fb923c',
    '85 ans et plus': '#f87171',
    'Âge inconnu': '#64748b',
    // GIR
    'GIR 1': '#ef4444',
    'GIR 2': '#f87171',
    'GIR 3': '#fb923c',
    'GIR 4': '#fbbf24',
    'GIR 5': '#4ade80',
    'GIR 6': '#34d399',
    'GIR non renseigné': '#64748b'
};

// -- ECharts instance (global for resize) --
let chartInstance = null;

/**
 * Get current dimension selections
 */
function getSelectedDimensions() {
    return {
        dim1: document.getElementById('select-dim1').value,
        dim2: document.getElementById('select-dim2').value,
        dim3: document.getElementById('select-dim3').value
    };
}

/**
 * Fetch sankey data from the API with selected dimensions
 */
async function loadDashboard() {
    const dims = getSelectedDimensions();
    
    // Check for duplicate dimensions
    const activeDims = [dims.dim1, dims.dim2, dims.dim3].filter(d => d !== 'none');
    const uniqueDims = new Set(activeDims);
    
    if (activeDims.length !== uniqueDims.size) {
        document.getElementById('sankey-chart').style.display = 'none';
        document.getElementById('sankey-empty').style.display = 'block';
        document.getElementById('sankey-empty-msg').innerHTML = '<span style="color: var(--text-primary); font-weight: 500;">Veuillez ne pas sélectionner deux dimensions identiques.</span>';
        return; // Abort
    }

    const url = `/api/dashboard/sankey?dim1=${dims.dim1}&dim2=${dims.dim2}&dim3=${dims.dim3}`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        // Update KPIs
        updateKPIs(data.kpis);

        // Render Sankey
        if (data.sankey.nodes.length === 0) {
            document.getElementById('sankey-chart').style.display = 'none';
            document.getElementById('sankey-empty').style.display = 'block';
            document.getElementById('sankey-empty-msg').textContent = 'Aucun dossier enregistré pour le moment.';
        } else {
            document.getElementById('sankey-chart').style.display = 'block';
            document.getElementById('sankey-empty').style.display = 'none';
            renderSankey(data.sankey);
        }
    } catch (err) {
        console.error('Erreur lors du chargement du dashboard:', err);
        document.getElementById('sankey-chart').style.display = 'none';
        document.getElementById('sankey-empty').style.display = 'block';
        document.getElementById('sankey-empty-msg').textContent = 'Une erreur est survenue lors du chargement des données.';
    }
}

/**
 * Update KPI cards with values
 */
function updateKPIs(kpis) {
    document.getElementById('total-dossiers').textContent = kpis.total_dossiers;
    document.getElementById('kpi-score-value').textContent = kpis.score_moyen !== null
        ? kpis.score_moyen.toFixed(1)
        : '–';
    document.getElementById('kpi-commune-value').textContent = kpis.commune_top || '–';
    document.getElementById('kpi-structure-value').textContent = kpis.structure_top || '–';
    document.getElementById('kpi-complexity-value').textContent = kpis.niveau_top || '–';
}

/**
 * Assign colors to nodes based on their name
 */
function getNodeColor(name, index) {
    // Direct match
    if (NODE_COLORS[name]) return NODE_COLORS[name];

    // Partial match (for COMID levels with encoding issues)
    for (const key of Object.keys(NODE_COLORS)) {
        if (typeof key === 'string' && name.includes(key)) return NODE_COLORS[key];
    }

    // Default: use commune palette (rotating colors)
    const communeColors = NODE_COLORS['commune'];
    return communeColors[index % communeColors.length];
}

/**
 * Get dimension label for display
 */
function getDimensionLabel(dimValue) {
    const labels = {
        'commune': 'Commune',
        'tranche_age': "Tranche d'âge",
        'complexite': 'Complexité COMID',
        'structure': 'Type de structure',
        'apa': 'Bénéficiaire APA',
        'gir': 'GIR',
        'medecin_traitant': 'Médecin traitant',
        'urgence': 'Urgence'
    };
    return labels[dimValue] || dimValue;
}

/**
 * Render Sankey chart with ECharts
 */
function renderSankey(sankeyData) {
    const chartDom = document.getElementById('sankey-chart');

    // Dispose previous instance if exists
    if (chartInstance) {
        chartInstance.dispose();
    }
    chartInstance = echarts.init(chartDom, null, { renderer: 'canvas' });

    // Assign colors to nodes
    const coloredNodes = sankeyData.nodes.map((node, i) => ({
        ...node,
        itemStyle: {
            color: getNodeColor(node.name, i),
            borderColor: 'rgba(255,255,255,0.15)',
            borderWidth: 1
        }
    }));

    const dims = getSelectedDimensions();

    const option = {
        backgroundColor: 'transparent',
        toolbox: {
            feature: {
                saveAsImage: {
                    title: 'Télécharger l\'image',
                    name: 'diagramme_sankey_oria',
                    pixelRatio: 2,
                    backgroundColor: '#ffffff'
                }
            },
            iconStyle: {
                borderColor: '#475569'
            },
            right: 20,
            top: 0
        },
        tooltip: {
            trigger: 'item',
            triggerOn: 'mousemove',
            backgroundColor: 'rgba(255, 255, 255, 0.95)',
            borderColor: 'rgba(0, 0, 0, 0.1)',
            borderWidth: 1,
            textStyle: {
                color: '#0f172a',
                fontFamily: 'Inter',
                fontSize: 13
            },
            formatter: function (params) {
                if (params.dataType === 'edge') {
                    return `<strong>${params.data.source}</strong> → <strong>${params.data.target}</strong><br/>Dossiers : <strong>${params.data.value}</strong>`;
                }
                return `<strong>${params.name}</strong>`;
            }
        },
        series: [{
            type: 'sankey',
            layout: 'none',
            emphasis: {
                focus: 'adjacency',
                lineStyle: {
                    opacity: 0.6
                }
            },
            nodeAlign: 'left',
            nodeWidth: 22,
            nodeGap: 14,
            layoutIterations: 32,
            draggable: true,
            data: coloredNodes,
            links: sankeyData.links,
            lineStyle: {
                color: 'gradient',
                curveness: 0.5,
                opacity: 0.35
            },
            label: {
                color: '#0f172a',
                fontFamily: 'Inter',
                fontSize: 12,
                fontWeight: 500
            },
            itemStyle: {
                borderWidth: 1,
                borderColor: 'rgba(0, 0, 0, 0.1)'
            },
            animationType: 'scale',
            animationDuration: 800,
            animationEasing: 'cubicOut'
        }]
    };

    chartInstance.setOption(option);
}

// -- Event listeners for dimension selectors --
function initSelectors() {
    const selectors = ['select-dim1', 'select-dim2', 'select-dim3'];
    selectors.forEach(id => {
        document.getElementById(id).addEventListener('change', () => {
            loadDashboard();
        });
    });
}

// -- Responsive resize --
window.addEventListener('resize', () => {
    if (chartInstance) chartInstance.resize();
});

// -- Launch --
document.addEventListener('DOMContentLoaded', () => {
    initSelectors();
    loadDashboard();
});
