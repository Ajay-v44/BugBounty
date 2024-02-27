document.addEventListener("DOMContentLoaded", function () {
    // Get the query parameter 'user' from the URL
    const queryParams = new URLSearchParams(window.location.search);
    const user = queryParams.get("user");

    // Activate the tab based on the 'user' query parameter
    const tab = document.querySelector(`[href="/chat/msg/?user=${user}"]`);
    if (tab) {
        tab.classList.add("active");
        tab.setAttribute("aria-selected", "true");
        document.getElementById('username').textContent = user
    }
    if (user === null) {
        const chatContent = document.querySelector('.chat-content');
        chatContent.style.display = 'none';
    }
    var sendButton = document.querySelector(".send-button");
    var textarea = document.querySelector(".message-input");
    var chatMessages = document.querySelector(".chat-messages");
    var ws;

    // Function to append a received message to chat messages
    function appendMessage(user, message) {
        const chatCard = document.createElement("div");
        chatCard.classList.add(user === "me" ? "chat-card" : "otherchat");
        chatCard.innerHTML = `<p>${message}</p>`;
        chatMessages.appendChild(chatCard);
    }

    // Function to send a message via WebSocket
    function sendMessage(message) {
        if (ws && ws.readyState === WebSocket.OPEN) {
            ws.send(JSON.stringify({ user: user, msg: message }));
        }
    }

    // Connect to the WebSocket server
    ws = new WebSocket("ws://127.0.0.1:8000/chat/msg/ws/wsc/");

    // Handle WebSocket connection open
    ws.addEventListener("open", function (event) {
        console.log("WebSocket connection opened.");
    });

    // Handle WebSocket message received
    ws.addEventListener("message", function (event) {
        console.log(event.data) 
        appendMessage("frnd",event.data);
    });

    // Handle WebSocket close
    ws.addEventListener("close", function (event) {
        console.log("WebSocket connection closed.");
    });

    // Handle Send button click
    sendButton.addEventListener('click', function () {
        const messageText = textarea.value;

        if (messageText.trim() !== "") {
            sendMessage(messageText);

            // Append the sent message to chat messages
            appendMessage("me", messageText);

            // Clear the textarea
            textarea.value = "";
        }
    });
});
