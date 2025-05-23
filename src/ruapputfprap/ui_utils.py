import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

def criar_layout_principal(app):
    """Cria e retorna o layout principal do aplicativo."""
    main_box = toga.Box(style=Pack(direction=COLUMN, margin=20))

    # Cabeçalho com data
    app.date_label = toga.Label(
        f"📅 {app.data_hoje.strftime('%d/%m/%Y')}",
        style=Pack(
            margin_bottom=15,
            font_size=16,
            font_weight="bold",
            text_align="center"
        )
    )

    # Seletor de Data
    def on_date_change(widget):
        app.set_data_hoje(widget.value)

    app.date_picker = toga.DateInput(
        on_change=on_date_change,
        style=Pack(margin_bottom=15)
    )
    app.date_picker.value = app.data_hoje

    # Área de exibição de conteúdo
    app.data_display = toga.MultilineTextInput(
        readonly=True,
        style=Pack(flex=1, margin=10)
    )

    # Barra de botões
    button_box = toga.Box(style=Pack(direction=ROW, margin_bottom=15))

    app.cardapio_button = toga.Button(
        "🍽️ Cardápio de Hoje",
        on_press=app._mostrar_cardapio,
        style=Pack(margin=10, flex=1)
    )

    app.notif_button = toga.Button(
        "🔔 Notificações",
        on_press=app._mostrar_notificacoes,
        style=Pack(margin=10, flex=1)
    )

    # Adiciona os botões
    button_box.add(app.cardapio_button)
    button_box.add(app.notif_button)

    # Montagem da interface
    main_box.add(app.date_label)
    main_box.add(app.date_picker)
    main_box.add(button_box)
    main_box.add(app.data_display)

    return main_box
