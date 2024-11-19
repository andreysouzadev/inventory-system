// Função para remover mensagens após 5 segundos
setTimeout(() => {
    const messages = document.querySelectorAll('.message'); // Seleciona todas as mensagens
    messages.forEach((message) => {
        // Adiciona uma transição suave
        message.style.transition = "opacity 1s ease";
        message.style.opacity = "0"; // Define a opacidade como 0 para desaparecer

        // Remove o elemento do DOM após a transição
        setTimeout(() => {
            message.remove();
        }, 1000); // Aguarda 1 segundo para a transição concluir
    });
}, 5000); // Aguarda 5 segundos antes de começar a desaparecer

