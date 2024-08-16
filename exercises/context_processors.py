from .forms import ContactMessageForm

def contact_form_processor(request):
    return {'contact_form': ContactMessageForm()}
