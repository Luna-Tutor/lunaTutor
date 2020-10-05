$(() => {
  $("#hashtag").autocomplete({
    source: (request, response) => {
        $.getJSON("/search/tags",{
            q: request.term,
        }, function(data) {
            response(data.matching_results);
        });
    },
    minLength: 1,
  });
})