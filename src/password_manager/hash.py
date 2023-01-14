from passlib.hash import argon2, bcrypt, sha256_crypt

# Class which represents the collection of hash algorithms we can use to hash a certain input. Add additional hash functions as needed.
class HashAlgos():
    """

    For any methods with the keyword pass in them, please place the code you'd like to run above the statement, and remove pass completely after doing so.

    """

    def sha256_hash(input_to_hash : str, salt=""):
        """
        Use SHA256 to hash the given salt and input.
        
        :param input_to_hash: the string to hash
        :param salt: the salt to append to the input before hashing. By default is empty string (not recommended for security)
        """
        pass

    def sha512_hash(input_to_hash : str, salt=""):
        """
        Use SHA512 to hash the given salt and input.
        
        :param input_to_hash: the string to hash
        :param salt: the salt to append to the input before hashing. By default is empty string (not recommended for security)
        """
        pass

    def argon2_hash(input_to_hash : str, salt=""):
        """
        Use argon2 to hash the given salt and input.
        
        :param input_to_hash: the string to hash
        :param salt: the salt to append to the input before hashing. By default is empty string (not recommended for security)
        """
        pass

    def bcrypt_hash(input_to_hash : str, salt=""):
        """
        Use bcrypt to hash the given salt and input.
        
        :param input_to_hash: the string to hash
        :param salt: the salt to append to the input before hashing. By default is empty string (not recommended for security)
        """
        pass

    """
    A dictionary containing a number (int) to function mapping. 
    Example: Calling hash_algorithms[1]("string", "salt") is the same thing as calling sha256_hash("string", "salt")
    NOTE: Add additional mappings from numbers to hash functions as needed.
    """
    hash_algorithms = {
        1: sha256_hash,
        2: sha512_hash,
        3: argon2_hash,
        4: bcrypt_hash,
    }

    def number_codes(self):
        """
        Returns a list of strings for all the number codes for the hash functions that are supported, as indicated by hash_algorithms.
        Example: 1 becomes '1', 2 becomes '2', etc.
        """
        numbers = [str(k) for k in self.hash_algorithms.keys()]
        return numbers
