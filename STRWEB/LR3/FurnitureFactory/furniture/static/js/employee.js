function sortTable(columnIndex) {
    let table = document.getElementById("employeeTable");
    let rows = Array.from(table.rows).slice(1);  // Получаем все строки без заголовков
    let isSortedAsc = table.rows[0].cells[columnIndex].classList.contains('sorted-asc'); // Проверяем текущее направление сортировки

    // Сортируем строки
    rows.sort((rowA, rowB) => {
        let cellA = rowA.cells[columnIndex].innerText;
        let cellB = rowB.cells[columnIndex].innerText;

        // Если это фото, сравниваем по URL
        if (columnIndex === 1) {
            cellA = rowA.cells[columnIndex].querySelector('img').src;
            cellB = rowB.cells[columnIndex].querySelector('img').src;
        }

        // Сортируем по возрастанию или убыванию в зависимости от флага
        return (isSortedAsc ? cellA.localeCompare(cellB) : cellB.localeCompare(cellA));
    });

    table.tBodies[0].append(...rows);  // Перемещаем отсортированные строки

    // Убираем стрелку с других столбцов
    let headers = table.querySelectorAll("th");
    headers.forEach((header, index) => {
        if (index !== columnIndex) {
            header.classList.remove('sorted-asc', 'sorted-desc');
        }
    });

    // Добавляем классы для выбранного столбца
    const header = table.rows[0].cells[columnIndex];
    const directionSpan = header.querySelector('.sort-direction'); // Находим элемент для стрелки

    // Переключаем направление сортировки
    if (isSortedAsc) {
        header.classList.remove('sorted-asc');
        header.classList.add('sorted-desc');
    } else {
        header.classList.remove('sorted-desc');
        header.classList.add('sorted-asc');
    }
}


// Фильтрация таблицы
function filterTable() {
    const filterText = document.getElementById("filterText").value.toLowerCase();  // Получаем текст фильтра
    const rows = document.querySelectorAll(".employee-row");  // Получаем все строки таблицы
    let found = false;  // Переменная для отслеживания найденных результатов

    rows.forEach(row => {
        // Получаем значения всех ячеек для текущей строки
        const name = row.cells[0].innerText.toLowerCase();
        const position = row.cells[2].innerText.toLowerCase();
        const contactInfo = row.cells[3].innerText.toLowerCase();
        const email = row.cells[4].innerText.toLowerCase();

        // Проверяем, содержит ли какой-либо из столбцов введенный текст
        if (name.includes(filterText) || position.includes(filterText) || contactInfo.includes(filterText) || email.includes(filterText)) {
            row.style.display = "";  // Показываем строку
            found = true;  // Найдено хотя бы одно совпадение
        } else {
            row.style.display = "none";  // Скрываем строку
        }
    });

    // Отображаем сообщение, если ничего не найдено
    const noResultsMessage = document.getElementById("noResultsMessage");
    if (!found) {
        if (!noResultsMessage) {
            const message = document.createElement("p");
            message.id = "noResultsMessage";
            message.textContent = "Ничего не найдено.";
            document.querySelector("#employeeTable").insertAdjacentElement("beforebegin", message);
        }
    } else {
        if (noResultsMessage) {
            noResultsMessage.remove();  // Убираем сообщение, если результаты найдены
        }
    }
}

let currentPage = new URLSearchParams(window.location.search).get('page') || 1;
currentPage = parseInt(currentPage); // Начинаем с первой страницы

function changePage(direction) {
    if (direction === 'prev' && currentPage > 1) {
        currentPage--;
    } else if (direction === 'next') {
        currentPage++;
    }
    paginate();
}

function paginate() {
    let url = new URL(window.location.href);
    url.searchParams.set('page', currentPage);  // Устанавливаем параметр page
    window.location.href = url.toString();  // Перезагружаем страницу с новым параметром
}

// Открытие формы добавления сотрудника
function openAddEmployeeForm() {
    document.getElementById("addEmployeeForm").style.display = "block";
}

// Добавление сотрудника
document.getElementById("employeeForm").addEventListener("submit", function(event) {
    event.preventDefault();  // Предотвращаем перезагрузку страницы при отправке формы

    // Получаем данные формы
    const formData = new FormData(event.target);
    const fullName = formData.get('full_name');
    const photoUrl = formData.get('photo_url');
    const position = formData.get('position');
    const phone = formData.get('phone');
    const email = formData.get('email');

    // Валидация данных
    if (!validateUrl(photoUrl)) {
        alert("Некорректный URL!");
        return;
    }
    if (!validatePhone(phone)) {
        alert("Некорректный номер телефона!");
        return;
    }

    // Отправляем данные на сервер
    const requestData = {
        method: 'POST',
        body: JSON.stringify({
            full_name: fullName,
            photo_url: photoUrl,
            position: position,
            phone: phone,
            email: email
        }),
        headers: {
            'Content-Type': 'application/json',  // Указываем, что данные передаются в формате JSON
        }
    };

    // Асинхронный запрос на сервер
    fetch('/add_employee/', requestData)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("Сотрудник успешно добавлен!");
                location.reload(); // Перезагружаем страницу, чтобы отобразить новые данные
            } else {
                alert("Ошибка при добавлении сотрудника.");
            }
        })
        .catch(error => {
            alert("Произошла ошибка: " + error);
        });
});

// Показ деталей сотрудника
document.querySelectorAll(".employee-row").forEach(row => {
    row.addEventListener("click", function() {
        const details = `
            <h3>Детали сотрудника</h3>
            <p>ФИО: ${row.cells[0].innerText}</p>
            <p>Должность: ${row.cells[2].innerText}</p>
            <p>Телефон: ${row.cells[3].innerText}</p>
            <p>Email: ${row.cells[4].innerText}</p>
        `;
        document.getElementById("employeeDetails").innerHTML = details;
    });
});

function validateUrl(url) {
    // Регулярное выражение для проверки корректности URL
    const regex = /^(https?:\/\/(?:www\.)?[\w-]+(?:\.[a-z]{2,})+\/?.*\.((html|php))$)/i;
    return regex.test(url);  // Возвращает true, если URL валиден
}

function validatePhone(phone) {
    // Регулярное выражение для проверки корректности номера телефона
    const regex = /^(?:\+375|8) ?(?:\(\d{2}\)|\d{2}) ?\d{3}[- ]?\d{2}[- ]?\d{2}$/;
    return regex.test(phone);  // Возвращает true, если номер телефона валиден
}

function rewardSelected() {
    // Получаем все выбранные чекбоксы
    const checkboxes = document.querySelectorAll('.employee-checkbox:checked');
    const selectedEmployees = [];

    // Проходим по всем выбранным чекбоксам и добавляем фамилии сотрудников в массив
    checkboxes.forEach(checkbox => {
        const employeeName = checkbox.getAttribute('data-name');  // Извлекаем имя сотрудника
        selectedEmployees.push(employeeName);
    });

    // Проверяем, есть ли выбранные сотрудники
    if (selectedEmployees.length > 0) {
        const rewardText = `Премированы следующие сотрудники: ${selectedEmployees.join(', ')}`;

        // Отображаем текст премирования
        document.getElementById('rewardText').textContent = rewardText;
        document.getElementById('rewardMessage').style.display = 'block';  // Показываем сообщение
    } else {
        // Если никто не выбран, скрываем сообщение
        document.getElementById('rewardMessage').style.display = 'none';
    }
}


