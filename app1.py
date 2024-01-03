######################################flask app##################

import spacy
from flask import Flask, jsonify
import re, json

app = Flask(__name__)

with open(r'D:\projects intellipaat\mobiNLP\nitin verma.txt', 'r', encoding='utf-8') as f :
    input_text = f.read()

# print(input_text)

json_file_path = 'court_name.json'  # Replace 'your_file_name.json' with the actual file name

with open(json_file_path, 'r') as file:
    data = json.load(file)


@app.route('/result')
def process_data():
    # if request.method == 'POST';
    def dates(input_text):
        date_pattern = r'[\b\d{2}[./-]\d{2}[./-]\d{4}\b]'
        date_pattern = re.compile(r'\b(?:january|february|march|april|may|june|july|august|september|october|november|december)\s\d{1,2},?\s\d{4}\b', flags=re.IGNORECASE)

        dates_found = date_pattern.findall(input_text)
        return dates_found


    def name_of_court(input_text):
        court_name_pattern = re.compile(r'in the (high court of [^\n]+)')

        court_name = court_name_pattern.search(input_text.lower())
        court_name = " ".join(court_name[0].split())
        if court_name:
            return court_name
        else:
            return None



    def get_citation(text):
        try:
            citation_pattern = re.compile(r'\b\d{4}-\w+-\d{1,5}-\w+-\w{3,}-\w+\b')
            citation_match = citation_pattern.search(text)
            
            if citation_match:
                return citation_match.group(0)
            else:
                return None

        except Exception as e:
            return str(e)


    


    citation = get_citation(input_text) 
    court_name = name_of_court(input_text=input_text)
    dates_found = dates(input_text)

    def features(citation):
        court_name = citation.split('-')[-3]
        domain_name = citation.split('-')[-1]
        assesment_year = citation.split('-')[0]

        for i in data[0].keys():
            if citation.split('-')[-2] == i:
                bench_type = data[0][i]
            else:
                pass

        # Handle cases where values are empty or not found
        court_name = court_name if court_name else None
        domain_name = domain_name if domain_name else None
        assesment_year = assesment_year if assesment_year else None
        bench_type = bench_type if bench_type else None

        return court_name, domain_name, assesment_year, bench_type

    court, domain_name, assesment_year, bench_type = features(citation)



    def app_resp(input_text):
        input_text = input_text.lower()

        appellant_pattern = re.compile(r'appellant rep by: (.*?)(?=\n|$)')
        respondent_pattern = re.compile(r'respondent rep by:(.*?)(?=\n|$)')
        appellant = " ".join(appellant_pattern.findall(input_text))
        respondent = " ".join(respondent_pattern.findall(input_text))

        appellant = appellant if appellant else None
        respondent = respondent if respondent else None

        return appellant, respondent
    
    appellant, respondent = app_resp(input_text)

    # Create a dictionary with the results
    result_dict = {
        "court_name": court_name,
        "order_dates": " ".join(dates_found),
        "citation_number": citation,
        "court": court,
        "domain_name": domain_name,
        "assessment_year": assesment_year,
        "bench_type": bench_type,
        "appellant_name" : appellant,
        "respondent_name" : respondent
    }

    return jsonify(result_dict)



if __name__ == '__main__':
    app.run(debug=True)
