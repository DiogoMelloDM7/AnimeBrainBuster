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


function excluirQuiz(quiz_id){
    if (confirm("Tem certeza que deseja excluir este quiz?")) {
        const csrftoken = getCookie('csrftoken');
        fetch(`/excluirquiz/${quiz_id}`, {
            method: "DELETE",
            headers: {
                "X-CSRFToken": csrftoken,
            },
        })
        .then((response) => {
            if (response.ok) {
                location.reload(); // Atualiza a página após excluir o item
            } else {
                alert("Ocorreu um erro ao excluir o quiz.");
            }
        })
        .catch((error) => {
            console.error("Erro na solicitação AJAX:", error);
        });
    }
}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Verifica se o cookie começa com o nome do token CSRF
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
