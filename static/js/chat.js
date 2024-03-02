document.addEventListener("DOMContentLoaded", function () {
  const urlParams = new URLSearchParams(window.location.search);
  // Extract the value of the "user" parameter
  const userurl = urlParams.get("user");
  var chatMessages = document.getElementById("chatMessages");
  // Get the query parameter 'user' from the URL
  const queryParams = new URLSearchParams(window.location.search);
  const user = queryParams.get("user");
  // Activate the tab based on the 'user' query parameter
  const tab = document.querySelector(`[href="/chat/msg/?user=${user}"]`);
  if (tab) {
    tab.classList.add("active");
    tab.setAttribute("aria-selected", "true");
    document.getElementById("username").textContent = user;
  }
  if (user === null) {
    const chatContent = document.querySelector(".chat-content");
    chatContent.style.display = "none";
  }
  var sendButton = document.querySelector(".send-button");
  var textarea = document.querySelector(".message-input");
  var chatMessages = document.querySelector(".chat-messages");
  var ws;
  const spanElement = document.querySelector(".wanted");
  let value = "none";
  // Get the text content of the <span> element
  if (spanElement) {
    value = spanElement.textContent;
  }

  function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  // Function to check for new messages and scroll to bottom if added
  function checkForNewMessages() {
    // Select all elements with class 'js-message' inside the chat messages container
    var newMessages = chatMessages.querySelectorAll(".js-message");

    // If new messages are found, scroll to the bottom
    if (newMessages.length > 0) {
      scrollToBottom();
    }
  }
  setInterval(checkForNewMessages, 100);
  function appendMessage(user, message) {
    var srcValue = "{% static 'images/profilepic.webp' %}";
    let WhoIsUser = "";
    if (
      user === "frnd" &&
      (document.querySelector(".frnd") || document.querySelector(".userme"))
    ) {
      var imgElement = document.querySelector(".frnd");
      srcValue = imgElement.getAttribute("src");
      WhoIsUser = userurl;
    } else {
      var imgElement = document.querySelector(".userme");
      srcValue = imgElement.getAttribute("src");
      WhoIsUser = user;
    }
    if (userurl === usernames || user === value) {
      const chatCard = document.createElement("div");
      chatCard.classList.add(
        "flex",
        "items-start",
        "gap-2.5",
        "m-5",
        "js-messages"
      );

      const profileImg = document.createElement("img");
      profileImg.classList.add("w-10", "h-10", "rounded-full");
      profileImg.src = srcValue;
      profileImg.alt = "Profile Image";
      chatCard.appendChild(profileImg);

      const chatContent = document.createElement("div");
      chatContent.classList.add(
        "flex",
        "flex-col",
        "w-auto",
        "md:w-1/2",
        "leading-1.5"
      );
      const chatBubble = document.createElement("div");
      chatBubble.classList.add(
        "bg-blue-50",
        "dark:bg-black",
        "p-4",
        "rounded-lg",
        "shadow-md"
      );

      const nameTimeContainer = document.createElement("div");
      nameTimeContainer.classList.add(
        "flex",
        "items-center",
        "space-x-2",
        "rtl:space-x-reverse"
      );
      const nameSpan = document.createElement("span");
      nameSpan.classList.add(
        "text-sm",
        "font-semibold",
        "text-gray-900",
        "dark:text-white"
      );
      nameSpan.textContent = WhoIsUser;
      const timeSpan = document.createElement("span");
      timeSpan.classList.add(
        "text-sm",
        "font-normal",
        "text-gray-500",
        "dark:text-gray-400"
      );

      // Create a new Date object
      var now = new Date();

      // Get the current date and time components
      var year = now.getFullYear();
      var month = now.getMonth() + 1; // Month is zero-based, so add 1
      var day = now.getDate();
      var hours = now.getHours();
      var minutes = now.getMinutes();

      // Format the date and time as desired
      var formattedDateTime =
        year + "-" + month + "-" + day + " " + hours + ":" + minutes;
      timeSpan.textContent = formattedDateTime;
      nameTimeContainer.appendChild(nameSpan);
      nameTimeContainer.appendChild(timeSpan);

      const messageTextarea = document.createElement("textarea");
      messageTextarea.id = "message";
      messageTextarea.rows = "4";
      messageTextarea.classList.add(
        "block",
        "chat-card",
        "p-2.5",
        "w-full",
        "text-sm",
        "text-gray-900",
        "bg-gray-50",
        "rounded-lg",
        "border",
        "border-gray-300",
        "focus:ring-blue-500",
        "focus:border-blue-500",
        "dark:bg-gray-700",
        "dark:border-gray-600",
        "dark:placeholder-gray-400",
        "dark:text-white",
        "dark:focus:ring-blue-500",
        "dark:focus:border-blue-500"
      );
      messageTextarea.placeholder = message;

      chatBubble.appendChild(nameTimeContainer);
      chatBubble.appendChild(messageTextarea);
      chatContent.appendChild(chatBubble);
      chatCard.appendChild(chatContent);

      const dropdownButton = document.createElement("button");
      dropdownButton.id = "dropdownMenuIconButton";
      dropdownButton.setAttribute("data-dropdown-toggle", "dropdownDots");
      dropdownButton.setAttribute("data-dropdown-placement", "bottom-start");
      dropdownButton.classList.add(
        "inline-flex",
        "self-center",
        "items-center",
        "p-2",
        "text-sm",
        "font-medium",
        "text-center",
        "text-gray-900",
        "bg-white",
        "rounded-lg",
        "hover:bg-gray-100",
        "focus:ring-4",
        "focus:outline-none",
        "dark:text-white",
        "focus:ring-gray-50",
        "dark:bg-gray-900",
        "dark:hover:bg-gray-800",
        "dark:focus:ring-gray-600"
      );
      dropdownButton.type = "button";
      const dropdownIcon = document.createElement("svg");
      dropdownIcon.classList.add(
        "w-4",
        "h-4",
        "text-gray-500",
        "dark:text-gray-400"
      );
      dropdownIcon.setAttribute("aria-hidden", "true");
      dropdownIcon.setAttribute("xmlns", "http://www.w3.org/2000/svg");
      dropdownIcon.setAttribute("fill", "currentColor");
      dropdownIcon.setAttribute("viewBox", "0 0 4 15");
      const dropdownPath = document.createElement("path");
      dropdownPath.setAttribute(
        "d",
        "M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z"
      );
      dropdownIcon.appendChild(dropdownPath);
      dropdownButton.appendChild(dropdownIcon);
      chatCard.appendChild(dropdownButton);

      const dropdownContent = document.createElement("div");
      dropdownContent.id = "dropdownDots";
      dropdownContent.classList.add(
        "z-10",
        "hidden",
        "bg-white",
        "rounded-lg",
        "shadow-md",
        "dark:bg-gray-700"
      );
      const dropdownList = document.createElement("ul");
      dropdownList.classList.add(
        "py-1",
        "text-sm",
        "text-gray-700",
        "dark:text-gray-200"
      );
      dropdownList.setAttribute("aria-labelledby", "dropdownMenuIconButton");
      const dropdownItems = ["Reply", "Forward", "Copy", "Report", "Delete"];
      dropdownItems.forEach((item) => {
        const li = document.createElement("li");
        const a = document.createElement("a");
        a.classList.add(
          "block",
          "px-4",
          "py-2",
          "hover:bg-gray-100",
          "dark:hover:bg-gray-600",
          "dark:hover:text-white"
        );
        a.href = "#";
        a.textContent = item;
        li.appendChild(a);
        dropdownList.appendChild(li);
      });
      dropdownContent.appendChild(dropdownList);
      chatCard.appendChild(dropdownContent);

      chatMessages.appendChild(chatCard);
    }
    scrollToBottom();
  }
  let usernames = "m0";
  // Function to send a message via WebSocket
  function sendMessage(message) {
    if (ws && ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify({ user: user, msg: message }));
      val = JSON.stringify({ user: user });
      const parsedVal = JSON.parse(val);
      usernames = parsedVal.user;
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
    console.log(event.data);
    const data = JSON.parse(event.data);
    const uniqueid = data.uniqueid;
    console.log(uniqueid, "myr id");
    appendMessage("frnd", event.data);
  });

  // Handle WebSocket close
  ws.addEventListener("close", function (event) {
    console.log("WebSocket connection closed.");
  });

  // Handle Send button click
  sendButton.addEventListener("click", function () {
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
