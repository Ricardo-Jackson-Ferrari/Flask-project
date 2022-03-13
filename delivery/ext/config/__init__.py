def init_app(app):
    app.config['SECRET_KEY'] = 'efrgbn*-5bob0fnm7jgf$51&da0*'

    if app.debug:
        app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True