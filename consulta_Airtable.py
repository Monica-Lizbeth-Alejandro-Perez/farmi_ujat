import flet as ft
import nube as nb


def main(page: ft.Page):
    page.title = 'Recetas'
    page.theme_mode = 'light'
    page.scroll = True
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.FORMAT_LIST_BULLETED),
        title=ft.Column(
            [
                ft.Text("Recetas", size=18, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ft.Text("UJAT", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        center_title=True,
        bgcolor="blue",
        color="white"
    )

    # 🔹 Encabezado de la tabla
    encabezado = [
        ft.DataColumn(ft.Text('Medicamento')),
        ft.DataColumn(ft.Text('Interacciones'))
    ]

    filas = []  # Lista para almacenar las filas de la tabla
    
    # 🔹 Selecciona todos los medicamentos
    datos = nb.Receta.all()
    for d in datos:
        # Crear celdas con formato personalizado
        celda1 = ft.DataCell(ft.Text( d.medicamento  ))  # Descripción en negritas
        
        celda2 = ft.DataCell(ft.Container(ft.Text( d.interacciones ),width=200  # Presentación con ancho de 200
            )
        )


        fila = ft.DataRow([celda1, celda2])
        filas.append(fila)

    # 🔹 Crear la tabla con los datos
    tbl_medicamentos = ft.DataTable(
        columns=encabezado,
        rows=filas,
        expand=True  # Permite que la tabla crezca con la ventana
    )



    page.add(tbl_medicamentos)
    page.update()

if __name__=="__main__":
    ft.app(target=main)









