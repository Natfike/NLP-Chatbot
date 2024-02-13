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
    var messageContainer = document.createElement('div'); 
    var messageElement = document.createElement('div'); 
    messageElement.textContent = message;
    messageContainer.classList.add(chatContainer.children.length % 2 === 0 ? 'left-message' : 'right-message');
    messageElement.classList.add(chatContainer.children.length % 2 === 0 ? 'left-css' : 'right-css');    
    messageElement.classList.add('message'); 
    messageContainer.appendChild(messageElement); 
    messageContainer.classList.add('message-container'); 
    messageContainer.classList.add('text-width');

    if (chatContainer.children.length > 0) {
        messageContainer.classList.add('new-line');
    }
    
    chatContainer.appendChild(messageContainer); 
    chatContainer.scrollTop = chatContainer.scrollHeight;
}


