
#load and parse json and target file

import json
import re

#load patterns from json file

def load_patterns(json_file):
    with open(json_file,'r') as file:
        patterns = json.load(file)
    return patterns['patterns']

#load target file line by line

def load_target_file(file_path):
    with open(file_path,'r') as file:
        lines = file.readlines()
    return lines

#implementing pattern matching

def check_patterns(patterns,target_lines):
    matches=[]
    #check_pattern_count = 0

    for pattern in patterns:
        if 'regex' in pattern:
            regex_list=pattern['regex']
            all_matched = True
            for regex_pattern in regex_list:
                regex = re.compile(regex_pattern)

                #check if the regex mathces any line

                if not any(regex.search(line) for line in target_lines):
                    all_matched = False
                    break

            if all_matched:
                #print(f"printing {check_pattern_count} iteration of matched pattern ")
                #print(matches)
                #check_pattern_count = check_pattern_count + 1
                matches.append({
                    "pattern_name":pattern['name'],
                    "matched_regexes": regex_list
                })
    return matches

#outputing the results

def main():
    patterns_file = 'Example 1\patterns.json'
    target_file = 'Example 1\Targetfile.txt'
    output_json_file = 'Example 1\Detected_Patterns.json'

    #Load patterns and Target Data

    patterns = load_patterns(patterns_file)
    target_lines = load_target_file(target_file)

    #print("printing patterns ....")
    #print(patterns)

    #print("printing target file lines.....")
    #print(target_lines)

    #check for patterns:
    
    matches = check_patterns(patterns,target_lines)

    #formating and intending the data to dump on json

    with open(output_json_file, 'w') as file:
        json.dump(matches,file,indent=2)

    print("printing matched patterns...")
    print(matches)


    if matches:
        print(f"Found {len(matches)} matching patterns:")
        for match in matches:
            print(f"Pattern Name: {match['pattern_name']}")

            if 'matched_regexes' in match:
                print(f"All regexes matched : {match['matched_regexes']}")
            else:
                print("no patterns matched")

    

if __name__ == "__main__":
    main()