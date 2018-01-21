from flask import Flask
from flask import request
import json
import pymongo
import random
from pymongo import MongoClient
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, KeywordsOptions, EntitiesOptions, SemanticRolesOptions, ConceptsOptions, CategoriesOptions
from flask_cors import CORS



natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='4c5e2617-b877-401b-916c-e8eea8ab6309',
  password='lQqL2lyFSukU',
  version='2017-02-27')
app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})


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
	print "Received startup registration ", request
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
	k1, e1, k2, e2 = json.loads("{}"), json.loads("{}"), json.loads("{}"), json.loads("{}")
	try:
		k1, e1 = get_keywords_entities(tagline)
		k2, e2 = get_keywords_entities(business_model)
	except:
		pass
	client = MongoClient()
	igmm_db = client.startups.saved

	# TODO
	uniqueness = random.uniform(0.0, 1.0)
	print "Saving to MongoDB"
	igmm_db.insert({"company_name": name, "company_logo": logo, "tagline": tagline,
		"business_model": business_model, "kpi": kpi, "money_made":money_made, 
		"num_founder": num_founder, "num_employees":num_employees, 
		"num_money_planning_to_raise":num_money_planning_to_raise,
		"keywords_tagline": k1, "entity_tagline": e1,
		"keywords_business": k2, "entity_business": e2, "uniqueness": uniqueness,
		"cid":str(id(name))});

	return request.data

def company_dict_to_json(company):
	if not company:
		return json.loads("{}")
	j = json.loads("{}")
	j["name"] = company["company_name"]
	j["id"] = company["cid"]
	j["logo"] = company["company_logo"]
	j["tags"] = []
	try:
		kw_tagline = [x["text"] for x in company["keywords_tagline"]["keywords"]]
		kw_business = [x["text"] for x in company["keywords_business"]["keywords"]]
		e_tagline = [x["text"] for x in company["entity_tagline"]["entities"]]
		e_business = [x["text"] for x in company["entity_tagline"]["entities"]]
		kw = list(set(kw_tagline + kw_business + e_tagline + e_business))
		j["tags"] = kw
	except:
		pass
	j["uniqueness"] = company["uniqueness"]
	j["revenue"] = company["money_made"]
	j["founder"] = company["num_founder"]
	j["employees"] = company["num_employees"]
	j["tagline"] = company["tagline"]
	j["model"] = company["business_model"]
	j["responses"] = []
	return j


def company_dict_to_json_str(company):
	return json.dumps(company_dict_to_json(company))

@app.route('/company_digest/<string:cid>')
def company_digest(cid):
	print "Company digest route"
	client = MongoClient()
	db = client.startups.saved
	company = None
	for i in db.find({"cid": cid}):
		company = i
		break
	return company_dict_to_json_str(company)

@app.route('/company_all_digest')
def company_all_digest():
	print "Company digest route"
	client = MongoClient()
	db = client.startups.saved
	company_json_strs = []
	for i in db.find():
		company_json_strs.append(company_dict_to_json(i))

	return json.dumps(company_json_strs)


if __name__ == "__main__":
    app.run(debug=True)