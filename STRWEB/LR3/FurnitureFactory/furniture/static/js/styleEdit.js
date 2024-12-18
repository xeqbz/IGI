document.addEventListener("DOMContentLoaded", () => {
    const toggleCheckbox = document.getElementById("customize-toggle");
    const customizePanel = document.getElementById("customize-panel");
    const fontSizeSlider = document.getElementById("font-size-slider");
    const textColorPicker = document.getElementById("text-color-picker");
    const backgroundColorPicker = document.getElementById("background-color-picker");
    const titles = document.querySelectorAll('.news');

    toggleCheckbox.addEventListener("change", () => {
        if (toggleCheckbox.checked) {
            customizePanel.style.display = "block";
        } else {
            customizePanel.style.display = "none";
        }
    });

    fontSizeSlider.addEventListener("input", () => {
        titles.forEach((title) => {
            title.style.fontSize = `${fontSizeSlider.value}px`;
        })
    });

    textColorPicker.addEventListener("input", () => {
        titles.forEach((title) => {
            title.style.color = textColorPicker.value;
        })
    });

    backgroundColorPicker.addEventListener("input", () => {
        document.body.style.backgroundColor = backgroundColorPicker.value;
    });
});