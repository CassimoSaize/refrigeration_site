// Smooth scroll para links internos (reforço)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// Feedback visual no formulário (validação simples)
const form = document.querySelector('form');
if (form) {
    form.addEventListener('submit', function (e) {
        const name = form.querySelector('input[name="name"]').value.trim();
        const phone = form.querySelector('input[name="phone"]').value.trim();
        const msg = form.querySelector('textarea[name="message"]').value.trim();
        if (!name || !phone || !msg) {
            e.preventDefault();
            alert('Por favor, preencha todos os campos.');
        }
    });
}