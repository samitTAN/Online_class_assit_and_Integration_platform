from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField,RadioField

from wtforms.validators import DataRequired, Email, EqualTo,email_validator

from wtforms import ValidationError

from models import User

class LoginForm(FlaskForm):
    email = StringField('電子郵件', validators=[DataRequired(),
    Email()])
    password = PasswordField('密碼',validators=[DataRequired()])
    submit = SubmitField('登入系統')

class RegistrationForm(FlaskForm):
    email = StringField('電子郵件', validators=[DataRequired(), Email()])
    username = StringField('使用者', validators=[DataRequired()])
    password = PasswordField('密碼', validators=[DataRequired(), EqualTo('pass_confirm', message='密碼需要吻合')])
    pass_confirm = PasswordField('確認密碼', validators=[DataRequired()])
    gender = RadioField('請輸入性別', choices=[('M','男生'),('F','女生')])
    submit = SubmitField('註冊')


def check_username(self, field):
    """檢查username"""
    if User.query.filter_by(username=field.data).first():
        raise ValidationError('使用者已存在')
