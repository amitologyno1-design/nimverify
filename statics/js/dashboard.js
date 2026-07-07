document.addEventListener("DOMContentLoaded", function () {

    // Animate numbers
    const counters = document.querySelectorAll(".card h1");

    counters.forEach(counter => {

        let target = parseInt(counter.innerText.replace(/[^0-9]/g, "")) || 0;

        let count = 0;

        let speed = 20;

        function updateCounter() {

            if (count < target) {

                count++;

                if (counter.innerText.includes("₦")) {
                    counter.innerText = "₦" + count.toFixed(2);
                } else {
                    counter.innerText = count;
                }

                setTimeout(updateCounter, speed);
            }

        }

        updateCounter();

    });

});