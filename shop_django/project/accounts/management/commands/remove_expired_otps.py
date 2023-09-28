from django.core.management import BaseCommand
from accounts.models import OtpCode
from datetime import datetime , timedelta
import pytz

class Command(BaseCommand):
    help = 'Remove All Expired Otp Code'
    def handle(self, *args, **options):
        expried_time = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=2)
        OtpCode.objects.filter(created__lt = expried_time).delete()
        self.stdout.write('All Expried Otp Code Removed.')
