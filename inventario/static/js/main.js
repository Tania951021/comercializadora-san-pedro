document.getElementById('formContacto').addEventListener('submit', async function(e){
    e.preventDefault();

    const msg = document.getElementById('msgEstado');
    msg.innerHTML = "Enviando...";
    msg.className = "text-info";

    const datos = new FormData(this);

    try {
        const res = await fetch('/api/contacto/', {
            method: 'POST',
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