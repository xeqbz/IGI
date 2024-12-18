window.addEventListener('scroll', () => {
    // Получаем текущее значение прокрутки
    const scrollPosition = window.scrollY;

    // Все элементы с классом chair
    const chairs = document.querySelectorAll('.chair');

    chairs.forEach((chair, index) => {
        // Рассчитываем вращение на основе позиции прокрутки и индекса элемента
        const rotation = (scrollPosition / 10) + (index * 45);
        chair.style.setProperty('--rotation', rotation);
    });
});

