var joy = new JoyStick('joyDiv');
var updatePeriod = 500; //miliseconds
var connection_active_btn = document.getElementById("connection_active");
var timeout_id = null;
var mySocket;

function initSocket(){
    mySocket = new WebSocket("ws://192.168.0.24:13254", "joystick_protocol");
    setInterval(updateState, 50);
    mySocket.onopen = (event) => {
        document.getElementById("socketState").style.color = "green";
        connection_active_btn.checked = true;
        updateJoy();
      }
    
    mySocket.onclose = (event) => {
        document.getElementById("socketState").style.color = "red";
        connection_active_btn.checked = false;
      }
}

initSocket();

function updateState(){
    var p = document.getElementById("socketState");
    var state = mySocket.readyState;
    switch (state) {
        case 0:
            p.innerHTML = "CONNECTING";
            break;
        case 1:
            p.innerHTML = "OPEN";
            break;
        case 2:
            p.innerHTML = "CLOSING";
            break;
        case 3:
            p.innerHTML = "CLOSED";
            break;
    }
}

connection_active_btn.onchange = function(){
    if (connection_active_btn.checked && mySocket.readyState == 3){
        initSocket();
    } else if (!connection_active_btn.checked && mySocket.readyState == 1){
        mySocket.close();
    }
}

function updateJoy(){
    const output = document.getElementById("joy-output");
    let x_value = joy.GetX();
    let y_value = joy.GetY();
    let direction = joy.GetDir();
    let lights = document.getElementById('LEDswitch').checked
    output.innerHTML = `X = ${x_value}, Y = ${y_value}, DIR: ${direction}`;
    let msg = {
        dir : direction,
        lights : lights
    }
    if (mySocket.readyState = 1) {
        mySocket.send(JSON.stringify(msg));   
    }
    updatePeriod = document.querySelector('input[name="sendingRateRadio"]:checked').value;
    timeout_id = setTimeout(updateJoy, updatePeriod);
}

