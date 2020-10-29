$(function() {
    $('#sendBtn').bind('click', function() {

        var value = document.getElementById("msg").value
        document.getElementById("msg").value = null;
        socket.emit('my event', value);
        return false;
    });
});

// This function return the input client name
async function get_name(){
  return await fetch('/get_name')

        .then(async function (response) {
          return await response.json();
      }).then(function (text) {
          return text["name"]
      });
};




// Establish connection with the server
var messageArray = [];
var socket = io.connect('http://' + document.domain + ':' + location.port);
console.log("[CONNECTION] Connection established with server " + document.domain)

// while socket is connect
socket.on('connect', async function() {
    var clientName = await get_name()           // get the client name
    socket.emit('my event', 'I\'m connected!');

});
// Receive messages from server
socket.on('message_response', function( msg ) {
    messageArray.push(msg)
    console.log(messageArray)
});


window.onload = function (){
    var update_loop = setInterval(update, 100);
    update()
};
function update(){
    messages = "";
    for (newMessage of messageArray) {
         messages = messages + "<br>" +newMessage;
    }
    document.getElementById("msgIn").innerHTML = messages;
};