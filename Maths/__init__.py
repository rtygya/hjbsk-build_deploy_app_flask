from . import mathematics
from Maths.mathematics import summation, subtraction, multiplication

@app.route("/")
def render_index_page():
    return render_template('index.html')