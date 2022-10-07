import math

def test_filters():
   new_numbers = list(filter(lambda x: x%2 == 0,[1,2,3,4,5,6,7,8,9,10]))
   assert new_numbers == [2,4,6,8,10]

def test_map():
   new_list = list(map(int,['1','2','3','4','5']))
   assert new_list == [1,2,3,4,5]

def test_sort():
   numbers = [1,25,-9,56,-128]
   numbers.sort()
   assert numbers == [-128,-9,1,25,56]

def test_sqrt():
   sqrt_list = list(map(lambda numbers:math.sqrt(numbers),[4,9,16,25,36]))
   assert sqrt_list == [2,3,4,5,6]

def test_pow():
   pow_list = list(map(lambda numbers:math.pow(numbers,2),[2,4,7,9,11]))
   assert pow_list == [4,16,49,81,121]

def test_hypot():
   assert math.hypot(4,1) == 4.123105625617661
   assert math.hypot(-2,0) == 2.0
   assert math.hypot(-1,2) == 2.23606797749979