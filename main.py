import flet as ft

def main(page: ft.Page):
    page.title = 'FARMI-UJAT'
    page.appbar = ft.AppBar(
        title=ft.Text('FARMI-UJAT', size= 50),
        center_title=True
    )
    btn_interacciones = ft.FilledButton(
        content= ft.Container(
            content = ft.Column(
                controls= [
                    ft.Icon('medication', size=40, color='black'),
                    ft.Text('Interacciones Medicamentosas', text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding= 10
        ),
        style= ft.ButtonStyle(
            shape= ft.RoundedRectangleBorder(radius=10),
            side= ft.BorderSide(1, 'orange')
        ),
        bgcolor= 'orange100',
        color='black',
        width=200
    )
    btn_alta = ft.FilledButton(
        content= ft.Container(
            content = ft.Column(
                controls= [
                    ft.Icon('add_box', size=40, color='black'),
                    ft.Text('Alta de Medicamentos', text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding= 10
        ),
        style= ft.ButtonStyle(
            shape= ft.RoundedRectangleBorder(radius=10),
            side= ft.BorderSide(1, 'orange')
        ),
        bgcolor= 'PURPLE100',
        color='black',
        width=200
    )
    btn_lista = ft.FilledButton(
        content= ft.Container(
            content = ft.Column(
                controls= [
                    ft.Icon('VIEW_LIST', size=40, color='black'),
                    ft.Text('Lista de Medicamentos', text_align=ft.TextAlign.CENTER)
                ],horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding= 10
        ),
        style= ft.ButtonStyle(
            shape= ft.RoundedRectangleBorder(radius=10),
            side= ft.BorderSide(1, '')
        ),
        bgcolor= 'INDIGO100',
        color='black',
        width=200
    )
    row_botones = ft.Row(
        controls=[btn_interacciones, btn_alta, btn_lista],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=40
    )



    page.add(ft.Divider(color='black'))
    page.add(row_botones)
    page.update()

ft.app(target= main, view=ft.AppView.WEB_BROWSER)