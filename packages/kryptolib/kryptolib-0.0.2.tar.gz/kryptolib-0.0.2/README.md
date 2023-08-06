# KryptoLib

## Simple Krypto library

## About
krypto library provides a simple interface to sign, verify the digital signature for one or more krypto algorithms platforms independent.

## Documentation

## Quickstart

#### Install pip library
```
$ pip install kryptolib
```

#### Krypto framwork to generate key pair
```
from kryptolib import krypto_obj 
krypto = krypto_obj('Ed25519')
privkey,pubkey = krypto.keygen(secret_key)

```

#### Krypto framwork to generate signature
```
signature = krypto.sign(privkey, pubkey, msg)
```

#### Krypto framwork to verify signature
```
krypto.verify(public, msg, signature)
```

## Issues

Please submit a [new issue report on the GitHub repository](https://github.com/subramanya-a/kryptolib/issues) with a detailed overview of the problem that you are having.


## Project Contributors

- [Subramanya A](https://github.com/subramanya-a/) (@Subramanya.a)

---
[MIT License](https://github.com/subramanya-a/kryptolib/master/docs/LICENSE) | Built with the [Kryptolib](https://pypi.python.org/pypi/Kryptolib)