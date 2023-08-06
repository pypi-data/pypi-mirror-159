"""zdppy_password_hash.ext.django.models -- monkeypatch django hashing framework

this plugin monkeypatches django's hashing framework
so that it uses a zdppy_password_hash context object, allowing handling of arbitrary
hashes in Django databases.
"""
