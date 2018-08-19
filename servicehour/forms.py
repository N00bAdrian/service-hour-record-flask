from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length
from flask_admin.form import DatePickerWidget

class InputForm(FlaskForm):
    applicant = StringField('Applicant', validators=[DataRequired()])
    hours = IntegerField('Hours', validators=[DataRequired(), NumberRange(min=1)])
    date = DateField('Date', format='%Y/%m/%d', widget=DatePickerWidget())
    sid = StringField('Docent', validators=[DataRequired(), Length(7,7)])
    submit = SubmitField('Submit')
