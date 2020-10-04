// Visual change when clicking upvote button
const favToggle = (event) => {
  let eventClass = event.target.classList;
  // let qId = event.target.parentElement.dataset.questionId;
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


// const upvoteToggle = async (event) => {
//   let qId = event.target.parentElement.dataset.questionId;
//   let aId = event.target.parentElement.dataset.answerId;
//   let subject = event.target.parentElement.dataset.subject;
//   await axios.post(`/q/${subject}/`);
// };

$(".upvote").on("click", favToggle);
