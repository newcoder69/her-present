sendButton = document.getElementById('messageButton');
message = document.getElementById('message');

sendButton.addEventListener("click", function() {
    console.log("Button Clicked")
    const messageValue = message.value;

    fetch("/sendMessage",{
        signal: AbortSignal.timeout(3000),
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({message: messageValue})
    })
    .then(response => {
        if (response.ok){
            document.getElementById('responseOk').innerHTML = "Message Sent Successfully";
        }
    })
    .catch(error => {
        document.getElementById('responseOk').innerHTML = "Error Sending Message" + error;

    })
    
});