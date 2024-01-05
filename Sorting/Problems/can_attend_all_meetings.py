
def can_attend_all_meetings(intervals):
    """
    Problem:
    Given a list of meeting intervals where each interval consists of a start and an end time, 
    check if a person can attend all the given meetings such that only one meeting can be attended at a time.
    https://aaronice.gitbook.io/lintcode/sweep-line/meeting-rooms

    Complexity:
    * Time: O(nlog(n))
    * Space: O(1) 
    """
    # Write your code here.
    intervals.sort()
    n = len(intervals)
    for i in range(n - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return 0
    return 1
