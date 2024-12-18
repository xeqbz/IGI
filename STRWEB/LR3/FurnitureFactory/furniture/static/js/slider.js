class Slider {
    constructor(sliderElement, linkElement, textElement, images, options = {}) {
        this.sliderElement = sliderElement;
        this.linkElement = linkElement;
        this.textElement = textElement; // Элемент для подписи
        this.images = images;
        this.currentIndex = 0;
        this.interval = options.auto ? (options.delay || 5000) : null; // Используем delay, если auto=true
        this.timer = null;

        // Дополнительные параметры
        this.loop = options.loop || false;  // Если true, слайдер будет цикличным
        this.navs = options.navs !== undefined ? options.navs : true; // Показ стрелок
        this.pags = options.pags !== undefined ? options.pags : true; // Показ пагинации
        this.auto = options.auto !== undefined ? options.auto : false; // Автопереключение
        this.stopMouseHover = options.stopMouseHover || false; // Остановка слайдера при наведении мыши
        this.delay = options.delay || 5000; // Время задержки между слайдами, если auto=true

        // Элементы для управления слайдами и пагинацией
        this.prevButton = document.querySelector('#prev-slide');
        this.nextButton = document.querySelector('#next-slide');
        this.pagination = document.querySelector('#pagination');
        this.slideNumber = document.querySelector('#slider-text');

        this.initSlider();
    }

    initSlider() {
        if (this.auto) {
            this.startSlider();
            if (this.stopMouseHover) {
                this.sliderElement.addEventListener('mouseenter', () => this.stopSlider());
                this.sliderElement.addEventListener('mouseleave', () => this.startSlider());
            }
        }

        if (this.navs) {
            this.prevButton.addEventListener('click', () => this.prevSlide());
            this.nextButton.addEventListener('click', () => this.nextSlide());
        } else {
            this.prevButton.style.display = 'none';
            this.nextButton.style.display = 'none';
        }

        if (this.pags) {
            this.createPagination();
        } else {
            this.pagination.style.display = 'none';
        }

        this.updateSlide();
    }

    changeSlide() {
        if (this.loop) {
            this.currentIndex = (this.currentIndex + 1) % this.images.length;
        } else {
            if (this.currentIndex < this.images.length - 1) {
                this.currentIndex++;
            }
        }
        this.updateSlide();
    }

    prevSlide() {
        if (this.loop) {
            this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
        } else {
            if (this.currentIndex > 0) {
                this.currentIndex--;
            }
        }
        this.updateSlide();
    }

    nextSlide() {
        this.changeSlide();
    }

    updateSlide() {
        const { src, link, text } = this.images[this.currentIndex];
        this.sliderElement.src = src;
        this.linkElement.href = link;
        this.textElement.innerText = text; // Подпись к слайду
        this.updateSlideNumber(); // Обновляем номер слайда
        this.updatePagination(); // Обновляем пагинацию
    }

    updateSlideNumber() {
        const totalSlides = this.images.length;
        const currentSlide = this.currentIndex + 1; // Индексация с 1
        this.slideNumber.innerText = `${currentSlide} / ${totalSlides}`;
    }

    startSlider() {
        this.timer = setInterval(() => this.changeSlide(), this.interval);
    }

    stopSlider() {
        clearInterval(this.timer);
    }

    updateInterval(newInterval) {
        this.stopSlider();
        this.interval = newInterval;
        this.startSlider();
    }

    createPagination() {
        this.pagination.innerHTML = '';
        this.images.forEach((_, index) => {
            const pageButton = document.createElement('button');
            pageButton.classList.add('pagination-button');
            pageButton.addEventListener('click', () => this.goToSlide(index));
            this.pagination.appendChild(pageButton);
        });
        this.updatePagination(); // Обновляем пагинацию сразу
    }

    updatePagination() {
        const paginationButtons = document.querySelectorAll('.pagination-button');
        paginationButtons.forEach((button, index) => {
            button.classList.remove('active');
            if (index === this.currentIndex) {
                button.classList.add('active');
            }
        });
    }

    goToSlide(index) {
        this.currentIndex = index;
        this.updateSlide();
    }
}

// Пример конфигурации слайдера с дополнительными параметрами
const images = [
    { src: `${staticUrl}banner1.jpg`, link: "/news", text: "Новости" },
    { src: `${staticUrl}banner2.jpg`, link: "/about", text: "О нас" },
    { src: `${staticUrl}banner3.png`, link: "/contacts", text: "Контакты" }
];

const options = {
    loop: true,  // Зацикливание слайдера
    navs: true,  // Показ стрелок
    pags: true,  // Показ пагинации
    auto: true,  // Автоматическая смена слайдов
    stopMouseHover: true, // Остановка при наведении
    delay: 5000,  // Задержка на 5 секунд
};

const sliderImage = document.querySelector('.footer-banner');
const sliderLink = document.querySelector('#slider-link');
const sliderText = document.querySelector('#slider-text'); // Элемент для текста
const intervalInput = document.querySelector('#interval');
const updateButton = document.querySelector('#update-interval');

const slider = new Slider(sliderImage, sliderLink, sliderText, images, options);

// Обновление интервала слайдера
updateButton.addEventListener('click', () => {
    const newInterval = parseInt(intervalInput.value, 10);
    if (newInterval >= 1000) {
        slider.updateInterval(newInterval);
        alert('Интервал обновлен');
    } else {
        alert('Интервал должен быть больше 1000мс');
    }
});

