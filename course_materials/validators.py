from rest_framework import serializers


class MaterialLinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        link_example = 'youtube.com'
        print(value)
        tmp_val = dict(value).get(self.field)
        if link_example not in tmp_val:
            raise serializers.ValidationError(
                "Разрешены ссылки только на youtube.com"
            )
