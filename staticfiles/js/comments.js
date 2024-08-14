document.addEventListener('DOMContentLoaded', function () {
    // Handle delete confirmation modal
    const deleteButtons = document.querySelectorAll('.btn-delete');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function () {
            const commentId = this.getAttribute('data-comment_id');
            const exercisePk = this.getAttribute('data-exercise_pk');

            const deleteConfirmLink = document.getElementById('deleteConfirm');
            deleteConfirmLink.href = `/delete-comment/${exercisePk}/${commentId}/`;  // Adjust this URL as needed

            const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
            deleteModal.show();
        });
    });

    // Display message modal if messages are present
    const messageModal = document.getElementById('messageModal');
    const messages = JSON.parse(messageModal.getAttribute('data-messages'));
    if (messages.length > 0) {
        const modalBody = messageModal.querySelector('.modal-body');
        modalBody.innerHTML = messages.join('<br>');
        const modalInstance = new bootstrap.Modal(messageModal);
        modalInstance.show();
    }
});
