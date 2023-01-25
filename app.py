import json
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def redirectToFormulario():
    form = 'none'
    return redirect(url_for('formulario', form=form))

@app.route("/formulario2/<form>", methods=['GET', 'POST'])
def formulario2(form):
    if(form != 'none'):
        form = form.replace("\'", "\"")
        form = json.loads(form)
    return render_template('formulario2.html', form=form)

@app.route("/formulario", methods=['GET', 'POST'])
def formulario():
    request_method = request.method

    if(request_method == 'POST'):
        formData = {
           "produto1": request.form["produto1"],"quantidade1": request.form["quantidade1"],
            "produto2": request.form["produto2"],"quantidade2": request.form["quantidade2"],
            "produto3": request.form["produto3"], "quantidade3": request.form["quantidade3"]
        }
        return redirect(url_for('formulario2', form=formData))
    return render_template('formulario.html')

if __name__ == "__main__":
    app.run(debug=True)



