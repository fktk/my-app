import reflex as rx
from sqlmodel import select, asc, desc, or_, func

from .models import Customer


class State(rx.State):
    """The app state."""

    current_user: Customer = Customer()
    users: list[Customer] = []
    products: dict[str, str] = {}
    email_content_data: str = "Click 'Generate Email' to generate a personalized sales email."
    gen_response = False
    tone: str = "😊 Formal"
    length: str = "1000"
    search_value: str = ""
    sort_value: str = ""
    sort_reverse: bool = False

    def load_entries(self) -> list[Customer]:
        """Get all users from the database."""
        with rx.session() as session:
            query = select(Customer)
            if self.search_value:
                search_value = f"%{str(self.search_value).lower()}%"
                query = query.where(
                    or_(
                        *[
                            getattr(Customer, field).ilike(search_value)
                            for field in Customer.get_fields()
                        ],
                    )
                )

            if self.sort_value:
                sort_column = getattr(Customer, self.sort_value)
                if self.sort_value == "salary":
                    order = desc(sort_column) if self.sort_reverse else asc(
                        sort_column)
                else:
                    order = desc(func.lower(sort_column)) if self.sort_reverse else asc(
                        func.lower(sort_column))
                query = query.order_by(order)

            self.users = session.exec(query).all()

    def sort_values(self, sort_value: str):
        self.sort_value = sort_value
        self.load_entries()

    def toggle_sort(self):
        self.sort_reverse = not self.sort_reverse
        self.load_entries()

    def filter_values(self, search_value):
        self.search_value = search_value
        self.load_entries()

    def get_user(self, user: Customer):
        self.current_user = user

    def add_customer_to_db(self, form_data: dict):
        self.current_user = form_data

        with rx.session() as session:
            if session.exec(
                select(Customer).where(
                    Customer.email == self.current_user["email"])
            ).first():
                return rx.window_alert("User with this email already exists")
            session.add(Customer(**self.current_user))
            session.commit()
        self.load_entries()
        return rx.toast.info(f"User {self.current_user['customer_name']} has been added.", position="bottom-right")

    def delete_customer(self, id: int):
        """Delete a customer from the database."""
        with rx.session() as session:
            customer = session.exec(
                select(Customer).where(Customer.id == id)).first()
            session.delete(customer)
            session.commit()
        self.load_entries()
        return rx.toast.info(f"User {customer.customer_name} has been deleted.", position="bottom-right")
