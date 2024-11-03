import reflex as rx
from sqlmodel import select, asc, desc, or_, func

from .models import News


class State(rx.State):
    """The app state."""

    news: list[News] = []
    search_value: str = ""
    sort_value: str = ""
    sort_reverse: bool = False

    def load_entries(self):
        """Get all news from the database."""
        with rx.session() as session:
            query = select(News)
            if self.search_value:
                search_value = f"%{str(self.search_value).lower()}%"
                query = query.where(
                    or_(
                        *[
                            getattr(News, field).ilike(search_value)
                            for field in News.get_fields()
                        ],
                    )
                )

            if self.sort_value:
                sort_column = getattr(News, self.sort_value)
                if self.sort_value == "salary":
                    order = desc(sort_column) if self.sort_reverse else asc(
                        sort_column)
                else:
                    order = desc(func.lower(sort_column)) if self.sort_reverse else asc(
                        func.lower(sort_column))
                query = query.order_by(order)

            self.news = list(session.exec(query).all())

    def sort_values(self, sort_value: str):
        self.sort_value = sort_value
        self.load_entries()

    def toggle_sort(self):
        self.sort_reverse = not self.sort_reverse
        self.load_entries()

    def filter_values(self, search_value):
        self.search_value = search_value
        self.load_entries()
