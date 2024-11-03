import reflex as rx
from .views.table import main_table
from .backend.backend import State


def index() -> rx.Component:
    return rx.container(
        main_table(),
        size='3',
        bg=rx.color("accent", 1),
    )


app = rx.App(
    theme=rx.theme(
        appearance="light", has_background=True, radius="large", accent_color="blue"
    ),
)
app.add_page(
    index,
    on_load=State.load_entries,
    title="Sales App",
    description="Generate personalized sales emails.",
)
