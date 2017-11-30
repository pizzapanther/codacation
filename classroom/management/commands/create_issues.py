import logging

from django.core.management.base import BaseCommand, CommandError
from classroom.tasks import create_issues

class Command (BaseCommand):
  help = 'Create Github Issues for Assignment'
  
  def add_arguments(self, parser):
    parser.add_argument('ass_id', nargs='+', type=int)

  def handle(self, *args, **options):
    root_logger = logging.getLogger('')
    root_logger.setLevel(logging.DEBUG)
    
    for ass_id in options['ass_id']:
      create_issues(ass_id)
