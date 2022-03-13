from ..models import Collection


class CollectionService:
    def getAllForUser(self, user):
        return Collection.objects.filter(user=user).all()

    def store(self, data, user):
        return self.__update_model(Collection(), data, user)

    def update(self, id, data, user):
        model = self.__get_by_id(id)

        return self.__update_model(model, data, user)

    def delete(self, id):
        model = self.__get_by_id(id)
        model.delete()

    def __get_by_id(self, id):
        return Collection.objects.get(id=id)

    def __update_model(self, model, data, user):
        model.user = user
        model.title = data['title']
        model.height = data['height']
        model.save()

        return model
