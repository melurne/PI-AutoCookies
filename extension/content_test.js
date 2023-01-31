var websocket;

websocket = new WebSocket("ws://localhost:8765/");

websocket.onopen = () => {
    console.log("opened socket")
};

websocket.onmessage = (event) => {
    console.log(event.data);
};

setTimeout(() => {websocket.send("hi !");}, 1000)



