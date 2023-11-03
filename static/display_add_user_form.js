document.addEventListener("DOMContentLoaded", function() {
    // Get a reference to the add_movie_form element
    var addMovieForm = document.querySelector(".add_user_form");

    // Hide the form by default
    addMovieForm.style.display = "none";

    // Get a reference to the "Add Movie" button
    var addMovieButton = document.querySelector("button");

    // Add a click event listener to the button
    addMovieButton.addEventListener("click", function() {
        // Toggle the visibility of the form when the button is clicked
        if (addMovieForm.style.display === "none") {
            addMovieForm.style.display = "block";
        } else {
            addMovieForm.style.display = "none";
        }
    });
});