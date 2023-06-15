from services.dog_servise import DogService


def test_post():
    dog_service = DogService()
    all_dogs = dog_service.get_all_dog()
    dog_service.get_dog_image(all_dogs[0])
