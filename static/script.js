
async function updateDHT11() {
    const response = await fetch('/data');
    const data = await response.json();

    if (json.error) {
        return;
    }
    else {
        document.getElementById('temp').innerText = ` Current Temperature : ${data.temperature.toFixed(1)} °C`;
        document.getElementById('hum').innerText = ` Current Humidity : ${data.humidity.toFixed(1)} %`;
    }
}

setInterval(updateDHT11, 1000);