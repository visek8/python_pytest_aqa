from core.base_service import BaseService
from core.dog_url import ALL_BREDS, BREED_IMAGES


class DogService(BaseService):

    def get_all_dog(self):
        response = self.get(ALL_BREDS)
        all_breds = response['message']
        return list(all_breds.keys())

    def get_dog_image(self, breed):
        self.get(BREED_IMAGES(breed))
