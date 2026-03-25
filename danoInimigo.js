let vidaInimigo = 100;

function danoInimigo() {
  let dano = Number(prompt("digite o valor do dano: "));
  let danoExtra = prompt("deseja dano extra? s/n").toLocaleLowerCase();
  let danoextraValor = 20;
  if (dano > 0) {
    if (danoExtra == "s") {
      dano += danoextraValor;
      vidaInimigo -= dano;
      alert("o dano dado no inimigo com extra foi: " + dano);
      alert("o inimigo ficou com a vida: " + vidaInimigo);
    } else if (danoExtra == "n") {
      dano = dano;
      vidaInimigo -= dano;
      alert("o dano padrao foi: " + dano);
      alert("o inimigo ficou com a vida: " + vidaInimigo);
    } else {
      alert("o dano precisa ser maior que 0");
    }
  }
}

let posicaoPlayer = prompt("digite a posição do player: ");
let posicaoInimigo = 1;
if (posicaoPlayer == posicaoInimigo) {
  danoInimigo();
} else {
  alert("o player errou o ataque");
}

danoInimigo();
