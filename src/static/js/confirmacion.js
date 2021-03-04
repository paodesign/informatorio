function confirmarEliminacion(id) {
    swal({
        title: "¿Está seguro de Eliminar el post?",
        text: "No podras deshacer esta acción.",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    })
        .then((willDelete) => {
            if (willDelete) {
                //   swal("Tu post se ha eliminado!", {
                //     icon: "success",
                //   });
                window.location.href = "/eliminar/" + id + "/";
            } else {
                //   swal("Tu post esta a salvo.");
            }
        });

}

function confirmacionEditar(id) {
    swal({
        title: "Se guardo con Exito!",
        // text: "You clicked the button!",
        icon: "success",
        button: "Ok",
    })
    
}

