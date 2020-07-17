from django.db import models
from django.contrib.postgres.fields import ArrayField
from .user import User

# Creating the 'rules' for each of the project's necessary fields
class Game(models.Model):

  # Each of fields to run Sudoku
  cells = ArrayField(models.CharField(max_length=100, blank=True), default=list)
  over = models.BooleanField(default=False)
  # time = models.CharField(max_length=100, default='')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  owner = models.ForeignKey('User', related_name='games', on_delete=models.CASCADE)

  # Returns Game model as a string; easier for debugging
  def __str__(self):
    return self.pk

  # Returns Game model as an object with key value pairs
  def as_dict(self):
    return {
      'id': self.id,
      'cells': self.cells,
      'over': self.over,
      # 'time': self.time,
      'created_at': self.created_at,
      'updated_at': self.updated_at,
      'owner': self.owner
    }
