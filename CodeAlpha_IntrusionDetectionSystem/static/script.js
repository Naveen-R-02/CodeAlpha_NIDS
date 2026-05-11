const socket = io();

const alertsBody =
    document.getElementById("alertsBody");

const ctx =
    document.getElementById("threatChart");

let threatData = [];

const chart = new Chart(ctx, {
    type: "line",

    data: {
        labels: [],
        datasets: [{
            label: "Threat Activity",
            data: threatData
        }]
    }
});

socket.on("alert", (data) => {

    document.getElementById("packetCount")
        .innerText = data.total_packets;

    document.getElementById("threatCount")
        .innerText = data.threats;

    document.getElementById("highCount")
        .innerText = data.high;

    document.getElementById("mediumCount")
        .innerText = data.medium;

    const row = `
        <tr>
            <td>${data.ip}</td>

            <td>${data.type}</td>

            <td class="${data.severity.toLowerCase()}">
                ${data.severity}
            </td>
        </tr>
    `;

    alertsBody.innerHTML =
        row + alertsBody.innerHTML;

    chart.data.labels.push("");

    threatData.push(data.threats);

    chart.update();

    // Audio Alert
    const audio = new Audio(
        "https://actions.google.com/sounds/v1/alarms/beep_short.ogg"
    );

    audio.play();
});