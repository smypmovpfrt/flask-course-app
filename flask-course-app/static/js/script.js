// Получаем элемент инпута
const inputField = document.querySelector('.txt_input');

// Добавляем обработчик события "клик"
inputField.addEventListener('click', function() {
    // Проверяем, пуст ли инпут, чтобы не очищать его снова, если он уже пуст
    if (inputField.value === "Ваша ссылка:") {
        inputField.value = ''; // Очищаем инпут
    }
});

// Дополнительно: предотвращаем очистку, если пользователь уже начал вводить текст
inputField.addEventListener('focus', function() {
    if (inputField.value === "Ваша ссылка:") {
        inputField.value = ''; // Очищаем инпут при получении фокуса
    }
});

// Восстанавливаем текст, если инпут остается пустым
inputField.addEventListener('blur', function() {
    if (inputField.value === '') {
        inputField.value = 'Ваша ссылка:'; // Восстанавливаем текст
    }
});