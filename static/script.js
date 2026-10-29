const rideForm = document.getElementById('ride-form');
rideForm.addEventListener("submit", function(event) {
	event.preventDefault();
        const trail = document.getElementById("trail").value;
        const miles = Number(document.getElementById("miles").value);
        const minutes = Number(document.getElementById("minutes").value);
        const message = document.getElementById("ride-message");
        const rideData = {
            trail: trail,
            miles: miles,
            minutes: minutes
        };
        fetch("http://127.0.0.1:8000/rides", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(rideData)
        })
        .then(response => response.json())
        .then(data => {
            message.textContent = data.message
        })
        .catch(error => {
            message.textContent = "Could not save ride. Check API connection";
        });
});
function loadRides() {
        const history = document.getElementById("ride-history");

    fetch("/rides")
        .then(response => response.json())
        .then(rides => {
            history.innerHTML = "";

            rides.forEach(ride => {
                const item = document.createElement("p");
                item.textContent = `${ride[1]} — ${ride[2]} miles — ${ride[3]} minutes`;
                history.appendChild(item);
            });
        });
}
loadRides();