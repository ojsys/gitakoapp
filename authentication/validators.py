from django.core.exceptions import ValidationError


class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'The password must contain a letter', code='password_no_letters'
            )
    def get_help_text(self):
        return 'The password must contain at least one Upper or Lower case letter'

# class ContainsNumberValidator:
#     def validate(self, password, user=None):
#         if not any(char.is_digit() for char in password):
#             raise ValidationError(
#                 'The password must contain at least one digit', code='password_no_numbers'
#             )
#     def get_help_text(self):
#         return 'The password must contain at least one Number'