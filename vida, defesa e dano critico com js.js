const danoBase = 150;
const houveCritico = Math.random() < 0.3; 
const bonusCritico = 50;

const defesas = ["Fortificada", "Santa", "Nenhuma", "Reflexiva"];
const tipoDefesaInimigo = defesas[Math.floor(Math.random() * defesas.length)];

let danoTotal = danoBase + (houveCritico ? bonusCritico : 0);

const multiplicadores = {
    "Fortificada": 0.85,
    "Santa": 0.0,
    "Reflexiva": 0.45,
    "Nenhuma": 1.0
};

let danoFinal = danoTotal * multiplicadores[tipoDefesaInimigo];

const statusCritico = houveCritico ? "SIM! 💥" : "Não.";
const linha = "=".repeat(30);

let resumo = `
${linha}
⚔️ RELATÓRIO DE COMBATE
${linha}
Ataque Crítico? ${statusCritico}
Inimigo usou: ${tipoDefesaInimigo}
Dano causado: ${danoFinal.toFixed(2)}
`;

if (tipoDefesaInimigo === "Santa") {
    resumo += "🚫 O dano foi totalmente bloqueado!";
} else if (tipoDefesaInimigo === "Reflexiva") {
    resumo += `⚠️ Você recebeu ${danoFinal.toFixed(2)} de dano de volta!`;
} else if (tipoDefesaInimigo === "Fortificada") {
    resumo += "🛡️ Dano reduzido em 15%.";
}

alert(resumo);
