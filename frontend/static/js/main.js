document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("loginForm");
    const registerForm = document.getElementById("registerForm");

    if (loginForm) {
        loginForm.addEventListener("submit", function (event) {
            event.preventDefault();
            const email = document.getElementById("email").value;
            const password = document.getElementById("password").value;

            fetch("/api/login", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ email, password }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = "/dashboard";
                } else {
                    alert("Erro ao fazer login!");
                }
            });
        });
    }

    if (registerForm) {
        registerForm.addEventListener("submit", function (event) {
            event.preventDefault();
            const nome = document.getElementById("nome").value;
            const email = document.getElementById("email").value;
            const username = document.getElementById("username").value;
            const password = document.getElementById("password").value;

            fetch("/api/register", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ nome, email, username, password }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert("Conta criada! Faça login.");
                    window.location.href = "/login";
                } else {
                    alert("Erro ao registrar!");
                }
            });
        });
    }
});
