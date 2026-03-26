const ARMAS = {
  espada: 15,
  arco: 10,
  macumba: 10000,
  magia: 40,
  canhao: 60
};

let vidaInimigo = 100;
const listaArmas = Object.keys(ARMAS);
let mensagem = `Escolha um item (${listaArmas.join(', ')}):`;
let itemAtk = prompt(mensagem)?.toLowerCase();

function ataque() {
  if (ARMAS[itemAtk] !== undefined) {
    let dano = ARMAS[itemAtk];
    
    vidaInimigo -= dano;
    if (vidaInimigo < 0) vidaInimigo = 0;

    alert(`O inimigo perdeu ${dano} de vida! Vida restante: ${vidaInimigo}`);

    if (vidaInimigo === 0) {
      alert('O INIMIGO MORREEEEEEEEEEEU');
    } else {
      alert('Bom ataque, mas seu inimigo permanece vivo!');
    }
  } else {
    alert('Item inválido ou você errou o golpe!');
  }
}

ataque();