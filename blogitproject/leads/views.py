from django.shortcuts import render
from leads.models import Lead
from django.contrib import messages
from leads.forms import LeadForm
# Create your views here.


def contact_page(request):

    if request.method == 'POST':
        
        form = LeadForm(request.POST)
        if form.is_valid():
            new_lead = Lead()
            new_lead.name = request.POST.get('name', '')
            new_lead.subject = request.POST.get('subject', '')
            new_lead.email = request.POST.get('email', '')
            new_lead.message = request.POST.get('message', '')
            new_lead.save()

            messages.success(request, '{}, Your message was delivered!'.format(new_lead.name))
        else:
            messages.error(request, 'Something is going wrong! Try again')
    form = LeadForm()

    context = {
        'form': form
    }

    return render(request, 'leads/contact.html',context=context)
