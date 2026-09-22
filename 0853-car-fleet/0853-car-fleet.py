class Solution(object):
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for p, s in cars:
            time = float(target - p) / s

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)


        