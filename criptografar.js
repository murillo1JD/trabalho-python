let senha = Number(prompt("Digite a senha: "));

function criptografar(valor) {
    valor += 10;
    alert("Senha criptografada: " + valor);
    return valor;
}

function descriptografar(valor) {
    valor -= 10;
    alert("Senha descriptografada: " + valor);
}

let senhaCriptografada = criptografar(senha);
descriptografar(senhaCriptografada);
