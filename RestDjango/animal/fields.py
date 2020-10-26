from django.core.validators import validate_email
from django.db import models
from django.core.exceptions import ValidationError
import re


def validate_phone_number(number):
    rule = re.compile(r'^(?:\+?44)?[07]\d{9,13}$')

    if not rule.search(number):
        msg = "Invalid mobile number."
        raise ValidationError(msg)
    return


class MultiContactField(models.TextField):
    separator = ','
    validator = None

    def to_python(self, value):
        if not value:
            return None
        cleaned_contact_list = []
        contact_list = filter(None, re.split(r';|,\s|\n', value))

        for contact in contact_list:
            if contact.strip(' @;,'):
                cleaned_contact_list.append(contact.strip(' @;,'))

        cleaned_contact_list = list(set(cleaned_contact_list))

        return self.separator.join(cleaned_contact_list)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)

        email_list = value.split(self.separator)

        for email in email_list:
            self.validator(email.strip())


class MultiEmailField(MultiContactField):
    validator = validate_email


class MultiPhoneNumberField(MultiContactField):
    validator = validate_phone_number
