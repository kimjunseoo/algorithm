def _max(idx, total, _plus, _minus, _multiply, _divide):
    global nums
    global maximum
    
    if _plus > buho[0]:
        return
    if _minus > buho[1]:
        return
    if _multiply > buho[2]:
        return
    if _divide > buho[3]:
        return
    
    if idx == N - 1:
        maximum = max(maximum, total)
        return
    
    #plus
    _max(idx + 1, total + nums[idx + 1], _plus + 1, _minus, _multiply, _divide)

    #minus
    _max(idx + 1, total - nums[idx + 1], _plus, _minus + 1, _multiply, _divide)

    #multiply
    _max(idx + 1, total * nums[idx + 1], _plus, _minus, _multiply + 1, _divide)
    
    #divide
    if total < 0:
        _max(idx + 1, -(-total // nums[idx + 1]), _plus, _minus, _multiply, _divide + 1)
    else:
        _max(idx + 1, total // nums[idx + 1], _plus, _minus, _multiply, _divide + 1)

def _min(idx, total, _plus, _minus, _multiply, _divide):
    global nums
    global minimum
    
    if _plus > buho[0]:
        return
    if _minus > buho[1]:
        return
    if _multiply > buho[2]:
        return
    if _divide > buho[3]:
        return
    
    if idx == N - 1:
        minimum = min(minimum, total)
        return
    
    #plus
    _min(idx + 1, total + nums[idx + 1], _plus + 1, _minus, _multiply, _divide)

    #minus
    _min(idx + 1, total - nums[idx + 1], _plus, _minus + 1, _multiply, _divide)

    #multiply
    _min(idx + 1, total * nums[idx + 1], _plus, _minus, _multiply + 1, _divide)
    
    #divide
    if total < 0:
        _min(idx + 1, -(-total // nums[idx + 1]), _plus, _minus, _multiply, _divide + 1)
    else:
        _min(idx + 1, total // nums[idx + 1], _plus, _minus, _multiply, _divide + 1)

N = int(input())

nums = list(map(int, input().split()))

buho = list(map(int, input().split()))

minimum = 9999999999999
maximum = -999999999999

_min(0, nums[0], 0, 0, 0, 0)
_max(0, nums[0], 0, 0, 0, 0)

print(maximum)
print(minimum)
