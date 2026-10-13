Hvilken oppgave er jeg på
Side 25, Nivå 1


Feilsøking
debugging
hvis jinja2.exceptions.TemplatesNotfound: index.htmk
skjekk: templates/index.html
hvis BadRequestKeyError
<!-- skjekk: request.form["navn"] -->
input name="name"
hvis css ikke funker skjekk static/css/style.css
og skjekk url for {{ url_for('static', filnename='css) }}
hvis endringer ikke vises skjekk, app.run(debug=True)
hvis port ikke vises app.run(debug=True, port=5001)