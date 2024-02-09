document.getElementById('submit-btn').addEventListener('click', function () {
    var messageInput = document.getElementById('message-input');
    var message = messageInput.value;
    if (message.trim() !== '') {
        addMessageToChat(message);
        messageInput.value = '';
    }
});

function addMessageToChat(message) {
    var chatContainer = document.getElementById('chat-container');
    var messageElement = document.createElement('div');
    messageElement.textContent = message;
    chatContainer.appendChild(messageElement);
}
