"""
zdppy_password_hash.utils.des - DEPRECATED LOCATION, WILL BE REMOVED IN 2.0

This has been moved to :mod:`zdppy_password_hash.crypto.des`.
"""
#=============================================================================
# import from new location
#=============================================================================
from warnings import warn
warn("the 'zdppy_password_hash.utils.des' module has been relocated to 'zdppy_password_hash.crypto.des' "
     "as of zdppy_password_hash 1.7, and the old location will be removed in zdppy_password_hash 2.0",
     DeprecationWarning)

#=============================================================================
# relocated functions
#=============================================================================
from zdppy_password_hash.utils.decor import deprecated_function
from zdppy_password_hash.crypto.des import expand_des_key, des_encrypt_block, des_encrypt_int_block

expand_des_key = deprecated_function(deprecated="1.7", removed="1.8",
    replacement="zdppy_password_hash.crypto.des.expand_des_key")(expand_des_key)

des_encrypt_block = deprecated_function(deprecated="1.7", removed="1.8",
    replacement="zdppy_password_hash.crypto.des.des_encrypt_block")(des_encrypt_block)

des_encrypt_int_block = deprecated_function(deprecated="1.7", removed="1.8",
    replacement="zdppy_password_hash.crypto.des.des_encrypt_int_block")(des_encrypt_int_block)

#=============================================================================
# deprecated functions -- not carried over to zdppy_password_hash.crypto.des
#=============================================================================
import struct
_unpack_uint64 = struct.Struct(">Q").unpack

@deprecated_function(deprecated="1.6", removed="1.8",
                     replacement="zdppy_password_hash.crypto.des.des_encrypt_int_block()")
def mdes_encrypt_int_block(key, input, salt=0, rounds=1): # pragma: no cover -- deprecated & unused
    if isinstance(key, bytes):
        if len(key) == 7:
            key = expand_des_key(key)
        key = _unpack_uint64(key)[0]
    return des_encrypt_int_block(key, input, salt, rounds)

#=============================================================================
# eof
#=============================================================================
