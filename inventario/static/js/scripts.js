document.addEventListener("DOMContentLoaded", () => {
    console.log("Sistema cargado correctamente");
    const botonesEliminar = document.querySelectorAll(".btn-danger");
    botonesEliminar.forEach((boton) => {
        boton.addEventListener("click", (e) => {
            const respuesta = confirm(
                "¿Deseas eliminar este producto?"
            );
            if (!respuesta) {
                e.preventDefault();
            }
        });
    });
});