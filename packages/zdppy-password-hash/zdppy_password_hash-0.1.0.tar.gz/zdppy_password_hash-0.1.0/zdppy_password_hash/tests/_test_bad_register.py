"""helper for method in test_registry.py"""
from zdppy_password_hash.registry import register_crypt_handler
import zdppy_password_hash.utils.handlers as uh

class dummy_bad(uh.StaticHandler):
    name = "dummy_bad"

class alt_dummy_bad(uh.StaticHandler):
    name = "dummy_bad"

# NOTE: if zdppy_password_hash.tests is being run from symlink (e.g. via gaeunit),
#       this module may be imported a second time as test._test_bad_registry.
#       we don't want it to do anything in that case.
if __name__.startswith("zdppy_password_hash.tests"):
    register_crypt_handler(alt_dummy_bad)
