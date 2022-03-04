from idom import html, component, run


@component
def form():
    def handle_form(event):
        print(event)

    return html.form(
        {"onSubmit": handle_form},
        html.input({"name": "name"}),
        html.p("test"),
        html.button({"type": "submit", "value": "Submit"}, "Submit"),
        html.input({"lastname": "lastname"}),
        html.p("tes2t"),
    )


run(form)
