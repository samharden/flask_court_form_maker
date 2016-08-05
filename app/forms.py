from flask import flash, Markup
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class InputForm(Form):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    case_num = StringField('case_num', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    ## adds the variable for the email address input
    ##email_address = StringField('email_address', validators=[DataRequired()])

    # http://flask-wtf.readthedocs.io/en/latest/api.html#flask_wtf.Form.validate_on_submit
    # http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-unit-testing

###Old validate function:
#    def validate(self):
#        if not Form.validate(self):
#            #print "not form validate"
#            if self.first_name.data or \
#                    self.last_name.data or \
#                    self.case_num.data:
#                #print "Should return True"
#                return True
            #print "Should return False"
#            info = Markup('<h2 style="color:red"> Must enter at least one search term. </h2>')
#            flash(info)
#            return False
#        return True
###
### New Function:
    def validate(self):
        if not Form.validate(self):
            #print "not form validate"
            if "<" in self.first_name.data or \
                    "<" in self.last_name.data or \
                    "<" in self.case_num.data:
                #info = Markup("<h2 style='color:red'> Really? Try Harder. </h2>")
                #<img src="/static/500_error.jpg">
                info = Markup("<img src='/static/hackers.jpg'>")
                flash(info)
                return False
            elif self.first_name.data or \
                    self.last_name.data or \
                    self.case_num.data:
                #print "Should return True"
                return True
            #print "Should return False"
            info = Markup('<h2 style="color:red"> Must enter at least one search term. </h2>')
            flash(info)
            return False
        return True