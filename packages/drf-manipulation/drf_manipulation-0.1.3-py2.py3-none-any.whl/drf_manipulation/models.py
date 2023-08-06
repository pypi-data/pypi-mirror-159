from django.db.models import DateTimeField, Model


class ManipulationAbstractModel(Model):
    created_at: DateTimeField = DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
    modified_at: DateTimeField = DateTimeField(
        auto_now=True,
        db_index=True,
    )

    class Meta:
        abstract = True
