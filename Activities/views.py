from django.shortcuts import get_object_or_404, render
from .models import Lesson, UserActivity

def complete_lesson(request, lesson_id):
    # Retrieve the lesson object based on the lesson_id
    lesson = get_object_or_404(Lesson, pk=lesson_id)

    # Assume the user is authenticated and stored in the request.user attribute
    user = request.user

    # Create a UserActivity instance for the completed lesson
    UserActivity.objects.create(
        user=user,
        course=lesson.course,
        lesson=lesson,
        activity_type='Lesson Completion'
    )

    # Other logic related to completing the lesson (e.g., updating user progress)

    # Render a template or redirect the user to another page
    return render(request, 'lesson_completed.html', {'lesson': lesson})
