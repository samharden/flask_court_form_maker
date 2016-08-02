from flask import render_template, flash, redirect, url_for, session, Markup
from app import app
from app import models as mdl
from .forms import InputForm

print "Top of Views"
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    print "Top of index"
    form = InputForm()
    if form.validate_on_submit():
        session['first_name'] = form.first_name._value()
        session['last_name'] = form.last_name._value()
        session['case_num'] = form.case_num._value()

#        flash('Will search for First Name: %s, Last Name: %s, \
#               Case Number: %s, remember_me= %s' %
#              (form.first_name._value(), form.last_name._value(),
#               form.case_num._value(), str(form.remember_me.data)))

        return redirect(url_for('results'))
    # Need a flash in validate function to write prompt that no
    # search was done so user knows something happened when index is
    # rendered a second time.

    return render_template('index.html',
                           title='Hillsborough County Court Date Search',
                           form=form)

@app.route('/results')
def results():
    df = mdl.search_all(session['first_name'].upper().replace(' ', ''),
                         session['last_name'].upper().replace(' ', ''),
                         session['case_num'].upper().replace(' ', '')
                        )

    #df = mdl.search_last(session['last_name'].replace(' ', ''))
    if len(df) < 1:
        print 'len(df) = ', len(df)
        info = Markup('<h2 style="color:red"> Sorry, but we didn\'t find any results for your search: <br> \
         First Name: %s, <br> \
         Last Name: %s, <br> \
         Case Number: %s. <br><br> \
         Make sure you entered the full first and last name or case number correctly.</h2>' %
                      (session['first_name'], session['last_name'], session['case_num'])
                      )
        flash(info)
        return redirect(url_for('index'))

    return render_template('results.html',
                           data=df.to_html(),
                           title='Hillsborough County Court Date Search',
                           )

# http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-unit-testing
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    #db.session.rollback()
    return render_template('500.html'), 500
