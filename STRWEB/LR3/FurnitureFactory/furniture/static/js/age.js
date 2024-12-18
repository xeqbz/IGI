document.getElementById("checkAge").addEventListener("click", function() {
    const birthdateInput = document.getElementById("birthdate").value;
    if (!birthdateInput) {
        alert("Пожалуйста, введите вашу дату рождения.");
        return;
    }

    const birthdate = new Date(birthdateInput);
    const currentDate = new Date();
    const resultElement = document.getElementById("result");

    if (birthdate > currentDate) {
        alert("Дата рождения не может быть в будущем.");
        resultElement.innerHTML = "Дата рождения не может быть в будущем.";
        return;
    }

    const age = currentDate.getFullYear() - birthdate.getFullYear();

    const isBirthdayPassed = currentDate.getMonth() > birthdate.getMonth() || (currentDate.getMonth() === birthdate.getMonth() && currentDate.getDate() >= birthdate.getDate());
    const actualAge = isBirthdayPassed ? age : age - 1;

    const daysOfWeek = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"];
    const birthDayOfWeek = daysOfWeek[birthdate.getDay()];

    if (actualAge < 18) {
        resultElement.innerHTML = `Вы несовершеннолетний. Пожалуйста, получите разрешение родителей для использования сайта.`;
        alert("Вы несовершеннолетний. Пожалуйста, получите разрешение родителей.");
    } else {
        resultElement.innerHTML = `Ваш возраст: ${actualAge} лет. День недели вашего рождения: ${birthDayOfWeek}.`;
    }
});