document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('http://localhost:8000/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            user_name: username,
            password: password,
        }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('message').innerText = '登録成功！';
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('message').innerText = '登録失敗';
    });
});
