from collections import deque
class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        q=deque(students)
        i=0
        c=0
        while q and c<len(q):
            s=q.popleft()

            if s==sandwiches[i]:
                i=i+1
                c=0
            else:
                q.append(s)
                c=c+1
        return c        

        