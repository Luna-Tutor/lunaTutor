const favToggle = (event) => {
  let eventClass = event.target.classList;
  let qId = event.target.parentElement.dataset.questionId;
  let $numUsers = $(`span[data-question-id=${qId}]`)[0];

  if (eventClass.contains("fav")) {
    $numUsers.innerText = parseInt($numUsers.innerText) - 1;
  } else {
    if ($numUsers.innerText === "") {
      $numUsers.innerText = "1";
    } else {
      $numUsers.innerText = parseInt($numUsers.innerText) + 1;
    }
  }

  eventClass.toggle("fav");
  eventClass.toggle("far");
  eventClass.toggle("fas");
};

$(".upvote").on("click", favToggle);
