document.addEventListener('DOMContentLoaded', function () {
    var editButtons = document.querySelectorAll('.edit_movie');
    editButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            // Find the closest ancestor which is the div with the class "movie-container"
            var movieContainer = button.closest('.movie-container');
            // Within that container, find the form with the class "update_movie_form"
            var updateForm = movieContainer.querySelector('.update_movie_form');

            if (updateForm.style.display === 'none' || updateForm.style.display === '') {
                updateForm.style.display = 'block';
            } else {
                updateForm.style.display = 'none';
            }
        });
    });
});
