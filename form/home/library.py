
# https://stackoverflow.com/questions/14647723/django-forms-if-not-valid-show-form-with-error-message
def get_form_errors(form) :

    retval = list()
    for field in form:
        message = ''
        for error in field.errors :
            if len(message) > 0 : message += ', '
            message += error

        if len(message) > 0 :
            row = {'name': field.name, 'label': field.label, 'message': message}
            retval.append(row)

    message = ''
    for error in form.non_field_errors() :
        if len(message) > 0 : message += ', '
        message += error

    if len(message) > 0 :
        row = {'name': '_general', 'label': 'General errors', 'message': message}
        retval.append(row)

    return retval
