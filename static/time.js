


function displayTime () {
     let dateTime = new Date();
     let hour = dateTime.getHours();
     let minute = dateTime.getMinutes();
     let second = dateTime.getSeconds();

     if (hour === 0) {
            hour = 12;
     }
     else if (hour > 12) {
            hour = hour - 12;
     }

     document.getElementById("hour").innerHTML = `${hour}:`;
     document.getElementById("minute").innerHTML = `${minute}:`;
     document.getElementById("second").innerHTML = `${second}`;
}

setInterval(displayTime, 10);