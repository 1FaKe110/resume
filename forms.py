from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, TextAreaField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Length, Regexp


# class OrderForm(FlaskForm):
#
#     name = StringField('ФИО', validators=[DataRequired()])
#     email = EmailField('Электронная почта', validators=[DataRequired()])
#     phone = StringField('Номер телефона',  default='+7', validators=[
#         DataRequired(),
#         Regexp(r'^\+7\s?[\(]{0,1}9[0-9]{2}[\)]{0,1}\s?\d{3}[-]{0,1}\d{2}[-]{0,1}\d{2}$',
#                message="Не верный формат телефонного номера"),
#         Length(min=11, max=12, message='Не верная длина номера телефона')
#     ])
#
#     product = SelectField('Выберите Продукт',
#                           choices=[
#                               ('site', 'Сайт'),
#                               ('chat-bot', 'Чат - бот'),
#                               ('infographic', 'Инфографика'),
#                               ('other', 'Другое'),
#                           ],
#                           validators=[DataRequired()])
#     feedback_method = SelectField('Способ связи',
#                                   choices=[
#                                       ('telegram', 'Telegram'),
#                                       ('email', 'Почта'),
#                                       ('whats-up', 'Whats-up'),
#                                       ('other', 'Другое (укажите в комментариях)'),
#                                   ],
#                                   validators=[DataRequired()])
#     comments = TextAreaField("Комментарии (не обязательно)")
#     submit = SubmitField("Отправить")