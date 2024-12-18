document.addEventListener("DOMContentLoaded", function() {
    const productsPerPage = 3; // Число товаров на одну страницу
    const products = document.querySelectorAll('.product-item'); // Все товары на странице
    const totalPages = Math.ceil(products.length / productsPerPage); // Общее количество страниц
    let currentPage = 1; // Текущая страница

    // Функция для отображения товаров на текущей странице
    function showPage(page) {
        // Скрываем все товары
        products.forEach((product, index) => {
            product.style.display = 'none';
            // Показываем товары только для текущей страницы
            if (index >= (page - 1) * productsPerPage && index < page * productsPerPage) {
                product.style.display = 'block';
            }
        });
    }

    // Функция для создания кнопок пагинации
    function createPagination() {
        const pagination = document.getElementById('pagination');
        pagination.innerHTML = ''; // Очищаем старую пагинацию

        // Создаем кнопки для перехода по страницам
        for (let page = 1; page <= totalPages; page++) {
            const button = document.createElement('button');
            button.textContent = page;
            button.addEventListener('click', function() {
                currentPage = page;
                showPage(currentPage);
                updatePaginationButtons();
            });
            pagination.appendChild(button);
        }
    }

    // Функция для обновления активной кнопки пагинации
    function updatePaginationButtons() {
        const buttons = document.querySelectorAll('.pagination button');
        buttons.forEach(button => {
            button.classList.remove('active');
            if (parseInt(button.textContent) === currentPage) {
                button.classList.add('active');
            }
        });
    }

    // Инициализируем отображение товаров и пагинацию
    showPage(currentPage);
    createPagination();
    updatePaginationButtons();
});

