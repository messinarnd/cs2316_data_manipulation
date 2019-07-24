# Christopher Messina
# cmessina6
# 903023165

def time_seconds(time):
    """Take a time in MM:SS format and return the corresponding number of seconds

    Parameters:
    time: str -- time in MM:SS format

    Return:
    int -- number of seconds of a time specified in MM:SS format

    Usage Examples:
    >>> time_seconds("2:30")
    150
    """
    if len(time) == 4:
        minutes = time[0]
    elif len(time) == 5:
        minutes = time[0:2]
    else:
        minutes = 0

    mins = int(minutes)
    seconds = time[len(time) - 2: len(time)]
    sec = int(seconds)
    sec += mins * 60
    return sec

def score(entry):
    """Take a dict containing the data for a participant and calculate a score

    Parameters:
    entry: dict[str -> Any] -- a dictonary containng the fitness test data for
           an entry in the contest

    Return:
    int -- score computed as follows:
           swim in seconds + run insconds - (2 * pushups) - situps - (pullups * 6)

    Usage Examples:
    >>> score({'Run': '11:10', 'Push-ups': '60', 'Sit-ups': '80', 'Swim': '11:45', 'Name': 'Tyrion', 'Pull-ups': '30'})
    995
    """
    score = time_seconds(entry['Swim'])
    score += time_seconds(entry['Run'])
    score -= (int(entry['Push-ups']) * 2)
    score -= int(entry['Sit-ups'])
    score -= int(entry['Pull-ups']) * 6
    return score

def average(data, event):
    """Take a list of dicts of fitness test entries and return the average for
    a single event

    Parameters:
    data: List[dict] -- a list of dictionaries of fitness test data
    event: str -- the name of an event, from the header of the data file

    Return:
    float -- the average score for that event. For run and swim, should be in
             seconds

    Usage Examples:
    >>> average([{'Run': '11:10', 'Push-ups': '60', 'Sit-ups': '80', 'Swim': '11:45', 'Name': 'Tyrion', 'Pull-ups': '30'}, {'Run': '12:00', 'Push-ups': '100', 'Sit-ups': '100', 'Swim': '12:45', 'Name': 'Drogo', 'Pull-ups': '20'}], "Pull-ups")
    25.0
    """
    if len(data) == 0:
        return 0

    score = 0
    # scores = []
    count = 0
    for i in data:
        count += 1
        if event == 'Swim' or event == 'Run':
            num = time_seconds(i[event])
            #print("first if")
            #Sprint(num)
        else:
            num = int(i[event])
            #print("second if")
            #print(num)
        #scores[count] =
        #print("end of loop count" + str(count))
        score += num
        #print ("score" + str(score))

    # total = 0
    # for x in range(0,len(scores)):
    #     total += scores[x]
    score = float(score)

    return score / count

def winner(data, event):
    """Take a list of dicts of fitness test entries and return the winner of
    event

    Parameters:
    data: List[dict] -- a list of dictionaries of fitness test data
    event: str -- the name of an event, from the header of the data file

    Return:
    (str, int) -- a tuple with the name of the winner of the event and the score
                  they got for that event. Swim and run should be in seconds

    Usage Examples:
    >>> winner([{'Run': '11:10', 'Push-ups': '60', 'Sit-ups': '80', 'Swim': '11:45', 'Name': 'Tyrion', 'Pull-ups': '30'}, {'Run': '12:00', 'Push-ups': '100', 'Sit-ups': '100', 'Swim': '12:45', 'Name': 'Drogo', 'Pull-ups': '20'}], "Pull-ups")
    ('Tyrion', 30)
    """
    if len(data) == 0:
        return ('none', 0)

    if event == 'Swim' or event == 'Run':
        winScore = 1000000000
        for i in data:
            s = time_seconds(i[event])
            if s < winScore:
                winScore = s
                name = i['name']
    else:
        winScore = -1
        for i in data:
            s = int(i[event])
            if s > winScore:
                winScore = s
                name = i['Name']

    return (name, winScore)
