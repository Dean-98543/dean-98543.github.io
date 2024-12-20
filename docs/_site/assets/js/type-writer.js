document.addEventListener('DOMContentLoaded', function() {
    const element = document.querySelector('.hello-title');
    const text = element.getAttribute('data-text');  // 从 data-text 属性获取文本
    let i = 0;

    function typeWriter() {
        if (i < text.length) {
            element.textContent += text.charAt(i);
            i++;
            setTimeout(typeWriter, 150);
        }
    }

    typeWriter();
});