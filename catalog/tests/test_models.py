from django.test import TestCase

# Create your tests here.

from catalog.models import Child


class OwnerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Child.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        child = Child.objects.get(id=1)
        field_label = child._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_last_name_label(self):
        child = Child.objects.get(id=1)
        field_label = child._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_date_of_birth_label(self):
        child = Child.objects.get(id=1)
        field_label = child._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date of birth')

    def test_date_of_death_label(self):
        child = Child.objects.get(id=1)
        field_label = child._meta.get_field('group').verbose_name
        self.assertEquals(field_label, 'died')

    def test_first_name_max_length(self):
        child = Child.objects.get(id=1)
        max_length = child._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_last_name_max_length(self):
        child = Child.objects.get(id=1)
        max_length = child._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        child = Child.objects.get(id=1)
        expected_object_name = '{0}, {1}'.format(child.last_name, child.first_name)

        self.assertEquals(expected_object_name, str(child))

    def test_get_absolute_url(self):
        child = Child.objects.get(id=1)
        self.assertEquals(child.get_absolute_url(), '/catalog/child/1')
