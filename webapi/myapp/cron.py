# for testing create tasks in the background in Django
from .models import Alert
def my_scheduled_job():
    Alert.objects.all(Alert_isTake=True)
