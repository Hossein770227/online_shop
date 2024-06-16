

from django.contrib.auth.models import BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self,phone_number, full_name, password):
        if not phone_number:
            raise ValueError("user must have phone number")
        if not full_name:
            raise ValueError("user must have full name")
        user = self.model(phone_number=phone_number, full_name=full_name)
        user.set_password((password))
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, full_name, password):
        user = self.create_user(phone_number, full_name, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
