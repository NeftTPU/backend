from ..models import Pool
import os
import subprocess

class PoolService:
    def getListForUser(self, user):
        return Pool.objects.filter(user=user).all()

    def getById(self, id):
        return Pool.objects.get(id=id)

    def store(self, data, user):

        model = Pool()

        model.user = user
        model.title = data['title']
        model.is_generated = False
        model.save()

        model.collections.add(*data.getlist('collection_ids[]'))

        subprocess.Popen(["python3", "manage.py", "generate_pool", str(model.id)])

        return model
