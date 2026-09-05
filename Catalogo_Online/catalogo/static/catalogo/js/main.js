document.addEventListener('DOMContentLoaded', function() {
    // Elementos del DOM
    const buscador = document.getElementById('buscador');
    const tarjetas = document.querySelectorAll('.producto-card');
    const contadorVisible = document.getElementById('contador-visible');

    // Función de filtrado
    function filtrarProductos() {
        const texto = buscador.value.toLowerCase().trim();
        let visibles = 0;

        tarjetas.forEach(tarjeta => {
            const nombre = tarjeta.dataset.nombre.toLowerCase();
            const categoria = tarjeta.dataset.categoria.toLowerCase();
            const coincide = nombre.includes(texto) || categoria.includes(texto);

            if (coincide) {
                tarjeta.style.display = 'block';
                visibles++;
            } else {
                tarjeta.style.display = 'none';
            }
        });

        // Actualizar contador
        contadorVisible.textContent = visibles;
    }

    // Evento input en el buscador
    buscador.addEventListener('input', filtrarProductos);

    // Inicializar contador al cargar
    filtrarProductos();
});