function finalizandoQuiz(event){
    event.preventDefault();
    let divQuiz = document.getElementById("form-quiz-create");
    let divQuizFinish = document.getElementById("form-quiz-finish");
    divQuiz.style.display="none";
    divQuizFinish.style.display="block";
}

// Função para mostrar a mensagem de erro
function showErrorMessage() {
    var errorMessage = document.getElementById("error-message");
    errorMessage.style.display = "block";

    // Ocultar a mensagem após 3 segundos (ou o período desejado)
    setTimeout(function() {
        errorMessage.style.display = "none";
    }, 3000); // 3000 milissegundos = 3 segundos
}

// Chame a função para mostrar a mensagem de erro quando necessário
showErrorMessage();