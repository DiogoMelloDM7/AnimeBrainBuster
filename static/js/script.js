function finalizandoQuiz(event){
    event.preventDefault();
    let divQuiz = document.getElementById("form-quiz-create");
    let divQuizFinish = document.getElementById("form-quiz-finish");
    divQuiz.style.display="none";
    divQuizFinish.style.display="block";
}