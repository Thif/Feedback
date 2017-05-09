from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField

from wtforms import validators, ValidationError

class ContactForm(Form):
   project = TextField("Project number",[validators.Required("Please enter the project number.")],default="")
   supplier = TextField("supplier",[validators.Required("Please enter a supplier")],default="")
   
   communication=SelectField("Test", choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),("TE","TE")], default=3)
   recommendation=SelectField("Test", choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),("TE","TE")], default=3)
   plan=SelectField("Test", choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),("TE","TE")], default=3)
   expertise=SelectField("Test", choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),("TE","TE")], default=3)
   quality=SelectField("Test", choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),("TE","TE")], default=3)
   deadline=SelectField("Test", choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),("TE","TE")], default=3)
   overall=SelectField("Test", choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),("TE","TE")], default=3)
   
   feedback = TextAreaField("feedback",[validators.Required("Please enter a feedback")])
   
   email = TextField("Email",[validators.Required("Please enter your email address."),
      validators.Email("Please enter a valid email address.")],default="")

   submit = SubmitField("Send")
