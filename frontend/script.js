let socket = new WebSocket("ws://localhost:8765");

socket.onmessage = function(event) {
    let dados = JSON.parse(event.data);

    if (dados.tipo === "login_resposta") {
        if (dados.sucesso) {
            alert("Login bem-sucedido! Redirecionando...");
            window.location.href = "biblioteca.html";
        } else {
            alert("Login falhou! Verifique suas credenciais.");
        }
    } else if (dados.tipo === "registro_resposta") {
        if (dados.sucesso) {
            alert("Conta criada com sucesso! Redirecionando para o login...");
            setTimeout(() => {
                window.location.href = "index.html";  // Agora o redirecionamento acontece automaticamente!
            }, 1000);
        } else {
            alert("Erro: Usuário ou email já existente.");
        }
    }
};

function login() {
    let usuario = document.getElementById("usuario").value;
    let senha = document.getElementById("senha").value;

    let dados = { tipo: "login", usuario: usuario, senha: senha };
    socket.send(JSON.stringify(dados));
}

function registrar() {
    let nome = document.getElementById("nome").value;
    let email = document.getElementById("email").value;
    let usuario = document.getElementById("usuario").value;
    let senha = document.getElementById("senha").value;

    let dados = { tipo: "registro", nome: nome, email: email, usuario: usuario, senha: senha };
    socket.send(JSON.stringify(dados));
}
