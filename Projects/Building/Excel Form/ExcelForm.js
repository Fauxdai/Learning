document.getElementById('excelForm').addEventListener('submit', function (event) {
    event.preventDefault();
    
    const formData = new FormData(this);
    const data = {};
    
    formData.forEach((value, key) => {
        data[key] = key === 'proUser' || key === 'loaner' ? value === 'on' : value;
    });

    fetch('/submit', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.text())
    .then(message => {
        alert(message);
        this.reset();
    });
});
