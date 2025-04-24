"""site_settings > utilities > pdf_export.py"""
# PYTHON IMPORTS
import logging
import tempfile
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

logger = logging.getLogger(__name__)


def render_pdf(request, template, context, file_name: str):
    html_string = render_to_string(
        template, context
    )
    html = HTML(
        string=html_string,
        base_url=request.build_absolute_uri()
    )
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = f"inline; filename={file_name}'.pdf"
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
    return response
