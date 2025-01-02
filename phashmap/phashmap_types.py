import numpy as np
import _phashmap as _phm
dict_types = {
    (np.dtype('u1'), np.dtype('u1')) : _phm.Dict_u1_u1,
    (np.dtype('u1'), np.dtype('u2')) : _phm.Dict_u1_u2,
    (np.dtype('u1'), np.dtype('u4')) : _phm.Dict_u1_u4,
    (np.dtype('u1'), np.dtype('u8')) : _phm.Dict_u1_u8,
    (np.dtype('u1'), np.dtype('i1')) : _phm.Dict_u1_i1,
    (np.dtype('u1'), np.dtype('i2')) : _phm.Dict_u1_i2,
    (np.dtype('u1'), np.dtype('i4')) : _phm.Dict_u1_i4,
    (np.dtype('u1'), np.dtype('i8')) : _phm.Dict_u1_i8,
    (np.dtype('u1'), np.dtype('f4')) : _phm.Dict_u1_f4,
    (np.dtype('u1'), np.dtype('f8')) : _phm.Dict_u1_f8,
    (np.dtype('u1'), np.dtype('S8')) : _phm.Dict_u1_S8,
    (np.dtype('u1'), np.dtype('S16')) : _phm.Dict_u1_S16,
    (np.dtype('u1'), np.dtype('S32')) : _phm.Dict_u1_S32,
    (np.dtype('u1'), np.dtype('S64')) : _phm.Dict_u1_S64,
    (np.dtype('u1'), np.dtype('S128')) : _phm.Dict_u1_S128,
    (np.dtype('u1'), np.dtype('S256')) : _phm.Dict_u1_S256,
    (np.dtype('u2'), np.dtype('u1')) : _phm.Dict_u2_u1,
    (np.dtype('u2'), np.dtype('u2')) : _phm.Dict_u2_u2,
    (np.dtype('u2'), np.dtype('u4')) : _phm.Dict_u2_u4,
    (np.dtype('u2'), np.dtype('u8')) : _phm.Dict_u2_u8,
    (np.dtype('u2'), np.dtype('i1')) : _phm.Dict_u2_i1,
    (np.dtype('u2'), np.dtype('i2')) : _phm.Dict_u2_i2,
    (np.dtype('u2'), np.dtype('i4')) : _phm.Dict_u2_i4,
    (np.dtype('u2'), np.dtype('i8')) : _phm.Dict_u2_i8,
    (np.dtype('u2'), np.dtype('f4')) : _phm.Dict_u2_f4,
    (np.dtype('u2'), np.dtype('f8')) : _phm.Dict_u2_f8,
    (np.dtype('u2'), np.dtype('S8')) : _phm.Dict_u2_S8,
    (np.dtype('u2'), np.dtype('S16')) : _phm.Dict_u2_S16,
    (np.dtype('u2'), np.dtype('S32')) : _phm.Dict_u2_S32,
    (np.dtype('u2'), np.dtype('S64')) : _phm.Dict_u2_S64,
    (np.dtype('u2'), np.dtype('S128')) : _phm.Dict_u2_S128,
    (np.dtype('u2'), np.dtype('S256')) : _phm.Dict_u2_S256,
    (np.dtype('u4'), np.dtype('u1')) : _phm.Dict_u4_u1,
    (np.dtype('u4'), np.dtype('u2')) : _phm.Dict_u4_u2,
    (np.dtype('u4'), np.dtype('u4')) : _phm.Dict_u4_u4,
    (np.dtype('u4'), np.dtype('u8')) : _phm.Dict_u4_u8,
    (np.dtype('u4'), np.dtype('i1')) : _phm.Dict_u4_i1,
    (np.dtype('u4'), np.dtype('i2')) : _phm.Dict_u4_i2,
    (np.dtype('u4'), np.dtype('i4')) : _phm.Dict_u4_i4,
    (np.dtype('u4'), np.dtype('i8')) : _phm.Dict_u4_i8,
    (np.dtype('u4'), np.dtype('f4')) : _phm.Dict_u4_f4,
    (np.dtype('u4'), np.dtype('f8')) : _phm.Dict_u4_f8,
    (np.dtype('u4'), np.dtype('S8')) : _phm.Dict_u4_S8,
    (np.dtype('u4'), np.dtype('S16')) : _phm.Dict_u4_S16,
    (np.dtype('u4'), np.dtype('S32')) : _phm.Dict_u4_S32,
    (np.dtype('u4'), np.dtype('S64')) : _phm.Dict_u4_S64,
    (np.dtype('u4'), np.dtype('S128')) : _phm.Dict_u4_S128,
    (np.dtype('u4'), np.dtype('S256')) : _phm.Dict_u4_S256,
    (np.dtype('u8'), np.dtype('u1')) : _phm.Dict_u8_u1,
    (np.dtype('u8'), np.dtype('u2')) : _phm.Dict_u8_u2,
    (np.dtype('u8'), np.dtype('u4')) : _phm.Dict_u8_u4,
    (np.dtype('u8'), np.dtype('u8')) : _phm.Dict_u8_u8,
    (np.dtype('u8'), np.dtype('i1')) : _phm.Dict_u8_i1,
    (np.dtype('u8'), np.dtype('i2')) : _phm.Dict_u8_i2,
    (np.dtype('u8'), np.dtype('i4')) : _phm.Dict_u8_i4,
    (np.dtype('u8'), np.dtype('i8')) : _phm.Dict_u8_i8,
    (np.dtype('u8'), np.dtype('f4')) : _phm.Dict_u8_f4,
    (np.dtype('u8'), np.dtype('f8')) : _phm.Dict_u8_f8,
    (np.dtype('u8'), np.dtype('S8')) : _phm.Dict_u8_S8,
    (np.dtype('u8'), np.dtype('S16')) : _phm.Dict_u8_S16,
    (np.dtype('u8'), np.dtype('S32')) : _phm.Dict_u8_S32,
    (np.dtype('u8'), np.dtype('S64')) : _phm.Dict_u8_S64,
    (np.dtype('u8'), np.dtype('S128')) : _phm.Dict_u8_S128,
    (np.dtype('u8'), np.dtype('S256')) : _phm.Dict_u8_S256,
    (np.dtype('i1'), np.dtype('u1')) : _phm.Dict_i1_u1,
    (np.dtype('i1'), np.dtype('u2')) : _phm.Dict_i1_u2,
    (np.dtype('i1'), np.dtype('u4')) : _phm.Dict_i1_u4,
    (np.dtype('i1'), np.dtype('u8')) : _phm.Dict_i1_u8,
    (np.dtype('i1'), np.dtype('i1')) : _phm.Dict_i1_i1,
    (np.dtype('i1'), np.dtype('i2')) : _phm.Dict_i1_i2,
    (np.dtype('i1'), np.dtype('i4')) : _phm.Dict_i1_i4,
    (np.dtype('i1'), np.dtype('i8')) : _phm.Dict_i1_i8,
    (np.dtype('i1'), np.dtype('f4')) : _phm.Dict_i1_f4,
    (np.dtype('i1'), np.dtype('f8')) : _phm.Dict_i1_f8,
    (np.dtype('i1'), np.dtype('S8')) : _phm.Dict_i1_S8,
    (np.dtype('i1'), np.dtype('S16')) : _phm.Dict_i1_S16,
    (np.dtype('i1'), np.dtype('S32')) : _phm.Dict_i1_S32,
    (np.dtype('i1'), np.dtype('S64')) : _phm.Dict_i1_S64,
    (np.dtype('i1'), np.dtype('S128')) : _phm.Dict_i1_S128,
    (np.dtype('i1'), np.dtype('S256')) : _phm.Dict_i1_S256,
    (np.dtype('i2'), np.dtype('u1')) : _phm.Dict_i2_u1,
    (np.dtype('i2'), np.dtype('u2')) : _phm.Dict_i2_u2,
    (np.dtype('i2'), np.dtype('u4')) : _phm.Dict_i2_u4,
    (np.dtype('i2'), np.dtype('u8')) : _phm.Dict_i2_u8,
    (np.dtype('i2'), np.dtype('i1')) : _phm.Dict_i2_i1,
    (np.dtype('i2'), np.dtype('i2')) : _phm.Dict_i2_i2,
    (np.dtype('i2'), np.dtype('i4')) : _phm.Dict_i2_i4,
    (np.dtype('i2'), np.dtype('i8')) : _phm.Dict_i2_i8,
    (np.dtype('i2'), np.dtype('f4')) : _phm.Dict_i2_f4,
    (np.dtype('i2'), np.dtype('f8')) : _phm.Dict_i2_f8,
    (np.dtype('i2'), np.dtype('S8')) : _phm.Dict_i2_S8,
    (np.dtype('i2'), np.dtype('S16')) : _phm.Dict_i2_S16,
    (np.dtype('i2'), np.dtype('S32')) : _phm.Dict_i2_S32,
    (np.dtype('i2'), np.dtype('S64')) : _phm.Dict_i2_S64,
    (np.dtype('i2'), np.dtype('S128')) : _phm.Dict_i2_S128,
    (np.dtype('i2'), np.dtype('S256')) : _phm.Dict_i2_S256,
    (np.dtype('i4'), np.dtype('u1')) : _phm.Dict_i4_u1,
    (np.dtype('i4'), np.dtype('u2')) : _phm.Dict_i4_u2,
    (np.dtype('i4'), np.dtype('u4')) : _phm.Dict_i4_u4,
    (np.dtype('i4'), np.dtype('u8')) : _phm.Dict_i4_u8,
    (np.dtype('i4'), np.dtype('i1')) : _phm.Dict_i4_i1,
    (np.dtype('i4'), np.dtype('i2')) : _phm.Dict_i4_i2,
    (np.dtype('i4'), np.dtype('i4')) : _phm.Dict_i4_i4,
    (np.dtype('i4'), np.dtype('i8')) : _phm.Dict_i4_i8,
    (np.dtype('i4'), np.dtype('f4')) : _phm.Dict_i4_f4,
    (np.dtype('i4'), np.dtype('f8')) : _phm.Dict_i4_f8,
    (np.dtype('i4'), np.dtype('S8')) : _phm.Dict_i4_S8,
    (np.dtype('i4'), np.dtype('S16')) : _phm.Dict_i4_S16,
    (np.dtype('i4'), np.dtype('S32')) : _phm.Dict_i4_S32,
    (np.dtype('i4'), np.dtype('S64')) : _phm.Dict_i4_S64,
    (np.dtype('i4'), np.dtype('S128')) : _phm.Dict_i4_S128,
    (np.dtype('i4'), np.dtype('S256')) : _phm.Dict_i4_S256,
    (np.dtype('i8'), np.dtype('u1')) : _phm.Dict_i8_u1,
    (np.dtype('i8'), np.dtype('u2')) : _phm.Dict_i8_u2,
    (np.dtype('i8'), np.dtype('u4')) : _phm.Dict_i8_u4,
    (np.dtype('i8'), np.dtype('u8')) : _phm.Dict_i8_u8,
    (np.dtype('i8'), np.dtype('i1')) : _phm.Dict_i8_i1,
    (np.dtype('i8'), np.dtype('i2')) : _phm.Dict_i8_i2,
    (np.dtype('i8'), np.dtype('i4')) : _phm.Dict_i8_i4,
    (np.dtype('i8'), np.dtype('i8')) : _phm.Dict_i8_i8,
    (np.dtype('i8'), np.dtype('f4')) : _phm.Dict_i8_f4,
    (np.dtype('i8'), np.dtype('f8')) : _phm.Dict_i8_f8,
    (np.dtype('i8'), np.dtype('S8')) : _phm.Dict_i8_S8,
    (np.dtype('i8'), np.dtype('S16')) : _phm.Dict_i8_S16,
    (np.dtype('i8'), np.dtype('S32')) : _phm.Dict_i8_S32,
    (np.dtype('i8'), np.dtype('S64')) : _phm.Dict_i8_S64,
    (np.dtype('i8'), np.dtype('S128')) : _phm.Dict_i8_S128,
    (np.dtype('i8'), np.dtype('S256')) : _phm.Dict_i8_S256,
    (np.dtype('f4'), np.dtype('u1')) : _phm.Dict_f4_u1,
    (np.dtype('f4'), np.dtype('u2')) : _phm.Dict_f4_u2,
    (np.dtype('f4'), np.dtype('u4')) : _phm.Dict_f4_u4,
    (np.dtype('f4'), np.dtype('u8')) : _phm.Dict_f4_u8,
    (np.dtype('f4'), np.dtype('i1')) : _phm.Dict_f4_i1,
    (np.dtype('f4'), np.dtype('i2')) : _phm.Dict_f4_i2,
    (np.dtype('f4'), np.dtype('i4')) : _phm.Dict_f4_i4,
    (np.dtype('f4'), np.dtype('i8')) : _phm.Dict_f4_i8,
    (np.dtype('f4'), np.dtype('f4')) : _phm.Dict_f4_f4,
    (np.dtype('f4'), np.dtype('f8')) : _phm.Dict_f4_f8,
    (np.dtype('f4'), np.dtype('S8')) : _phm.Dict_f4_S8,
    (np.dtype('f4'), np.dtype('S16')) : _phm.Dict_f4_S16,
    (np.dtype('f4'), np.dtype('S32')) : _phm.Dict_f4_S32,
    (np.dtype('f4'), np.dtype('S64')) : _phm.Dict_f4_S64,
    (np.dtype('f4'), np.dtype('S128')) : _phm.Dict_f4_S128,
    (np.dtype('f4'), np.dtype('S256')) : _phm.Dict_f4_S256,
    (np.dtype('f8'), np.dtype('u1')) : _phm.Dict_f8_u1,
    (np.dtype('f8'), np.dtype('u2')) : _phm.Dict_f8_u2,
    (np.dtype('f8'), np.dtype('u4')) : _phm.Dict_f8_u4,
    (np.dtype('f8'), np.dtype('u8')) : _phm.Dict_f8_u8,
    (np.dtype('f8'), np.dtype('i1')) : _phm.Dict_f8_i1,
    (np.dtype('f8'), np.dtype('i2')) : _phm.Dict_f8_i2,
    (np.dtype('f8'), np.dtype('i4')) : _phm.Dict_f8_i4,
    (np.dtype('f8'), np.dtype('i8')) : _phm.Dict_f8_i8,
    (np.dtype('f8'), np.dtype('f4')) : _phm.Dict_f8_f4,
    (np.dtype('f8'), np.dtype('f8')) : _phm.Dict_f8_f8,
    (np.dtype('f8'), np.dtype('S8')) : _phm.Dict_f8_S8,
    (np.dtype('f8'), np.dtype('S16')) : _phm.Dict_f8_S16,
    (np.dtype('f8'), np.dtype('S32')) : _phm.Dict_f8_S32,
    (np.dtype('f8'), np.dtype('S64')) : _phm.Dict_f8_S64,
    (np.dtype('f8'), np.dtype('S128')) : _phm.Dict_f8_S128,
    (np.dtype('f8'), np.dtype('S256')) : _phm.Dict_f8_S256,
    (np.dtype('S8'), np.dtype('u1')) : _phm.Dict_S8_u1,
    (np.dtype('S8'), np.dtype('u2')) : _phm.Dict_S8_u2,
    (np.dtype('S8'), np.dtype('u4')) : _phm.Dict_S8_u4,
    (np.dtype('S8'), np.dtype('u8')) : _phm.Dict_S8_u8,
    (np.dtype('S8'), np.dtype('i1')) : _phm.Dict_S8_i1,
    (np.dtype('S8'), np.dtype('i2')) : _phm.Dict_S8_i2,
    (np.dtype('S8'), np.dtype('i4')) : _phm.Dict_S8_i4,
    (np.dtype('S8'), np.dtype('i8')) : _phm.Dict_S8_i8,
    (np.dtype('S8'), np.dtype('f4')) : _phm.Dict_S8_f4,
    (np.dtype('S8'), np.dtype('f8')) : _phm.Dict_S8_f8,
    (np.dtype('S8'), np.dtype('S8')) : _phm.Dict_S8_S8,
    (np.dtype('S8'), np.dtype('S16')) : _phm.Dict_S8_S16,
    (np.dtype('S8'), np.dtype('S32')) : _phm.Dict_S8_S32,
    (np.dtype('S8'), np.dtype('S64')) : _phm.Dict_S8_S64,
    (np.dtype('S8'), np.dtype('S128')) : _phm.Dict_S8_S128,
    (np.dtype('S8'), np.dtype('S256')) : _phm.Dict_S8_S256,
    (np.dtype('S16'), np.dtype('u1')) : _phm.Dict_S16_u1,
    (np.dtype('S16'), np.dtype('u2')) : _phm.Dict_S16_u2,
    (np.dtype('S16'), np.dtype('u4')) : _phm.Dict_S16_u4,
    (np.dtype('S16'), np.dtype('u8')) : _phm.Dict_S16_u8,
    (np.dtype('S16'), np.dtype('i1')) : _phm.Dict_S16_i1,
    (np.dtype('S16'), np.dtype('i2')) : _phm.Dict_S16_i2,
    (np.dtype('S16'), np.dtype('i4')) : _phm.Dict_S16_i4,
    (np.dtype('S16'), np.dtype('i8')) : _phm.Dict_S16_i8,
    (np.dtype('S16'), np.dtype('f4')) : _phm.Dict_S16_f4,
    (np.dtype('S16'), np.dtype('f8')) : _phm.Dict_S16_f8,
    (np.dtype('S16'), np.dtype('S8')) : _phm.Dict_S16_S8,
    (np.dtype('S16'), np.dtype('S16')) : _phm.Dict_S16_S16,
    (np.dtype('S16'), np.dtype('S32')) : _phm.Dict_S16_S32,
    (np.dtype('S16'), np.dtype('S64')) : _phm.Dict_S16_S64,
    (np.dtype('S16'), np.dtype('S128')) : _phm.Dict_S16_S128,
    (np.dtype('S16'), np.dtype('S256')) : _phm.Dict_S16_S256,
    (np.dtype('S32'), np.dtype('u1')) : _phm.Dict_S32_u1,
    (np.dtype('S32'), np.dtype('u2')) : _phm.Dict_S32_u2,
    (np.dtype('S32'), np.dtype('u4')) : _phm.Dict_S32_u4,
    (np.dtype('S32'), np.dtype('u8')) : _phm.Dict_S32_u8,
    (np.dtype('S32'), np.dtype('i1')) : _phm.Dict_S32_i1,
    (np.dtype('S32'), np.dtype('i2')) : _phm.Dict_S32_i2,
    (np.dtype('S32'), np.dtype('i4')) : _phm.Dict_S32_i4,
    (np.dtype('S32'), np.dtype('i8')) : _phm.Dict_S32_i8,
    (np.dtype('S32'), np.dtype('f4')) : _phm.Dict_S32_f4,
    (np.dtype('S32'), np.dtype('f8')) : _phm.Dict_S32_f8,
    (np.dtype('S32'), np.dtype('S8')) : _phm.Dict_S32_S8,
    (np.dtype('S32'), np.dtype('S16')) : _phm.Dict_S32_S16,
    (np.dtype('S32'), np.dtype('S32')) : _phm.Dict_S32_S32,
    (np.dtype('S32'), np.dtype('S64')) : _phm.Dict_S32_S64,
    (np.dtype('S32'), np.dtype('S128')) : _phm.Dict_S32_S128,
    (np.dtype('S32'), np.dtype('S256')) : _phm.Dict_S32_S256,
    (np.dtype('S64'), np.dtype('u1')) : _phm.Dict_S64_u1,
    (np.dtype('S64'), np.dtype('u2')) : _phm.Dict_S64_u2,
    (np.dtype('S64'), np.dtype('u4')) : _phm.Dict_S64_u4,
    (np.dtype('S64'), np.dtype('u8')) : _phm.Dict_S64_u8,
    (np.dtype('S64'), np.dtype('i1')) : _phm.Dict_S64_i1,
    (np.dtype('S64'), np.dtype('i2')) : _phm.Dict_S64_i2,
    (np.dtype('S64'), np.dtype('i4')) : _phm.Dict_S64_i4,
    (np.dtype('S64'), np.dtype('i8')) : _phm.Dict_S64_i8,
    (np.dtype('S64'), np.dtype('f4')) : _phm.Dict_S64_f4,
    (np.dtype('S64'), np.dtype('f8')) : _phm.Dict_S64_f8,
    (np.dtype('S64'), np.dtype('S8')) : _phm.Dict_S64_S8,
    (np.dtype('S64'), np.dtype('S16')) : _phm.Dict_S64_S16,
    (np.dtype('S64'), np.dtype('S32')) : _phm.Dict_S64_S32,
    (np.dtype('S64'), np.dtype('S64')) : _phm.Dict_S64_S64,
    (np.dtype('S64'), np.dtype('S128')) : _phm.Dict_S64_S128,
    (np.dtype('S64'), np.dtype('S256')) : _phm.Dict_S64_S256,
    (np.dtype('S128'), np.dtype('u1')) : _phm.Dict_S128_u1,
    (np.dtype('S128'), np.dtype('u2')) : _phm.Dict_S128_u2,
    (np.dtype('S128'), np.dtype('u4')) : _phm.Dict_S128_u4,
    (np.dtype('S128'), np.dtype('u8')) : _phm.Dict_S128_u8,
    (np.dtype('S128'), np.dtype('i1')) : _phm.Dict_S128_i1,
    (np.dtype('S128'), np.dtype('i2')) : _phm.Dict_S128_i2,
    (np.dtype('S128'), np.dtype('i4')) : _phm.Dict_S128_i4,
    (np.dtype('S128'), np.dtype('i8')) : _phm.Dict_S128_i8,
    (np.dtype('S128'), np.dtype('f4')) : _phm.Dict_S128_f4,
    (np.dtype('S128'), np.dtype('f8')) : _phm.Dict_S128_f8,
    (np.dtype('S128'), np.dtype('S8')) : _phm.Dict_S128_S8,
    (np.dtype('S128'), np.dtype('S16')) : _phm.Dict_S128_S16,
    (np.dtype('S128'), np.dtype('S32')) : _phm.Dict_S128_S32,
    (np.dtype('S128'), np.dtype('S64')) : _phm.Dict_S128_S64,
    (np.dtype('S128'), np.dtype('S128')) : _phm.Dict_S128_S128,
    (np.dtype('S128'), np.dtype('S256')) : _phm.Dict_S128_S256,
    (np.dtype('S256'), np.dtype('u1')) : _phm.Dict_S256_u1,
    (np.dtype('S256'), np.dtype('u2')) : _phm.Dict_S256_u2,
    (np.dtype('S256'), np.dtype('u4')) : _phm.Dict_S256_u4,
    (np.dtype('S256'), np.dtype('u8')) : _phm.Dict_S256_u8,
    (np.dtype('S256'), np.dtype('i1')) : _phm.Dict_S256_i1,
    (np.dtype('S256'), np.dtype('i2')) : _phm.Dict_S256_i2,
    (np.dtype('S256'), np.dtype('i4')) : _phm.Dict_S256_i4,
    (np.dtype('S256'), np.dtype('i8')) : _phm.Dict_S256_i8,
    (np.dtype('S256'), np.dtype('f4')) : _phm.Dict_S256_f4,
    (np.dtype('S256'), np.dtype('f8')) : _phm.Dict_S256_f8,
    (np.dtype('S256'), np.dtype('S8')) : _phm.Dict_S256_S8,
    (np.dtype('S256'), np.dtype('S16')) : _phm.Dict_S256_S16,
    (np.dtype('S256'), np.dtype('S32')) : _phm.Dict_S256_S32,
    (np.dtype('S256'), np.dtype('S64')) : _phm.Dict_S256_S64,
    (np.dtype('S256'), np.dtype('S128')) : _phm.Dict_S256_S128,
    (np.dtype('S256'), np.dtype('S256')) : _phm.Dict_S256_S256,
}


set_types = {
    np.dtype('u1') : _phm.Set_u1,
    np.dtype('u2') : _phm.Set_u2,
    np.dtype('u4') : _phm.Set_u4,
    np.dtype('u8') : _phm.Set_u8,
    np.dtype('i1') : _phm.Set_i1,
    np.dtype('i2') : _phm.Set_i2,
    np.dtype('i4') : _phm.Set_i4,
    np.dtype('i8') : _phm.Set_i8,
    np.dtype('f4') : _phm.Set_f4,
    np.dtype('f8') : _phm.Set_f8,
    np.dtype('S8') : _phm.Set_S8,
    np.dtype('S16') : _phm.Set_S16,
    np.dtype('S32') : _phm.Set_S32,
    np.dtype('S64') : _phm.Set_S64,
    np.dtype('S128') : _phm.Set_S128,
    np.dtype('S256') : _phm.Set_S256,
}

multidict_types = {
    (np.dtype('u1'), np.dtype('u1')) : _phm.MultiDict_u1_u1,
    (np.dtype('u1'), np.dtype('u2')) : _phm.MultiDict_u1_u2,
    (np.dtype('u1'), np.dtype('u4')) : _phm.MultiDict_u1_u4,
    (np.dtype('u1'), np.dtype('u8')) : _phm.MultiDict_u1_u8,
    (np.dtype('u1'), np.dtype('i1')) : _phm.MultiDict_u1_i1,
    (np.dtype('u1'), np.dtype('i2')) : _phm.MultiDict_u1_i2,
    (np.dtype('u1'), np.dtype('i4')) : _phm.MultiDict_u1_i4,
    (np.dtype('u1'), np.dtype('i8')) : _phm.MultiDict_u1_i8,
    (np.dtype('u1'), np.dtype('f4')) : _phm.MultiDict_u1_f4,
    (np.dtype('u1'), np.dtype('f8')) : _phm.MultiDict_u1_f8,
    (np.dtype('u1'), np.dtype('S8')) : _phm.MultiDict_u1_S8,
    (np.dtype('u1'), np.dtype('S16')) : _phm.MultiDict_u1_S16,
    (np.dtype('u1'), np.dtype('S32')) : _phm.MultiDict_u1_S32,
    (np.dtype('u1'), np.dtype('S64')) : _phm.MultiDict_u1_S64,
    (np.dtype('u1'), np.dtype('S128')) : _phm.MultiDict_u1_S128,
    (np.dtype('u1'), np.dtype('S256')) : _phm.MultiDict_u1_S256,
    (np.dtype('u2'), np.dtype('u1')) : _phm.MultiDict_u2_u1,
    (np.dtype('u2'), np.dtype('u2')) : _phm.MultiDict_u2_u2,
    (np.dtype('u2'), np.dtype('u4')) : _phm.MultiDict_u2_u4,
    (np.dtype('u2'), np.dtype('u8')) : _phm.MultiDict_u2_u8,
    (np.dtype('u2'), np.dtype('i1')) : _phm.MultiDict_u2_i1,
    (np.dtype('u2'), np.dtype('i2')) : _phm.MultiDict_u2_i2,
    (np.dtype('u2'), np.dtype('i4')) : _phm.MultiDict_u2_i4,
    (np.dtype('u2'), np.dtype('i8')) : _phm.MultiDict_u2_i8,
    (np.dtype('u2'), np.dtype('f4')) : _phm.MultiDict_u2_f4,
    (np.dtype('u2'), np.dtype('f8')) : _phm.MultiDict_u2_f8,
    (np.dtype('u2'), np.dtype('S8')) : _phm.MultiDict_u2_S8,
    (np.dtype('u2'), np.dtype('S16')) : _phm.MultiDict_u2_S16,
    (np.dtype('u2'), np.dtype('S32')) : _phm.MultiDict_u2_S32,
    (np.dtype('u2'), np.dtype('S64')) : _phm.MultiDict_u2_S64,
    (np.dtype('u2'), np.dtype('S128')) : _phm.MultiDict_u2_S128,
    (np.dtype('u2'), np.dtype('S256')) : _phm.MultiDict_u2_S256,
    (np.dtype('u4'), np.dtype('u1')) : _phm.MultiDict_u4_u1,
    (np.dtype('u4'), np.dtype('u2')) : _phm.MultiDict_u4_u2,
    (np.dtype('u4'), np.dtype('u4')) : _phm.MultiDict_u4_u4,
    (np.dtype('u4'), np.dtype('u8')) : _phm.MultiDict_u4_u8,
    (np.dtype('u4'), np.dtype('i1')) : _phm.MultiDict_u4_i1,
    (np.dtype('u4'), np.dtype('i2')) : _phm.MultiDict_u4_i2,
    (np.dtype('u4'), np.dtype('i4')) : _phm.MultiDict_u4_i4,
    (np.dtype('u4'), np.dtype('i8')) : _phm.MultiDict_u4_i8,
    (np.dtype('u4'), np.dtype('f4')) : _phm.MultiDict_u4_f4,
    (np.dtype('u4'), np.dtype('f8')) : _phm.MultiDict_u4_f8,
    (np.dtype('u4'), np.dtype('S8')) : _phm.MultiDict_u4_S8,
    (np.dtype('u4'), np.dtype('S16')) : _phm.MultiDict_u4_S16,
    (np.dtype('u4'), np.dtype('S32')) : _phm.MultiDict_u4_S32,
    (np.dtype('u4'), np.dtype('S64')) : _phm.MultiDict_u4_S64,
    (np.dtype('u4'), np.dtype('S128')) : _phm.MultiDict_u4_S128,
    (np.dtype('u4'), np.dtype('S256')) : _phm.MultiDict_u4_S256,
    (np.dtype('u8'), np.dtype('u1')) : _phm.MultiDict_u8_u1,
    (np.dtype('u8'), np.dtype('u2')) : _phm.MultiDict_u8_u2,
    (np.dtype('u8'), np.dtype('u4')) : _phm.MultiDict_u8_u4,
    (np.dtype('u8'), np.dtype('u8')) : _phm.MultiDict_u8_u8,
    (np.dtype('u8'), np.dtype('i1')) : _phm.MultiDict_u8_i1,
    (np.dtype('u8'), np.dtype('i2')) : _phm.MultiDict_u8_i2,
    (np.dtype('u8'), np.dtype('i4')) : _phm.MultiDict_u8_i4,
    (np.dtype('u8'), np.dtype('i8')) : _phm.MultiDict_u8_i8,
    (np.dtype('u8'), np.dtype('f4')) : _phm.MultiDict_u8_f4,
    (np.dtype('u8'), np.dtype('f8')) : _phm.MultiDict_u8_f8,
    (np.dtype('u8'), np.dtype('S8')) : _phm.MultiDict_u8_S8,
    (np.dtype('u8'), np.dtype('S16')) : _phm.MultiDict_u8_S16,
    (np.dtype('u8'), np.dtype('S32')) : _phm.MultiDict_u8_S32,
    (np.dtype('u8'), np.dtype('S64')) : _phm.MultiDict_u8_S64,
    (np.dtype('u8'), np.dtype('S128')) : _phm.MultiDict_u8_S128,
    (np.dtype('u8'), np.dtype('S256')) : _phm.MultiDict_u8_S256,
    (np.dtype('i1'), np.dtype('u1')) : _phm.MultiDict_i1_u1,
    (np.dtype('i1'), np.dtype('u2')) : _phm.MultiDict_i1_u2,
    (np.dtype('i1'), np.dtype('u4')) : _phm.MultiDict_i1_u4,
    (np.dtype('i1'), np.dtype('u8')) : _phm.MultiDict_i1_u8,
    (np.dtype('i1'), np.dtype('i1')) : _phm.MultiDict_i1_i1,
    (np.dtype('i1'), np.dtype('i2')) : _phm.MultiDict_i1_i2,
    (np.dtype('i1'), np.dtype('i4')) : _phm.MultiDict_i1_i4,
    (np.dtype('i1'), np.dtype('i8')) : _phm.MultiDict_i1_i8,
    (np.dtype('i1'), np.dtype('f4')) : _phm.MultiDict_i1_f4,
    (np.dtype('i1'), np.dtype('f8')) : _phm.MultiDict_i1_f8,
    (np.dtype('i1'), np.dtype('S8')) : _phm.MultiDict_i1_S8,
    (np.dtype('i1'), np.dtype('S16')) : _phm.MultiDict_i1_S16,
    (np.dtype('i1'), np.dtype('S32')) : _phm.MultiDict_i1_S32,
    (np.dtype('i1'), np.dtype('S64')) : _phm.MultiDict_i1_S64,
    (np.dtype('i1'), np.dtype('S128')) : _phm.MultiDict_i1_S128,
    (np.dtype('i1'), np.dtype('S256')) : _phm.MultiDict_i1_S256,
    (np.dtype('i2'), np.dtype('u1')) : _phm.MultiDict_i2_u1,
    (np.dtype('i2'), np.dtype('u2')) : _phm.MultiDict_i2_u2,
    (np.dtype('i2'), np.dtype('u4')) : _phm.MultiDict_i2_u4,
    (np.dtype('i2'), np.dtype('u8')) : _phm.MultiDict_i2_u8,
    (np.dtype('i2'), np.dtype('i1')) : _phm.MultiDict_i2_i1,
    (np.dtype('i2'), np.dtype('i2')) : _phm.MultiDict_i2_i2,
    (np.dtype('i2'), np.dtype('i4')) : _phm.MultiDict_i2_i4,
    (np.dtype('i2'), np.dtype('i8')) : _phm.MultiDict_i2_i8,
    (np.dtype('i2'), np.dtype('f4')) : _phm.MultiDict_i2_f4,
    (np.dtype('i2'), np.dtype('f8')) : _phm.MultiDict_i2_f8,
    (np.dtype('i2'), np.dtype('S8')) : _phm.MultiDict_i2_S8,
    (np.dtype('i2'), np.dtype('S16')) : _phm.MultiDict_i2_S16,
    (np.dtype('i2'), np.dtype('S32')) : _phm.MultiDict_i2_S32,
    (np.dtype('i2'), np.dtype('S64')) : _phm.MultiDict_i2_S64,
    (np.dtype('i2'), np.dtype('S128')) : _phm.MultiDict_i2_S128,
    (np.dtype('i2'), np.dtype('S256')) : _phm.MultiDict_i2_S256,
    (np.dtype('i4'), np.dtype('u1')) : _phm.MultiDict_i4_u1,
    (np.dtype('i4'), np.dtype('u2')) : _phm.MultiDict_i4_u2,
    (np.dtype('i4'), np.dtype('u4')) : _phm.MultiDict_i4_u4,
    (np.dtype('i4'), np.dtype('u8')) : _phm.MultiDict_i4_u8,
    (np.dtype('i4'), np.dtype('i1')) : _phm.MultiDict_i4_i1,
    (np.dtype('i4'), np.dtype('i2')) : _phm.MultiDict_i4_i2,
    (np.dtype('i4'), np.dtype('i4')) : _phm.MultiDict_i4_i4,
    (np.dtype('i4'), np.dtype('i8')) : _phm.MultiDict_i4_i8,
    (np.dtype('i4'), np.dtype('f4')) : _phm.MultiDict_i4_f4,
    (np.dtype('i4'), np.dtype('f8')) : _phm.MultiDict_i4_f8,
    (np.dtype('i4'), np.dtype('S8')) : _phm.MultiDict_i4_S8,
    (np.dtype('i4'), np.dtype('S16')) : _phm.MultiDict_i4_S16,
    (np.dtype('i4'), np.dtype('S32')) : _phm.MultiDict_i4_S32,
    (np.dtype('i4'), np.dtype('S64')) : _phm.MultiDict_i4_S64,
    (np.dtype('i4'), np.dtype('S128')) : _phm.MultiDict_i4_S128,
    (np.dtype('i4'), np.dtype('S256')) : _phm.MultiDict_i4_S256,
    (np.dtype('i8'), np.dtype('u1')) : _phm.MultiDict_i8_u1,
    (np.dtype('i8'), np.dtype('u2')) : _phm.MultiDict_i8_u2,
    (np.dtype('i8'), np.dtype('u4')) : _phm.MultiDict_i8_u4,
    (np.dtype('i8'), np.dtype('u8')) : _phm.MultiDict_i8_u8,
    (np.dtype('i8'), np.dtype('i1')) : _phm.MultiDict_i8_i1,
    (np.dtype('i8'), np.dtype('i2')) : _phm.MultiDict_i8_i2,
    (np.dtype('i8'), np.dtype('i4')) : _phm.MultiDict_i8_i4,
    (np.dtype('i8'), np.dtype('i8')) : _phm.MultiDict_i8_i8,
    (np.dtype('i8'), np.dtype('f4')) : _phm.MultiDict_i8_f4,
    (np.dtype('i8'), np.dtype('f8')) : _phm.MultiDict_i8_f8,
    (np.dtype('i8'), np.dtype('S8')) : _phm.MultiDict_i8_S8,
    (np.dtype('i8'), np.dtype('S16')) : _phm.MultiDict_i8_S16,
    (np.dtype('i8'), np.dtype('S32')) : _phm.MultiDict_i8_S32,
    (np.dtype('i8'), np.dtype('S64')) : _phm.MultiDict_i8_S64,
    (np.dtype('i8'), np.dtype('S128')) : _phm.MultiDict_i8_S128,
    (np.dtype('i8'), np.dtype('S256')) : _phm.MultiDict_i8_S256,
    (np.dtype('f4'), np.dtype('u1')) : _phm.MultiDict_f4_u1,
    (np.dtype('f4'), np.dtype('u2')) : _phm.MultiDict_f4_u2,
    (np.dtype('f4'), np.dtype('u4')) : _phm.MultiDict_f4_u4,
    (np.dtype('f4'), np.dtype('u8')) : _phm.MultiDict_f4_u8,
    (np.dtype('f4'), np.dtype('i1')) : _phm.MultiDict_f4_i1,
    (np.dtype('f4'), np.dtype('i2')) : _phm.MultiDict_f4_i2,
    (np.dtype('f4'), np.dtype('i4')) : _phm.MultiDict_f4_i4,
    (np.dtype('f4'), np.dtype('i8')) : _phm.MultiDict_f4_i8,
    (np.dtype('f4'), np.dtype('f4')) : _phm.MultiDict_f4_f4,
    (np.dtype('f4'), np.dtype('f8')) : _phm.MultiDict_f4_f8,
    (np.dtype('f4'), np.dtype('S8')) : _phm.MultiDict_f4_S8,
    (np.dtype('f4'), np.dtype('S16')) : _phm.MultiDict_f4_S16,
    (np.dtype('f4'), np.dtype('S32')) : _phm.MultiDict_f4_S32,
    (np.dtype('f4'), np.dtype('S64')) : _phm.MultiDict_f4_S64,
    (np.dtype('f4'), np.dtype('S128')) : _phm.MultiDict_f4_S128,
    (np.dtype('f4'), np.dtype('S256')) : _phm.MultiDict_f4_S256,
    (np.dtype('f8'), np.dtype('u1')) : _phm.MultiDict_f8_u1,
    (np.dtype('f8'), np.dtype('u2')) : _phm.MultiDict_f8_u2,
    (np.dtype('f8'), np.dtype('u4')) : _phm.MultiDict_f8_u4,
    (np.dtype('f8'), np.dtype('u8')) : _phm.MultiDict_f8_u8,
    (np.dtype('f8'), np.dtype('i1')) : _phm.MultiDict_f8_i1,
    (np.dtype('f8'), np.dtype('i2')) : _phm.MultiDict_f8_i2,
    (np.dtype('f8'), np.dtype('i4')) : _phm.MultiDict_f8_i4,
    (np.dtype('f8'), np.dtype('i8')) : _phm.MultiDict_f8_i8,
    (np.dtype('f8'), np.dtype('f4')) : _phm.MultiDict_f8_f4,
    (np.dtype('f8'), np.dtype('f8')) : _phm.MultiDict_f8_f8,
    (np.dtype('f8'), np.dtype('S8')) : _phm.MultiDict_f8_S8,
    (np.dtype('f8'), np.dtype('S16')) : _phm.MultiDict_f8_S16,
    (np.dtype('f8'), np.dtype('S32')) : _phm.MultiDict_f8_S32,
    (np.dtype('f8'), np.dtype('S64')) : _phm.MultiDict_f8_S64,
    (np.dtype('f8'), np.dtype('S128')) : _phm.MultiDict_f8_S128,
    (np.dtype('f8'), np.dtype('S256')) : _phm.MultiDict_f8_S256,
    (np.dtype('S8'), np.dtype('u1')) : _phm.MultiDict_S8_u1,
    (np.dtype('S8'), np.dtype('u2')) : _phm.MultiDict_S8_u2,
    (np.dtype('S8'), np.dtype('u4')) : _phm.MultiDict_S8_u4,
    (np.dtype('S8'), np.dtype('u8')) : _phm.MultiDict_S8_u8,
    (np.dtype('S8'), np.dtype('i1')) : _phm.MultiDict_S8_i1,
    (np.dtype('S8'), np.dtype('i2')) : _phm.MultiDict_S8_i2,
    (np.dtype('S8'), np.dtype('i4')) : _phm.MultiDict_S8_i4,
    (np.dtype('S8'), np.dtype('i8')) : _phm.MultiDict_S8_i8,
    (np.dtype('S8'), np.dtype('f4')) : _phm.MultiDict_S8_f4,
    (np.dtype('S8'), np.dtype('f8')) : _phm.MultiDict_S8_f8,
    (np.dtype('S8'), np.dtype('S8')) : _phm.MultiDict_S8_S8,
    (np.dtype('S8'), np.dtype('S16')) : _phm.MultiDict_S8_S16,
    (np.dtype('S8'), np.dtype('S32')) : _phm.MultiDict_S8_S32,
    (np.dtype('S8'), np.dtype('S64')) : _phm.MultiDict_S8_S64,
    (np.dtype('S8'), np.dtype('S128')) : _phm.MultiDict_S8_S128,
    (np.dtype('S8'), np.dtype('S256')) : _phm.MultiDict_S8_S256,
    (np.dtype('S16'), np.dtype('u1')) : _phm.MultiDict_S16_u1,
    (np.dtype('S16'), np.dtype('u2')) : _phm.MultiDict_S16_u2,
    (np.dtype('S16'), np.dtype('u4')) : _phm.MultiDict_S16_u4,
    (np.dtype('S16'), np.dtype('u8')) : _phm.MultiDict_S16_u8,
    (np.dtype('S16'), np.dtype('i1')) : _phm.MultiDict_S16_i1,
    (np.dtype('S16'), np.dtype('i2')) : _phm.MultiDict_S16_i2,
    (np.dtype('S16'), np.dtype('i4')) : _phm.MultiDict_S16_i4,
    (np.dtype('S16'), np.dtype('i8')) : _phm.MultiDict_S16_i8,
    (np.dtype('S16'), np.dtype('f4')) : _phm.MultiDict_S16_f4,
    (np.dtype('S16'), np.dtype('f8')) : _phm.MultiDict_S16_f8,
    (np.dtype('S16'), np.dtype('S8')) : _phm.MultiDict_S16_S8,
    (np.dtype('S16'), np.dtype('S16')) : _phm.MultiDict_S16_S16,
    (np.dtype('S16'), np.dtype('S32')) : _phm.MultiDict_S16_S32,
    (np.dtype('S16'), np.dtype('S64')) : _phm.MultiDict_S16_S64,
    (np.dtype('S16'), np.dtype('S128')) : _phm.MultiDict_S16_S128,
    (np.dtype('S16'), np.dtype('S256')) : _phm.MultiDict_S16_S256,
    (np.dtype('S32'), np.dtype('u1')) : _phm.MultiDict_S32_u1,
    (np.dtype('S32'), np.dtype('u2')) : _phm.MultiDict_S32_u2,
    (np.dtype('S32'), np.dtype('u4')) : _phm.MultiDict_S32_u4,
    (np.dtype('S32'), np.dtype('u8')) : _phm.MultiDict_S32_u8,
    (np.dtype('S32'), np.dtype('i1')) : _phm.MultiDict_S32_i1,
    (np.dtype('S32'), np.dtype('i2')) : _phm.MultiDict_S32_i2,
    (np.dtype('S32'), np.dtype('i4')) : _phm.MultiDict_S32_i4,
    (np.dtype('S32'), np.dtype('i8')) : _phm.MultiDict_S32_i8,
    (np.dtype('S32'), np.dtype('f4')) : _phm.MultiDict_S32_f4,
    (np.dtype('S32'), np.dtype('f8')) : _phm.MultiDict_S32_f8,
    (np.dtype('S32'), np.dtype('S8')) : _phm.MultiDict_S32_S8,
    (np.dtype('S32'), np.dtype('S16')) : _phm.MultiDict_S32_S16,
    (np.dtype('S32'), np.dtype('S32')) : _phm.MultiDict_S32_S32,
    (np.dtype('S32'), np.dtype('S64')) : _phm.MultiDict_S32_S64,
    (np.dtype('S32'), np.dtype('S128')) : _phm.MultiDict_S32_S128,
    (np.dtype('S32'), np.dtype('S256')) : _phm.MultiDict_S32_S256,
    (np.dtype('S64'), np.dtype('u1')) : _phm.MultiDict_S64_u1,
    (np.dtype('S64'), np.dtype('u2')) : _phm.MultiDict_S64_u2,
    (np.dtype('S64'), np.dtype('u4')) : _phm.MultiDict_S64_u4,
    (np.dtype('S64'), np.dtype('u8')) : _phm.MultiDict_S64_u8,
    (np.dtype('S64'), np.dtype('i1')) : _phm.MultiDict_S64_i1,
    (np.dtype('S64'), np.dtype('i2')) : _phm.MultiDict_S64_i2,
    (np.dtype('S64'), np.dtype('i4')) : _phm.MultiDict_S64_i4,
    (np.dtype('S64'), np.dtype('i8')) : _phm.MultiDict_S64_i8,
    (np.dtype('S64'), np.dtype('f4')) : _phm.MultiDict_S64_f4,
    (np.dtype('S64'), np.dtype('f8')) : _phm.MultiDict_S64_f8,
    (np.dtype('S64'), np.dtype('S8')) : _phm.MultiDict_S64_S8,
    (np.dtype('S64'), np.dtype('S16')) : _phm.MultiDict_S64_S16,
    (np.dtype('S64'), np.dtype('S32')) : _phm.MultiDict_S64_S32,
    (np.dtype('S64'), np.dtype('S64')) : _phm.MultiDict_S64_S64,
    (np.dtype('S64'), np.dtype('S128')) : _phm.MultiDict_S64_S128,
    (np.dtype('S64'), np.dtype('S256')) : _phm.MultiDict_S64_S256,
    (np.dtype('S128'), np.dtype('u1')) : _phm.MultiDict_S128_u1,
    (np.dtype('S128'), np.dtype('u2')) : _phm.MultiDict_S128_u2,
    (np.dtype('S128'), np.dtype('u4')) : _phm.MultiDict_S128_u4,
    (np.dtype('S128'), np.dtype('u8')) : _phm.MultiDict_S128_u8,
    (np.dtype('S128'), np.dtype('i1')) : _phm.MultiDict_S128_i1,
    (np.dtype('S128'), np.dtype('i2')) : _phm.MultiDict_S128_i2,
    (np.dtype('S128'), np.dtype('i4')) : _phm.MultiDict_S128_i4,
    (np.dtype('S128'), np.dtype('i8')) : _phm.MultiDict_S128_i8,
    (np.dtype('S128'), np.dtype('f4')) : _phm.MultiDict_S128_f4,
    (np.dtype('S128'), np.dtype('f8')) : _phm.MultiDict_S128_f8,
    (np.dtype('S128'), np.dtype('S8')) : _phm.MultiDict_S128_S8,
    (np.dtype('S128'), np.dtype('S16')) : _phm.MultiDict_S128_S16,
    (np.dtype('S128'), np.dtype('S32')) : _phm.MultiDict_S128_S32,
    (np.dtype('S128'), np.dtype('S64')) : _phm.MultiDict_S128_S64,
    (np.dtype('S128'), np.dtype('S128')) : _phm.MultiDict_S128_S128,
    (np.dtype('S128'), np.dtype('S256')) : _phm.MultiDict_S128_S256,
    (np.dtype('S256'), np.dtype('u1')) : _phm.MultiDict_S256_u1,
    (np.dtype('S256'), np.dtype('u2')) : _phm.MultiDict_S256_u2,
    (np.dtype('S256'), np.dtype('u4')) : _phm.MultiDict_S256_u4,
    (np.dtype('S256'), np.dtype('u8')) : _phm.MultiDict_S256_u8,
    (np.dtype('S256'), np.dtype('i1')) : _phm.MultiDict_S256_i1,
    (np.dtype('S256'), np.dtype('i2')) : _phm.MultiDict_S256_i2,
    (np.dtype('S256'), np.dtype('i4')) : _phm.MultiDict_S256_i4,
    (np.dtype('S256'), np.dtype('i8')) : _phm.MultiDict_S256_i8,
    (np.dtype('S256'), np.dtype('f4')) : _phm.MultiDict_S256_f4,
    (np.dtype('S256'), np.dtype('f8')) : _phm.MultiDict_S256_f8,
    (np.dtype('S256'), np.dtype('S8')) : _phm.MultiDict_S256_S8,
    (np.dtype('S256'), np.dtype('S16')) : _phm.MultiDict_S256_S16,
    (np.dtype('S256'), np.dtype('S32')) : _phm.MultiDict_S256_S32,
    (np.dtype('S256'), np.dtype('S64')) : _phm.MultiDict_S256_S64,
    (np.dtype('S256'), np.dtype('S128')) : _phm.MultiDict_S256_S128,
    (np.dtype('S256'), np.dtype('S256')) : _phm.MultiDict_S256_S256,
}
