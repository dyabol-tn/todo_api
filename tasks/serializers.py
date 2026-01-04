from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(
        source='get_status_display',
        read_only=True,
        help_text='Человекочитаемое название статуса'
    )

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'title': {
                'error_messages': {
                    'blank': 'Заголовок не может быть пустым',
                    'max_length': 'Заголовок не должен превышать 200 символов'
                }
            },
            'status': {
                'help_text': 'Статус задачи: todo, in_progress или done'
            }
        }

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Заголовок не может состоять только из пробелов")
        return value

    def validate_status(self, value):
        valid_statuses = [choice[0] for choice in Task.STATUS_CHOICES]
        if value not in valid_statuses:
            raise serializers.ValidationError(
                f"Недопустимый статус. Допустимые значения: {', '.join(valid_statuses)}"
            )
        return value