// py-loader.js
hljs.highlightAll();

document.addEventListener('DOMContentLoaded', function () {
    // 获取 URL 中的文件参数
    const queryParams = new URLSearchParams(window.location.search);
    const codeFile = queryParams.get('file');  // 获取名为 'file' 的查询参数

    // 构建文件路径并进行 fetch 操作
    const baseFilePath = "code/leetcode/";  // 设置基础文件路径
    const filePath = codeFile ? `${baseFilePath}${codeFile}` : `${baseFilePath}hello.py`; // 构建完整的文件路径

    fetch(filePath)
        .then(response => response.text())
        .then(text => {
            const codeContainer = document.getElementById('code-container');
            if (codeContainer) {
                codeContainer.textContent = text;
                hljs.highlightAll();  // 确保代码高亮
            } else {
                console.error('Code container element not found.');
            }
        })
        .catch(error => console.error('Error loading the file:', error));
});