from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class ContactForm(FlaskForm):
    name= StringField('Name',
    validators=[DataRequired()])

    email = StringField(
        'E-mail',
        [
            Email(message=('Not a valid email address.')),
            DataRequired()
        ]
    )

    subject= StringField('Subject',
    validators=[DataRequired()])

    message = TextAreaField(
        'Message',
        [
            DataRequired(),
            Length(5, 255,
            message=('Your message is too short.'))
        ]
    )

    submit = SubmitField('Send')