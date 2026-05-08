document.getElementById('formContacto').addEventListener('submit', async function(e){
    e.preventDefault();

    const msg = document.getElementById('msgEstado');
    msg.innerHTML = "Enviando...";
    msg.className = "text-info";

    const datos = new FormData(this);

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    try {
        const res = await fetch('/contacto/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken
            },
            body: datos
        });

        const data = await res.json();

        msg.innerHTML = data.mensaje;
        msg.className = "text-success";

        this.reset();
    } catch (error) {
        msg.innerHTML = "Error al enviar el formulario";
        msg.className = "text-danger";
    }
});