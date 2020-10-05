// Visual change when clicking upvote button
const favToggle = (event) => {
  let eventClass = event.target.classList;
  let aId = event.target.parentElement.dataset.answerId;
  let $numUsers = $(`span[data-answer-id=${aId}]`)[0];

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

// Axios request for clicking upvote button
const upvoteToggle = async (event) => {
  let eventClass = event.target.classList;
  let qId = event.target.parentElement.dataset.questionId;
  let aId = event.target.parentElement.dataset.answerId;

  if (eventClass.contains("fav")) {
    const response = await axios.post(`/q/${aId}/unlike`);
    if (response) {
      favToggle(event);
    }
  } else {
    const response = await axios.post(`/q/${aId}/like`);
    if (response) {
      favToggle(event);
    }
  }
};

$(".upvote").on("click", upvoteToggle);
