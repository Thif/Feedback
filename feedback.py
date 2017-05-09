from flask import Flask, render_template, request, flash
from forms import ContactForm
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/', methods = ['GET', 'POST'])
def contact():
    print "ok"
    form = ContactForm()
   
    if request.method == 'POST':
        if form.validate() == False:
            flash_errors(form)
            return render_template('contact.html', form = form)
        else:
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO contact (project,supplier,communication,recommendation,plan,expertise,quality,deadline,overall,feedback,email) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(form.project.data,form.supplier.data,form.communication.data,form.recommendation.data,form.plan.data,form.expertise.data,form.quality.data,form.deadline.data,form.overall.data,form.feedback.data,form.email.data) )
            
                con.commit()
                flash("Record successfully added")
            return render_template('contact.html', form = form)
        
    elif request.method == 'GET':
         return render_template('contact.html', form = form)

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))
            
if __name__ == '__main__':
   app.run(debug = True)
