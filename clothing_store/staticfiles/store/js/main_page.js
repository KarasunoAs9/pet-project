document.addEventListener('DOMContentLoaded', () => {
    const heroTitle = document.querySelector('.hero-section-title');
    const heroText = document.querySelector('.hero-section-text');
    const heroButton = document.querySelector('.hero-section-button');

    if (heroTitle && heroText && heroButton) {
        setTimeout(() => {
            heroTitle.classList.add('visible');
        }, 200); // Заголовок появляется через 200 мс

        setTimeout(() => {
            heroText.classList.add('visible');
        }, 400); // Текст появляется через 400 мс

        setTimeout(() => {
            heroButton.classList.add('visible');
        }, 1000); // Кнопка появляется через 600 мс
    }
});
