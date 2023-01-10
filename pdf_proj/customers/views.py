from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from .models import Customer

# Create your views here.
class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/main.html'

def customer_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    customer = get_object_or_404(Customer, pk=pk)

    template_path = 'customers/pdf2.html'
    context = {'customer': customer}
    # create a django response object
    response = HttpResponse(content_type='application/pdf')
    # if downlaod
    response['Content-Disposition']="attachment; filename='report.pdf'"
    # if open in browser
    response['Content-Disposition']="filename='report.pdf'"
    #find the template and render it
    template = get_template(template_path)
    html = template.render(context)

    #create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response
    )
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('we had some errors <pre>' + html + '</pre>')
    return response

def render_pdf_view(request):
    template_path = 'customers/pdf1.html'
    context = {'myvar': 'this is your template context'}
    # create a django response object
    response = HttpResponse(content_type='application/pdf')
    # if downlaod
    response['Content-Disposition']="attachment; filename='report.pdf'"
    # if open in browser
    response['Content-Disposition']="filename='report.pdf'"
    #find the template and render it
    template = get_template(template_path)
    html = template.render(context)

    #create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response
    )
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('we had some errors <pre>' + html + '</pre>')
    return response
