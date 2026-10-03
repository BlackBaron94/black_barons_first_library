def add_form_control(form):
    for field in form.visible_fields():
        field.field.widget.attrs['class'] = 'form-control'
    print("Done")

def get_abs(number):
    print("\n\nDoing stuff now\n\n")
    if number < 0:
        return -number
    return number