function movimentacao(tecla) {
  if (tecla === "w") {
    alert("Cima");
  } else if (tecla === "a") {
    alert("Esquerda");
  } else if (tecla === "s") {
    alert("Baixo");
  } else if (tecla === "d") {
    alert("Direita");
  } else if (tecla === "b") {
    alert("Ligar a lanterna");
  } else if (tecla === "1") {
    alert("Atacar com a espada");
  } else {
    alert("Tecla inválida");
  }
}
movimentacao(prompt("Digite uma tecla:").toUpperCase());
