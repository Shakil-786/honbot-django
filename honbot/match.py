def match(match_id):
    return 5


def playerMatches(match_json):
    print match_json
    print '****'
    if match_json[0]['win_loss_history'] is not None:
        data = match_json[0]['win_loss_history'].split('|')
        matches = []
        temp = []
        for i in data:
            temp = i.split('/')
            if temp[0] != '':
                if temp[1] == 'W':
                    temp[1] = True
                else:
                    temp[1] = False
                matches.append(temp)
        return matches[:10]
    else:
        matches = []
        return matches
