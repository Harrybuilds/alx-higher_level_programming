$(document).ready(function() {
  const url = "https://swapi-api.alx-tools.com/api/films/?format=json";

  $.getJSON(url, function(data) {
    const moviesList = $("#list_movies");

    // Loop through each movie in the results
    data.results.forEach(function(movie) {
      const listItem = $("<li></li>").text(movie.title);
      moviesList.append(listItem);
    });
  });
});
