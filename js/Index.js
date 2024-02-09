document.getElementById('submit-btn').addEventListener('click', function () {
    sendMessage();
});

document.getElementById('message-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        e.preventDefault(); 
        sendMessage();
    }
});

function sendMessage() {
    var messageInput = document.getElementById('message-input');
    var message = messageInput.value.trim();
    if (message !== '') {
        addMessageToChat(message);
        messageInput.value = '';
    }
}

function addMessageToChat(message) {
    var chatContainer = document.getElementById('chat-container');
    var messageElement = document.createElement('div');
    messageElement.textContent = message;
    messageElement.classList.add(chatContainer.children.length % 2 === 0 ? 'left-message' : 'right-message');
    chatContainer.appendChild(messageElement);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}
