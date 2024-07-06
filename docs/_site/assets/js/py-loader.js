// py-loader.js
hljs.highlightAll();

document.addEventListener('DOMContentLoaded', function () {
    // 获取 URL 中的文件参数
    const queryParams = new URLSearchParams(window.location.search);
    const codeFile = queryParams.get('file');  // 获取名为 'file' 的查询参数

    // 构建文件路径并进行 fetch 操作
    const filePath = codeFile ? `code/leetcode/${codeFile}` : 'code/leetcode/hello.py'; // 默认文件路径

    fetch(filePath)
        .then(response => response.text())
        .then(text => {
            document.getElementById('code-container').textContent = text;
            hljs.highlightAll();  // 确保代码高亮
        })
        .catch(error => console.error('Error loading the file:', error));
});