import nltk, math, six
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem.porter import *
import plotly.plotly as py
import plotly.graph_objs as go
from operator import itemgetter, attrgetter

stemmer = PorterStemmer()

answer_set = open('pitch_corpus')
answer_set = answer_set.read()

Dropbox_answers = dict()
Dropbox_answers['name'] = 'Dropbox'
Dropbox_answers[
    'tagline'] = 'Dropbox is a technology company that builds simple, powerful products for people and businesses.(https://www.ycombinator.com/apply/dropbox/)'
Dropbox_answers[
    'model'] = 'freemium approach: where we give away free 1GB accounts and charge for additional storage (maybe 5/mo or less for 10GB for individuals and team plans that start at maybe $20/mo.). It’s hard to get consumers to pay for things, but fortunately small/medium businesses already pay for solutions that are subsets of what Dropbox does and are harder to use. There will be tiered pricing for business accounts (upper tiers will retain more older versions of documents, have branded extranets for secure file sharing with clients/partners, etc., and an ‘enterprise’ plan that features, well, a really high price.)I’ve already been approached by potential partners/customers asking for a web services API to programmatically create Dropboxes (e.g. to handle file sharing for Assembla.com, a web site for managing global dev teams). There’s a natural synergy between project mgmt/groupware web apps (which do to-do lists, calendaring, etc. well but not files) and Dropbox for file sharing. I’ve also had requests for an enterprise version that would sit on a company’s network (as opposed to my S3 store) for which I could probably charge a lot.(https://www.ycombinator.com/apply/dropbox/)'
Dropbox_answers[
    'KPI'] = 'Total number of users of your app - The number of new users your app gains each day - The number of API calls your app makes each day.(https://blogs.dropbox.com/developers/2014/06/announcing-dropbox-app-metrics/)'
Dropbox_answers['revenue'] = 0
Dropbox_answers['cofnum'] = 1
Dropbox_answers['employee'] = 3
Dropbox_answers['goal'] = 15000


def getIdfs(file):
    idfs = dict()
    sentenceNumber = 0
    file = file.splitlines()
    for line in file:
        for sentence in sent_tokenize(line):
            ws = [stemmer.stem(w.lower()) for w in word_tokenize(sentence)]
            sentenceNumber += 1
            for wlower in set(ws):
                if wlower in idfs:
                    idfs[wlower] += 1
                else:
                    idfs[wlower] = 1
    for w in idfs:
        idfs[w] = 1 + math.log(sentenceNumber / idfs[w])
    return idfs


idfDict = getIdfs(answer_set)


def similarity(s1, s2, idfDict):
    a = set(s1)
    s1 = set([stemmer.stem(w.lower()) for w in word_tokenize(s1)])
    s2 = set([stemmer.stem(w.lower()) for w in word_tokenize(s2)])
    a = s1.union(s2)
    s1d = dict()
    s2d = dict()
    for w in s1:
        if w in s1d:
            s1d[w] += 1
        else:
            s1d[w] = 1
    for w in s2:
        if w in s2d:
            s2d[w] += 1
        else:
            s2d[w] = 1
    for w in a:
        if w not in s1d:
            s1d[w] = 0
        if w not in s2d:
            s2d[w] = 0
    s1tf = dict()
    s2tf = dict()
    for w in s1d:
        s1tf[w] = s1d[w] / len(s1)
    for w in s2d:
        s2tf[w] = s2d[w] / len(s2)
    s1idf = dict()
    s2idf = dict()
    for w in a:
        # print(idfDict[w.lower()],idfDict[w.lower()])
        s1idf[w] = idfDict.get(w.lower(), 0)
        s2idf[w] = idfDict.get(w.lower(), 0)
    for w in a:
        s1d[w] = s1tf[w] * s1idf[w]
        s2d[w] = s2tf[w] * s2idf[w]
    # print(s1d,s2d)
    dotProd = 0
    norm1 = 0
    norm2 = 0
    for key in s1d:
        dotProd += s1d[key] * s2d[key]
        norm1 += s1d[key] ** 2
        norm2 += s2d[key] ** 2
    if norm1 * norm2 == 0:
        return 0
    return dotProd / (math.sqrt(norm1) * math.sqrt(norm2))


def compareAnswers(answer1, answer2):
    sim = similarity(answer1, answer2, idfDict)
    return math.sqrt(sim * 100) * 10


def uniqueness(this_answer, answers):
    sims = []
    for ans in answers:
        sims.append((ans[0], compareAnswers(this_answer, ans[0])))
    return sims


def extract(model_keywords, answer):
    res = []
    for w in model_keywords:
        if w in answer:
            res.append(w)
    return res


c1 = {'name': 'c1', 'tagline': 'I have a dream'}
c2 = {'name': 'c2', 'tagline': 'i want a tech company'}
simcomps = [c1, c2]

revmodkeys = ['freemium', 'ads']


def companyOverview(company, similar_companies):
    # entries 'tagline' 'model' 'KPI' 'revenue' 'cofnum' 'employee' 'goal'
    # How unique is this company's mission?
    companies_taglines = [x['tagline'] for x in similar_companies]
    unique = str(sum([x[1] for x in uniqueness(company['tagline'], companies_taglines)]) / len(similar_companies))
    model = " ".join(extract(revmodkeys, company['model']))
    KPI = company['KPI']
    revenue = str(company['revenue'])
    cofounder_number = str(company['cofnum'])
    employeenum = str(company['employee'])
    goal = str(company['goal'])
    feature_list = [unique, model, KPI, revenue, cofounder_number, employeenum, goal]

    # uniquenes, revenue model keywords, KPI, revenue, cofounder numebr, employee number, goal amount of money
    res = "\n".join(feature_list)
    return res


print(companyOverview(Dropbox_answers, simcomps))


def similarityList(company, companies):
    taglines = [comp['tagline'] for comp in companies]
    company_tuples = []  # tagline, similarity
    for com in companies:
        company_tuples.append((com, similarity(company['tagline'], com['tagline'], idfDict)))
    ans = sorted(company_tuples, key=itemgetter(1), reverse=False)
    # print(ans[0])
    line_out = [(ct[0]['name'] + " " + str(round(ct[1]))) for ct in ans]
    str_out = "\n".join(line_out)
    return str_out


print(similarityList(Dropbox_answers, simcomps))


def heatMapInfo(company, companies):
    return 0
