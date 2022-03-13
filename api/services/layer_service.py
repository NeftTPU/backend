from ..models import Layer


class LayerService:
    def store(self, data):
        return self.__update_model(Layer(), data)

    def update(self, id, data):
        return self.__update_model(self.__get_by_id(id), data)

    def delete(self, id):
        model = self.__get_by_id(id)
        model.delete()

    def __get_by_id(self, id):
        return Layer.objects.get(id=id)

    def __update_model(self, model: Layer, data):
        model.image_id = data['image_id']
        model.title = data['title']
        model.collection_id = data['collection_id']

        model.save()

        return model
