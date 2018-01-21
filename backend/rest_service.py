from flask import Flask
import json
import pymongo
from pymongo import MongoClient
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, KeywordsOptions, EntitiesOptions, SemanticRolesOptions, ConceptsOptions, CategoriesOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='4c5e2617-b877-401b-916c-e8eea8ab6309',
  password='lQqL2lyFSukU',
  version='2017-02-27')
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

def get_keywords_entities(text):
	keywords_json = natural_language_understanding.analyze(
		text=text,
		features=Features(
			keywords=KeywordsOptions(
				sentiment=True,
				emotion=True,
				limit=2)))

	entities_json = natural_language_understanding.analyze(
		text=text,
		features=Features(
			entities=EntitiesOptions(
				sentiment=True,
				limit=1)))

	return keywords_json, entities_json

@app.route('/startup_registration', methods=['GET', 'POST'])
def startup_registration():
	j = json.loads(request.data)
	name = j["0"] 
	logo = j["1"]
	tagline = j["2"]
	business_model = j["3"]
	kpi = j["4"]
	money_made = j["5"]
	num_founder = j["6"]
	num_employees = j["7"]
	num_money_planning_to_raise = j["8"]
	k1, e1 = get_keywords_entities(tagline)
	k2, e2 = get_keywords_entities(business_model)
	client = MongoClient()
	igmm_db = client.startups.saved

	igmm_db.insert({"company_name": name, "company_logo": logo, "tagline": tagline,
		"business_model": business_model, "kpi": kpi, "money_made":money_made, 
		"num_founder": num_founder, "num_employees":num_employees, 
		"num_money_planning_to_raise":num_money_planning_to_raise,
		"keywords_tagline": k1, "entity_tagline": e1,
		"keywords_business": k2, "entity_business": e2});
	return request.data


@app.route('/company_digest/<string:name>')
def new_question_posted(name):
	client = MongoClient()
	db = client.startups.test
	db.insert({"aaa":"qwer", "bbb":"111"})
	return "HELLO " + name

if __name__ == "__main__":
    app.run(debug=True)