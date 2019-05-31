# for each log file generates a JSON file of the curent relationship graph
from reduce_logs import reduce_logs
import json
import os
import errno

MAX_USER_ID = 1200


def dumpJsonToFile(data, m, d, h):
    filename = "../gen/relationships/{}/{}/{}-{}-{}.json".format(m, d, m, d, h)
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(filename, "w") as outfile:
        json.dump(data, outfile)


def parse_judgement(log):
    try:
        requestUrl = log['httpRequest']['requestUrl']
        if 'judge' in requestUrl:
            request = log['jsonPayload']['metadata']['request']
            body = request['body']
            candidateUserId = body['candidateUserId']
            liked = body['liked']
            scene = body['scene']
            criticUserId = request['user']['id']

            # print(candidateUserId,
            #       liked,
            #       scene,
            #       criticUserId)
            return (criticUserId, candidateUserId, liked, scene)
    except:
        # e.g. Info logs
        return None


def gen_hour_relationships(log_hour_file, curr_relationships):
    m, d, h, file_name = log_hour_file
    print("Relationships for: {}:{}:{} | {}".format(m, d, h, file_name))

    relationships = curr_relationships
    with open(file_name) as f:
        for l in f:
            log = json.loads(l)
            judgment = parse_judgement(log)
            if judgment is not None:
                (criticUserId, candidateUserId, liked, scene) = judgment
                relationships[criticUserId][candidateUserId][scene] = liked

    # write our new JSON file for this hour
    graph = {}
    graph['nodes'] = []
    graph['edges'] = []
    for critic in range(MAX_USER_ID):
        for candidate in range(MAX_USER_ID):
            smash = relationships[critic][candidate]['smash']
            social = relationships[critic][candidate]['social']
            stone = relationships[critic][candidate]['stone']
            if smash or social or stone:
                graph['edges'].append({
                    'critic': critic,
                    'candidate': candidate,
                    'scenes': {
                        'smash': smash,
                        "social": social,
                        "stone": stone
                    }
                })

    dumpJsonToFile(graph, m, d, h)
    return relationships


empty_relationship = [[{'smash': False, 'stone': False, 'social': False}
                       for i in range(MAX_USER_ID)] for j in range(MAX_USER_ID)]
total_logs = reduce_logs(
    (lambda acc, log_file:
        gen_hour_relationships(log_file, acc)),
    empty_relationship)
