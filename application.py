from flask import Flask,render_template
FAI=Flask(__name__) #Flask(NAMe of the current Module)
@FAI.route('/dhoni')
def dhoni():
    return render_template('dhoni.html')

@FAI.route('/virat')
def virat():
    return render_template('virat.html')

if __name__=='__main__':
    FAI.run(debug=True) #to runserver