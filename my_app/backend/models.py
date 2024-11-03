import datetime
import reflex as rx


class News(rx.Model, table=True):  # type: ignore

    organization: str
    title: str
    upload_date: datetime.datetime
    url: str
    body: str
