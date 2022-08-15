


function displayTime () {
     let dateTime = new Date();
     let hour = dateTime.getHours();
     let minute = dateTime.getMinutes();
     let second = dateTime.getSeconds();
     let time = document.getElementById("time");


     document.getElementById("hour").innerHTML = `${hour}:`;
     document.getElementById("minute").innerHTML = `${minute}:`;
     document.getElementById("second").innerHTML = `${second}`;
}

setInterval(displayTime, 10);