document.addEventListener('DOMContentLoaded', function() {
    var deleteButtons = document.querySelectorAll('.btn-delete');
    var deleteConfirmButton = document.getElementById('deleteConfirm');

    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var commentId = button.getAttribute('data-comment_id');
            var exercisePk = button.getAttribute('data-exercise_pk');
            var url = "{% url 'delete_comment' 'EXERCISE_PK' 'COMMENT_ID' %}".replace('EXERCISE_PK', exercisePk).replace('COMMENT_ID', commentId);

            deleteConfirmButton.setAttribute('href', url);
        });
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

