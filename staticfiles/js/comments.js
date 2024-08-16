document.addEventListener('DOMContentLoaded', function () {
    // Handle delete confirmation modal
    document.addEventListener('DOMContentLoaded', function () {
        const deleteButtons = document.querySelectorAll('.btn-delete');
    
        deleteButtons.forEach(button => {
            button.addEventListener('click', function () {
                const commentId = this.getAttribute('data-comment_id');
                const exercisePk = this.getAttribute('data-exercise_pk');
    
                // Set the URL for the delete confirmation
                const deleteConfirmLink = document.getElementById('deleteConfirm');
                deleteConfirmLink.href = `exercises/delete_comment/${exercisePk}/${commentId}/`;  // Adjust this URL as needed
    
                // Initialize and show the modal
                const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
                deleteModal.show();
            });
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
