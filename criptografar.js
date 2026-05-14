let senha = Number(prompt("Digite a senha: "));

function criptografar(valor) {
    valor += 10;
    alert("Senha criptografada: " + valor);
}

criptografar(senha);