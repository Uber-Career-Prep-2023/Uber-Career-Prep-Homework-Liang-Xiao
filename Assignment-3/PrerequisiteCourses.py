"""
Given a list of courses that a student needs to take to complete their major and a map of courses to their prerequisites,
return a valid order for them to take their courses assuming they only take one course for their major at once.

time complexity O(n + m), n refer to courses and m refer to edges in course map
space complexity O(n + m), n refer to courses and m refer to edges in course map
time spent on the question: about 20 min
"""


# create adjacency_list from map of courses
def build_graph(courses, course_map):
    graph = {}
    for node in courses:
        graph[node] = []
    for node in course_map:
        for pre_course in course_map[node]:
            graph[pre_course].append(node)
    return graph


def PrerequisiteCourses(courses, course_map):
    graph = build_graph(courses, course_map)

    # create a list to store the number of prerequisites of courses.
    in_degree_dict = {node: 0 for node in courses}
    for node in graph:
        for neighbour in graph[node]:
            in_degree_dict[neighbour] += 1

    # find the first course with has no prerequisites.
    zero_degree = []
    for node in in_degree_dict:
        if in_degree_dict[node] == 0:
            zero_degree.append(node)

    # store the courses in topological_order
    topological_order = []
    while len(zero_degree) > 0:
        node = zero_degree.pop()
        topological_order.append(node)
        for neighbor in graph[node]:
            in_degree_dict[neighbor] -= 1
            if in_degree_dict[neighbor] == 0:
                zero_degree.append(neighbor)
    return topological_order


if __name__ == "__main__":
    input_courses = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
    input_map = {"Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"],
                 "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"]}
    print(PrerequisiteCourses(input_courses, input_map))
    input_courses = ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature",
                     "Plays & Screenplays"]
    input_map = {"Contemporary Literature": ["Intro to Writing"],
                 "Ancient Literature": ["Intro to Writing"],
                 "Comparative Literature": ["Ancient Literature", "Contemporary Literature"],
                 "Plays & Screenplays": ["Intro to Writing"]}
    print(PrerequisiteCourses(input_courses, input_map))
