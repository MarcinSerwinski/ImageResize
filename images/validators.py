from rest_framework.exceptions import ValidationError


def validate_images_extension(upload):
    valid_formats = ['png', 'jpeg']
    if not any([True if upload.name.endswith(i) else False for i in valid_formats]):
        raise ValidationError(f'{upload.name} is not a valid image format. Only .png and .jpeg are accepted.')