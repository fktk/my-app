import reflex as rx
from ..backend.backend import State, News
from ..components.gender_badges import gender_badge


def _show_navbar():
    return rx.flex(
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
            rx.spacer(),
            rx.color_mode.button(),
            justify="end",
            align="center",
            spacing="3",
            wrap="wrap",
            width="100%",
            padding_bottom="1em",
            )


def _show_card():
    return rx.card(
            rx.inset(
                rx.link(
                    rx.image(
                        src='https://www.kyoto-u.ac.jp/sites/default/files/styles/scale_crop_320x168/public/2024-10/2410_eye_enoto-e02c7055defc230bc171c12a1811a76f.webp?itok=FHl-Qtk4',
                        width='100%',
                        height='auto',
                        object_fit='cover',
                        ),
                    href='',
                    ),
                side='top',
                pb='current',
                href='',
                ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        '2024-11-01',
                        size='1',
                        as_='span',
                        ),
                    rx.spacer(),
                    rx.text(
                        '京都大学',
                        size='1',
                        as_='span',
                        ),
                    ),
                rx.hover_card.root(
                    rx.hover_card.trigger(
                        rx.heading(
                            '記事タイトル記事タイトル記事タイトル記事タイトル記事タイトル記事タイトル',
                            size='4',
                            as_='h2',
                            ),
                        ),
                    rx.hover_card.content(
                        rx.text("""
                        記事本文 記事本文 記事本文 記事本文 記事本文 記事本文 記事本文 記事本文 記事本文 記事本文 記事本文 記事本文 記事本文
                        記事本文 記事本文 記事本文 記事本文 記事本文 記事本文 記事本文 記事本文 記事本文 記事本文 記事本文 記事本文 記事本文
                        記事本文 記事本文 記事本文 記事本文 記事本文 記事本文 記事本文 記事本文 記事本文 記事本文 記事本文 記事本文 記事本文
                            """)
                        ),
                    ),
                rx.hstack(
                    rx.badge(
                        '材料',
                        variant='outline',
                        ),
                    rx.badge(
                        'データサイエンス',
                        variant='outline',
                        ),
                    spacing='1',
                    ),
                spacing='1'
                ),
            width='100%',
            # height='30vh',
            )

def main_table():
    return rx.box(
        _show_navbar(),
        rx.grid(
            rx.foreach(
                rx.Var.range(15),
                lambda _: _show_card(),
                ),
            columns=rx.breakpoints(
                initial='2',
                sm='3',
                ),
            spacing='3',
            width='100%',
            )
    )
