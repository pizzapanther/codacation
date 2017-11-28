from rest_framework import serializers

from classroom.models import Assignment, Issue

class IssueSerializer(serializers.ModelSerializer):
  class Meta:
    model = Issue
    fields = ('id', 'num', 'merge_branch', 'student', 'modified', 'created')
    
class AssignmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Assignment
    fields = ('id', 'name', 'repo_url', 'klass', 'short_description', 'modified', 'created')
    