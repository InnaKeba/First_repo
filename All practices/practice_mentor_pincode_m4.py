import re
def validated_pincode(pincode_str:str) -> bool:
   return re.fullmatch(r'[0-9]{4}|[0-9]{6}', pincode_str) is not None
assert validated_pincode("1234") == True
assert validated_pincode("123456") == True
assert validated_pincode("a1234") == False
assert validated_pincode("12345") == False
