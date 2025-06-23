"""написати рекурсивну функцію, яка буде рахувати суму
   10-> 10+9+8+7+6+5+4+3+2+1"""
def sum_numbers(number: int) -> int:
    #умова коли вона закінчується
    if number == 1:
        return 1
    # рекурсивний виклик функції
    result = number + sum_numbers(number - 1)
    # Виклик функції
    return result
print(sum_numbers(10))  # 55
    
