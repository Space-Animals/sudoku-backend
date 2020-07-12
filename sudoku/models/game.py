from django.db import models

# Creating the 'skeleton' of the project
class Game(models.Model):
  user = models.ForeignKey('User', on_delete=models.CASCADE)
  def fill(arr):
    for i in range(81):
      arr.append(None)

  # Da Fields
  cells = fill([])
  over = models.BooleanField()
  time = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.pk


  def as_dict(self):
    return {
      'id': self.id,
      'cells': self.cells,
      'over': self.over,
      'time': self.time,
      'created_at': self.created_at,
      'updated_at': self.updated_at,
      'user': self.user
    }
