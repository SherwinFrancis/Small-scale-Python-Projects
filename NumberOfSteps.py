def climbStairs(n: int) -> int:
        a = 0
        b = 1
        for i in range(0,n):
            prevA = a
            a = b
            b = b + prevA
        return b

