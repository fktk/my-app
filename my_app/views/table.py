import reflex as rx
from ..backend.backend import State, Customer
from ..components.gender_badges import gender_badge


def _header_cell(text: str, icon: str):
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            align="center",
            spacing="2",
        ),
    )


def _show_customer(user: Customer):
    """Show a customer in a table row."""
    return rx.table.row(
        rx.table.row_header_cell(user.customer_name),
        rx.table.cell(user.email),
        rx.table.cell(user.age),
        rx.table.cell(
            rx.match(
                user.gender,
                ("Male", gender_badge("Male")),
                ("Female", gender_badge("Female")),
                ("Other", gender_badge("Other")),
                gender_badge("Other"),
            )
        ),
        rx.table.cell(user.location),
        rx.table.cell(user.job),
        rx.table.cell(user.salary),
        style={"_hover": {"bg": rx.color("accent", 2)}},
        align="center",
    )


def main_table():
    return rx.fragment(
        rx.flex(
            rx.color_mode.button(),
            rx.spacer(),
            rx.cond(
                State.sort_reverse,
                rx.icon(
                    "arrow-down-z-a",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=State.toggle_sort,
                ),
                rx.icon(
                    "arrow-down-a-z",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=State.toggle_sort,
                ),
            ),
            rx.select(
                [
                    "customer_name",
                    "email",
                    "age",
                    "gender",
                    "location",
                    "job",
                    "salary",
                ],
                placeholder="Sort By: Name",
                size="3",
                on_change=lambda sort_value: State.sort_values(sort_value),
            ),
            rx.input(
                rx.input.slot(rx.icon("search")),
                placeholder="Search here...",
                size="3",
                max_width="225px",
                width="100%",
                variant="surface",
                on_change=lambda value: State.filter_values(value),
            ),
            justify="end",
            align="center",
            spacing="3",
            wrap="wrap",
            width="100%",
            padding_bottom="1em",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell("Name", "square-user-round"),
                    _header_cell("Email", "mail"),
                    _header_cell("Age", "person-standing"),
                    _header_cell("Gender", "user-round"),
                    _header_cell("Location", "map-pinned"),
                    _header_cell("Job", "briefcase"),
                    _header_cell("Salary", "dollar-sign"),
                ),
            ),
            rx.table.body(rx.foreach(State.users, _show_customer)),
            variant="surface",
            size="3",
            width="100%",
        ),
    )
