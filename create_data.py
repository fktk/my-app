from my_app.backend.models import News
import reflex as rx


with rx.session() as session:
    session.add(
            News()
            )
    session.commit()
