document.addEventListener('DOMContentLoaded', function () {
    const deleteButtons = document.querySelectorAll('.btn-delete');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function () {
            const commentId = this.getAttribute('data-comment_id');
            const exercisePk = this.getAttribute('data-exercise_pk');

            // Set the URL for the delete confirmation
            const deleteConfirmLink = document.getElementById('deleteConfirm');
            deleteConfirmLink.href = `/delete-comment/${exercisePk}/${commentId}/`;

            // Show the delete confirmation modal
            const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
            deleteModal.show();
        });
    });

    // Check for messages and display the message modal
    const messageModal = document.getElementById('messageModal');
    const messages = messageModal.getAttribute('data-messages');
    
    if (messages) {
        const parsedMessages = JSON.parse(messages);
        const messageBody = messageModal.querySelector('.modal-body');
        messageBody.innerHTML = parsedMessages.join('<br>');
        const modal = new bootstrap.Modal(messageModal);
        modal.show();
    }
});
