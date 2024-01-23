from rest_framework import serializers
from .models import  Lesson, QuizOption, Quiz_Question
from rest_framework import generics
from master.serializers import (AdditionalResourceListSerializers, CourseMaterialListSerializers,
LessonAttachmentSerializer,LessonAssignmentSerializer,)
from coursedetail.models import Quiz_Question, QuizOption
from master.models import batch, CourseMaterial, AdditionalResource,LessonAttachment, LessonAssignment 
# from coursedetail.serializers import QuizOptionListSerializers, Quiz_QuestionListSerializers
class LessonListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class LessonDetailSerializer(serializers.ModelSerializer):
    attachment_lession_count = serializers.SerializerMethodField()
    assignment_lession_count = serializers.SerializerMethodField()
    attachment_lession = serializers.SerializerMethodField()
    assignment_lession = serializers.SerializerMethodField()
    quiz_questions = serializers.SerializerMethodField()
    quiz_options = serializers.SerializerMethodField()
    attachment_lession = LessonAttachmentSerializer(many=True, read_only=True)
    assignment_lession = LessonAssignmentSerializer(many=True, read_only=True)
    # quiz_questions_detail = Quiz_QuestionListSerializers(many=True, read_only=True)
    # quiz_options_detail = QuizOptionListSerializers(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'

    def get_attachment_lession(self, lesson):
        return LessonAttachment.objects.filter(lesson=lesson)

    def get_assignment_lession(self, lesson):
        return LessonAssignment.objects.filter(lesson=lesson)

    def get_assignment_lession_count(self, lesson):
        assignments = LessonAssignment.objects.filter(lesson=lesson)
        serialized_assignments = LessonAssignmentSerializer(assignments, many=True).data
        return {
            'count': len(serialized_assignments),
            'assignments': serialized_assignments
        }

    def get_attachment_lession_count(self, lesson):
        attachments = LessonAttachment.objects.filter(lesson=lesson)
        serialized_attachments = LessonAttachmentSerializer(attachments, many=True).data
        return {
            'count': len(serialized_attachments),
            'attachments': serialized_attachments
        }

    def get_quiz_questions(self, lesson):
        quiz_questions = Quiz_Question.objects.filter(lesson=lesson)
        return Quiz_QuestionListSerializers(quiz_questions, many=True).data

    def get_quiz_options(self, lesson):
        quiz_options = QuizOption.objects.filter(name__lesson=lesson)
        return QuizOptionListSerializers(quiz_options, many=True).data


    
class LessionRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    class Meta:
        model = Lesson
        fields = '__all__'


class QuizOptionListSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuizOption
        fields = '__all__'

    
class Quiz_QuestionListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz_Question
        fields = '__all__'



