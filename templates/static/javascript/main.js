// Função para remover mensagens após 5 segundos
setTimeout(() => {
    const messages = document.querySelectorAll('.message');
    messages.forEach((message) => {
        message.style.transition = "opacity 1s ease";
        message.style.opacity = "0"; // Define a opacidade como 0 para desaparecer

        setTimeout(() => {
            message.remove();
        }, 1000); // Aguarda 1 segundo para a transição concluir
    });
}, 5000);

