import random

from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import Event, Track
import json

# Create your views here.


@csrf_exempt
def show(request):
    """
    View to return a list of events and tracks in JSON format.
    """

    events = Event.objects.all()
    returnList = []
    for event in events:
        returnList.append({
            'id': event.id,
            'title': event.title,
            'description': event.description,
            'start_time': event.start_time.isoformat(),
            'end_time': event.end_time.isoformat(),
            'created_at': event.created_at.isoformat(),
            'updated_at': event.updated_at.isoformat(),
            'track': event.track.id if event.track else None,
        })

    return JsonResponse(returnList, safe=False, )


@csrf_exempt
def create_event(request):
    """
    View to create a new event.
    """
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        title = body.get('title')
        description = body.get('description')
        start_time = body.get('start_time')
        end_time = body.get('end_time')

        event = Event(
            title=title,
            description=description,
            start_time=start_time,
            end_time=end_time
        )
        event.save()
        return JsonResponse({'status': 'success', 'event_id': event.id})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def update_event(request):
    """
    View to update an event.
    """
    if request.method == 'PATCH':
        event_id = request.PATCH.get('event_id')
        new_start_time = request.PATCH.get('new_start_time')
        new_end_time = request.PATCH.get('new_end_time')

        try:
            event = Event.objects.get(id=event_id)
            event.start_time = new_start_time
            event.end_time = new_end_time
            event.save()
            return JsonResponse({'status': 'success'})
        except Event.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Event not found'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def delete_event(request):
    """
    View to delete an event.
    """
    if request.method == 'DELETE':
        event_id = request.POST.get('event_id')

        try:
            event = Event.objects.get(id=event_id)
            event.delete()
            return JsonResponse({'status': 'success'})
        except Event.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Event not found'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def create_track(request):
    """
    View to create a new track.
    """
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        title = body.get('title')
        description = body.get('description')

        track = Track(
            title=title,
            description=description
        )
        track.save()
        return JsonResponse({'status': 'success', 'track_id': track.id})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def update_track(request):
    """
    View to update a track.
    """
    if request.method == 'PATCH':
        track_id = request.PATCH.get('track_id')
        new_title = request.PATCH.get('new_title')
        new_description = request.PATCH.get('new_description')

        try:
            track = Track.objects.get(id=track_id)
            track.title = new_title
            track.description = new_description
            track.save()
            return JsonResponse({'status': 'success'})
        except Track.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Track not found'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def delete_track(request):
    """
    View to delete a track.
    """
    if request.method == 'DELETE':
        track_id = request.POST.get('track_id')

        try:
            track = Track.objects.get(id=track_id)
            track.delete()
            return JsonResponse({'status': 'success'})
        except Track.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Track not found'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)