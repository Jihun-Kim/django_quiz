from .models import Question

from django.shortcuts import render
from django.http import HttpResponse

def single_photo(request):
    return HttpResponse('3....3. ... .. .....')

def single_photo2(request, photo_id):
    try:
        q = Question.objects.get(pk=photo_id)
    except Question.DoesNotExist:
        return HttpResponse('no question.')

    response_text = '<p>{photo_id}....{photo_id}. ... .. .....</p>'
    response_text += '<p>{photo_url}</p>'
    response_text += '<p><img src="{photo_url}" /></p>'

    return HttpResponse(response_text.format(
            photo_id=photo_id,
            photo_url=q.figure.url
        )
    )
