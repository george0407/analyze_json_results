import json
import numpy as np
from collections import defaultdict

def analize_rating():
    with open('trivial/rating.json') as f:
        rating = json.load(f)
    naiyan = rating["naiyan"]
    zehao = rating["zehao"]
    hongyang = rating["hongyang"]
    # calculate the average rating
    avg_results = {}
    for key in naiyan.keys():
        avg_results[key] = (naiyan[key] + zehao[key] + hongyang[key]) / 3
    # calculate the standard deviation
    std_results = {}
    for key in naiyan.keys():
        std_results[key] = np.std([naiyan[key], zehao[key], hongyang[key]])
    # print the results
    print("Average rating:")
    print(avg_results)
    print("Standard deviation:")
    print(std_results)
    
    # with open('trivial/avg_rating.json', 'w') as f:
    #     json.dump(avg_results, f)
    # with open('trivial/std_rating.json', 'w') as f:
    #     json.dump(std_results, f)
    # dump sorted results in reverse order
    sorted_avg_results = dict(sorted(avg_results.items(), key=lambda x: x[1], reverse=True))
    # with open('trivial/sorted_avg_rating.json', 'w') as f:
    #     json.dump(sorted_avg_results, f)
    sorted_std_results = dict(sorted(std_results.items(), key=lambda x: x[1], reverse=True))
    # with open('trivial/sorted_std_rating.json', 'w') as f:
    #     json.dump(sorted_std_results, f)
    
    final_results = {}
    for key in sorted_std_results.keys():
        final_results[key] = defaultdict(dict)
        final_results[key]["std"] = round(sorted_std_results[key], 2)
        final_results[key]["avg"] = round(sorted_avg_results[key], 2)
        final_results[key]["naiyan"] = naiyan[key]
        final_results[key]["zehao"] = zehao[key]
        final_results[key]["hongyang"] = hongyang[key]
    with open('trivial/final_rating.json', 'w') as f:
        json.dump(final_results, f)
        


if __name__ == '__main__':
    analize_rating()