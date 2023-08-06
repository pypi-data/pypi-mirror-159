from rest_framework.fields import DateTimeField


class ManipulationSerializerMixin:
    created_at: DateTimeField = DateTimeField(read_only=True)
    modified_at: DateTimeField = DateTimeField(read_only=True)

    class Meta:
        fields = [
            "created_at",
            "modified_at",
        ]
