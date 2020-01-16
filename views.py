@page.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated: #usuario actual
        return redirect(url_for('.Dashboard'))

    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        # print(form.username.data)
        # print(form.password.data)
        if (Functions.valida_user(form.username.data, form.password.data)):
            #
            # Como implementar la clase User para poder hacer uso de login_usr()??????
            #
            user = User()
            user.id = form.username.data
            login_user(user)
            flash('Usuario autenticado exitosamente')
            return redirect(url_for('.Dashboard'))
        else:
            flash('Usuario y/o clave errada', 'error')

    return render_template('auth/login.html', title='Login Portal BO', form=form,
                            active='login')
