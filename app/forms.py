from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequied, Lenght, Regexp

class ProductForm(FlaskForm):
    product_id = StringField(
        "Podaj kod produktu z serwisu Ceneo.pl: ",
        validators = [
            DataRequied("Musisz podać kod produktu!"),
            Lenght(min = 8, max = 8, "Kod produktu musi mieć dokładnie 8 znaków!"),
            Regexp("^[\d]+$", "Kod produktu musi zawierać wyłącznie cyfry!"),

        ]
    )
    submit = SubmitField("Pobierz")