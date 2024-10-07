def solution(n):
    num_str = str(n)
    digits = list(num_str)
    digits.reverse()
    return [int(x) for x in digits]
   # return solution


string = [548702838394]
print(solution(string))