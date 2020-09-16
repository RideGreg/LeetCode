'''
Students may decide to take different "tracks" or sequences of courses in the Computer Science curriculum. There may be more than one track that includes the same course, but each student follows a single linear track from a "root" node to a "leaf" node. In the graph below, their path always moves left to right.

Write a function that takes a list of (source, destination) pairs, and returns the name of all of the courses that the students could be taking when they are halfway through their track of courses.

Sample input:
all_courses = [
    ["Logic", "COBOL"],
    ["Data Structures", "Algorithms"],
    ["Creative Writing", "Data Structures"],
    ["Algorithms", "COBOL"],
    ["Intro to Computer Science", "Data Structures"],
    ["Logic", "Compilers"],
    ["Data Structures", "Logic"],
    ["Creative Writing", "System Administration"],
    ["Databases", "System Administration"],
    ["Creative Writing", "Databases"],
    ["Intro to Computer Science", "Graphics"],
]

Sample output (in any order):
          ["Data Structures", "Creative Writing", "Databases", "Intro to Computer Science"]

All paths through the curriculum (midpoint *highlighted*):

*Intro to C.S.* -> Graphics
Intro to C.S. -> *Data Structures* -> Algorithms -> COBOL
Intro to C.S. -> *Data Structures* -> Logic -> COBOL
Intro to C.S. -> *Data Structures* -> Logic -> Compiler
Creative Writing -> *Databases* -> System Administration
*Creative Writing* -> System Administration
Creative Writing -> *Data Structures* -> Algorithms -> COBOL
Creative Writing -> *Data Structures* -> Logic -> COBOL
Creative Writing -> *Data Structures* -> Logic -> Compilers

Visual representation:

                    ____________
                    |          |
                    | Graphics |
               ---->|__________|
               |                          ______________
____________   |                          |            |
|          |   |    ______________     -->| Algorithms |--\     _____________
| Intro to |   |    |            |    /   |____________|   \    |           |
| C.S.     |---+    | Data       |   /                      >-->| COBOL     |
|__________|    \   | Structures |--+     ______________   /    |___________|
                 >->|____________|   \    |            |  /
____________    /                     \-->| Logic      |-+      _____________
|          |   /    ______________        |____________|  \     |           |
| Creative |  /     |            |                         \--->| Compilers |
| Writing  |-+----->| Databases  |                              |___________|
|__________|  \     |____________|-\     _________________________
               \                    \    |                       |
                \--------------------+-->| System Administration |
                                         |_______________________|

Complexity analysis variables:

n: number of pairs in the input
'''

all_courses = [
    ["Logic", "COBOL"],
    ["Data Structures", "Algorithms"],
    ["Creative Writing", "Data Structures"],
    ["Algorithms", "COBOL"],
    ["Intro to Computer Science", "Data Structures"],
    ["Logic", "Compilers"],
    ["Data Structures", "Logic"],
    ["Creative Writing", "System Administration"],
    ["Databases", "System Administration"],
    ["Creative Writing", "Databases"],
    ["Intro to Computer Science", "Graphics"],
]


# n len(paris)
# m len(id)
# Time: O(m^2*n)
# Space: O(n) + O(n^2) key of answer is n^2 1+2+...n
# 2 students, each of them n//2 courses
from typing import List
import collections

# n # of pairs
# Time O(n^2), E n^2 // 2
# Space O(n)
# edge case 1 -> 2,3,,...10
def getCourse(prereqs):
    allcourses = set() # O(n)
    in_degree = collections.defaultdict(int) # space O(n)
    graph = collections.defaultdict(set) # space O(n)
    for pre, course in prereqs:
        allcourses.add(pre)
        allcourses.add(course)
        in_degree[course] += 1
        graph[pre].add(course)
    
    n = len(allcourses)
    zero_in = collections.deque([x for x in allcourses if x not in in_degree])
    taken = 0
    while zero_in:
        cur = zero_in.popleft()
        taken += 1
        if taken == (n+1) // 2: # n=5/6 -> 3
            return cur
        for nei in graph[cur]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                zero_in.append(nei)

# You are a developer for a university. Your current project is to develop a system for
# students to find courses they share with friends. The university has a system for querying
# courses students are enrolled in, returned as a list of (ID, course) pairs.
#
# Write a function that takes in a list of (student ID number, course name) pairs and returns,
# for every pair of students, a list of all courses they share.
def find_pairs(pairs: List[List[str]]) -> dict:
    reg = collections.defaultdict(set)
    for idx, name in pairs:
        reg[idx].add(name)
        
    ans = {}
    for id1 in reg:
        for id2 in reg:
            if id2 > id1:
                key = ','.join([id1, id2])
                ans[key] = [x for x in reg[id1] if x in reg[id2]]
    return ans

student_course_pairs_1 = [
  ["58", "Software Design"],
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
]
print(find_pairs(student_course_pairs_1))
'''
{
  '58,17': ["Software Design", "Linear Algebra"]
  [58, 94]: ["Economics"]
  [58, 25]: ["Economics"]
  [94, 25]: ["Economics"]
  [17, 94]: []
  [17, 25]: []
}
'''