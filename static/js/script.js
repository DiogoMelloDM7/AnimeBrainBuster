function finalizandoQuiz(event){
    event.preventDefault();
    let divQuiz = document.getElementById("form-quiz-create");
    let divQuizFinish = document.getElementById("form-quiz-finish");
    divQuiz.style.display="none";
    divQuizFinish.style.display="block";
}

function showErrorMessage() {
    var errorMessage = document.getElementById("error-message");
    errorMessage.style.display = "block";

    setTimeout(function() {
        errorMessage.style.display = "none";
    }, 3000);
}
showErrorMessage();

function showNextQuestionQuiz(idQuiz){
    let divAtual = document.getElementById(`question-quiz-${idQuiz}`);
    let divAnterior = document.getElementById(`question-quiz-${idQuiz - 1}`);
    divAtual.style.display = "flex";
    divAnterior.style.display = 'none';
}

function showBackQuestionQuiz(idQuiz){
    if (idQuiz == 1){
        return
    }
    let divAtual = document.getElementById(`question-quiz-${idQuiz}`);
    let divAnterior = document.getElementById(`question-quiz-${idQuiz - 1}`);
    divAtual.style.display = "none";
    divAnterior.style.display = 'flex';
}