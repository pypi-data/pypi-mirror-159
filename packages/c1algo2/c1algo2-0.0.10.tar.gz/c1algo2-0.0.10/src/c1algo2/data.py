import copy

MONTH_TO_SEMESTER = {
    "09": "Fall",
    "01": "Spring",
    "05": "Summer"
}


def parse_input(backend_input_data: dict, progression_data: dict) -> dict:
    # Outermost:    Dictionary, where keys are courses e.g. "CSC111" and values
    #               are dicts.
    # Each dict within a course contains the following structure:
    # {
    #   "CSCS111": {
    #       "2008":
    #           {
    #               "1": 10,
    #               "2": 10,
    #               "2T": 10,
    #               "3": 10,
    #               "4": 10,
    #               "5": 10,
    #               "6": 10,
    #               "7": 10,
    #               "Fall_Enrollment": 50,
    #               "Fall_MaxEnrollment": 60,
    #               "Spring_Enrollment": 50,
    #               "Spring_MaxEnrollment": 60,
    #               "Summer_Enrollment": 50,
    #               "Summer_MaxEnrollment": 60
    #           }
    #   }
    # }
    # course{year{term{section{}}}}

    final_input = {}

    for course in backend_input_data:
        offering = course["subjectCourse"]

        if course['term'].endswith('09'):
            year = course["term"][0:4]
        else:
            year = str(int(course["term"][0:4]) - 1)
        term = course['term'][-2:]
        # "Fall", "Spring" or "Summer"
        term = MONTH_TO_SEMESTER[term]

        # if the course is already in the dictionary, just append data to that
        # key
        if offering in final_input:

            if year in final_input[offering]:

                if year in progression_data:
                    final_input[offering][year].update(progression_data[year])
                else:
                    # add manually
                    final_input[offering][year].update(null_progression())

                final_input[offering][year].setdefault(f"{term}_Enrollment", 0)
                final_input[offering][year].setdefault(f"{term}_MaxEnrollment", 0)
                final_input[offering][year][f"{term}_Enrollment"] += course["enrollment"]
                final_input[offering][year][f"{term}_MaxEnrollment"] += course["maximumEnrollment"]

            else:
                new_year = {}
                final_input[offering][year] = new_year
                # final_input[offering]
                if year in progression_data:
                    final_input[offering][year].update(progression_data[year])
                else:
                    # add manually
                    final_input[offering][year].update(null_progression())

                new_year[f"{term}_Enrollment"] = course["enrollment"]
                new_year[f"{term}_MaxEnrollment"] = course["maximumEnrollment"]

                final_input[offering][year] = new_year

        # if the course is new, add as a new key
        else:

            final_input[course["subjectCourse"]] = {course["term"][0:4]: {}}
            year = course["term"][0:4]

            new_year = {}

            new_year[f"{term}_Enrollment"] = course["enrollment"]
            new_year[f"{term}_MaxEnrollment"] = course["maximumEnrollment"]

            final_input[course['subjectCourse']][year] = new_year
            final_input[course['subjectCourse']][year].update(null_progression())

    return final_input


def get_courses(schedule):

    courses = []

    for semester in schedule:
        for course in schedule[semester]:
            capacity = course["sections"][0]["capacity"]
            if capacity in (0, None):
                courses.append(course["course"]["code"])

    courses = list(dict.fromkeys(courses))

    return courses


def null_progression() -> dict:
    empty_data = {
        "1": 0,
        "2": 0,
        "2T": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0
    }
    return empty_data


def model_1_output(input_file: dict) -> dict:

    # use deepcopy to change iterable objects in the dictionary
    result = copy.deepcopy(input_file)
    for course in result:
        for year in result[course]:

            result[course][year]["Year_Enrollment"] = 0
            result[course][year]["Year_MaxEnrollment"] = 0

            for term in ("Fall", "Spring", "Summer"):
                if f"{term}_Enrollment" in result[course][year]:
                    result[course][year]["Year_Enrollment"] += result[course][year][f"{term}_Enrollment"]
                    result[course][year]["Year_MaxEnrollment"] += result[course][year][f"{term}_MaxEnrollment"]
                    result[course][year].pop(f"{term}_Enrollment")
                    result[course][year].pop(f"{term}_MaxEnrollment")
    return result


# This is not ugly anymore, its brother is though.
def fill_capacities(schedule: dict, capacities: dict, year: int) -> dict:
    Semesters = {"fall": 0, "spring": 1, "summer": 2}

    # copy the schedule dict for filling.
    final_schedule = copy.deepcopy(schedule)

    scheduleMap = {}
    for semester in schedule:
        scheduleMap[semester] = {}
        for course in schedule[semester]:
            course_code = course["course"]["code"]
            scheduleMap[semester][course_code] = course

    for semester in Semesters:
        fill_helper(
            (semester, Semesters[semester]),
            final_schedule,
            capacities,
            scheduleMap
        )

    return final_schedule


def fill_helper(semesterPair: tuple, schedule: dict, capacities: dict, map: dict) -> list:
    semester = semesterPair[0]
    index = semesterPair[1]

    for code in capacities:
        capacity = capacities[code][index]
        if capacity is not None and code in map[semester]:
            # we sized and the schedule has this course in the current semester, so we just fill.
            for i in range(len(schedule[semester])):
                if schedule[semester][i]["course"]["code"] == code:
                    schedule[semester][i]["sections"][0]["capacity"] = capacity

        elif capacity is not None and code not in map[semester]:
            # we sized but the course is NOT already in the schedule, so we add a new offering/section.
            for sem in ["fall", "spring", "summer"]:
                if code in map[sem]:
                    offering = map[sem][code]
                    offering["sections"][0]["capacity"] = capacity
                    break
            schedule[semester].append(offering)

        else:
            if capacities[code][index] is None and code in map[semester]:
                # we did not size and the course is in the input schedule, expecting a capacity.
                print("DEFAULTING: " + code)
