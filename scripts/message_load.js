
var ws = new WebSocket("ws://127.0.0.1:8000/ws");

ws.onmessage = function(event) {
    var messages = document.getElementById('messages');
    var data = JSON.parse(event.data)
    messages.insertAdjacentHTML('beforeend',  data.ID + " " + data.text + "<br>");
};

function sendMessage(event) {
    var input = document.getElementById("messageText");
    var data = {text: input.value};
    ws.send(JSON.stringify(data));
    input.value = "";
    event.preventDefault();
};