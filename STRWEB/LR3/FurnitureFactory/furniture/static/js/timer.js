document.addEventListener('DOMContentLoaded', () => {
    const timerElement = document.getElementById('countdown-timer');
    const oneHourInMins = 60 * 60 * 1000;

    const now = new Date().getTime();

    let endTime = localStorage.getItem('countdownEndTime');

    if(!endTime){
        endTime = now + oneHourInMins;
        localStorage.setItem('countdownEndTime', endTime);
    } else {
        if (now > endTime){
            endTime = now + oneHourInMins;
            localStorage.setItem('countdownEndTime', endTime);
        }
    }

    const updateCountdown = () => {
        const now = new Date().getTime();
        const timeLeft = endTime - now;

        if (timeLeft > 0){
            const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

            timerElement.textContent = `${hours.toString().padStart(2, '0')}:${minutes
                .toString()
                .padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
        } else {
            timerElement.textContent = 'Время вышло!';
            clearInterval(timerInterval);
            localStorage.removeItem('countdownEndTime');
        }
    };

    const timerInterval = setInterval(updateCountdown, 1000);
    updateCountdown();
})