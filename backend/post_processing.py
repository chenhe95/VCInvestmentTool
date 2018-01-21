import nltk,math,six
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
Dropbox_answers['tagline'] = 'Dropbox is a technology company that builds simple, powerful products for people and businesses.(https://www.ycombinator.com/apply/dropbox/)'
Dropbox_answers['model'] = 'freemium approach: where we give away free 1GB accounts and charge for additional storage (maybe 5/mo or less for 10GB for individuals and team plans that start at maybe $20/mo.). It\'s hard to get consumers to pay for things, but fortunately small/medium businesses already pay for solutions that are subsets of what Dropbox does and are harder to use. There will be tiered pricing for business accounts (upper tiers will retain more older versions of documents, have branded extranets for secure file sharing with clients/partners, etc., and an \'enterprise\' plan that features, well, a really high price.)I\'ve already been approached by potential partners/customers asking for a web services API to programmatically create Dropboxes (e.g. to handle file sharing for Assembla.com, a web site for managing global dev teams). There\'s a natural synergy between project mgmt/groupware web apps (which do to-do lists, calendaring, etc. well but not files) and Dropbox for file sharing. I\'ve also had requests for an enterprise version that would sit on a company\'s network (as opposed to my S3 store) for which I could probably charge a lot.(https://www.ycombinator.com/apply/dropbox/)'
Dropbox_answers['KPI'] = 'Total number of users of your app - The number of new users your app gains each day - The number of API calls your app makes each day.(https://blogs.dropbox.com/developers/2014/06/announcing-dropbox-app-metrics/)'
Dropbox_answers['revenue'] = 0
Dropbox_answers['cofnum'] = 1
Dropbox_answers['employee'] = 3 
Dropbox_answers['goal'] = 15000

Reddit_answers = dict()
Reddit_answers['name'] = 'Redbrick Solutions, LLC'
Reddit_answers['tagline'] = 'We are going to build an infrastructure that will allow consumers to order food from their cell phones (via a text-interface, rather than voice), drive to the restaurant and pick up their order'
Reddit_answers['model'] = 'We will make money by charging a percentage commission on every order made through our service. Our business model is B2B, and our business clients will be restaurants.'
Reddit_answers['KPI'] = 'restaurants signed up - users on the app'
Reddit_answers['revenue'] = 0
Reddit_answers['cofnum'] = 3
Reddit_answers['employee'] = 0
Reddit_answers['goal'] = 100000
# print(Reddit_answers)

TheMuse_answers = dict()
TheMuse_answers['name'] = 'The Daily Muse'
TheMuse_answers['tagline'] = 'The Daily Muse is building a massive community of job-seeking women to rival The Ladders.'
TheMuse_answers['model'] = 'In addition to pay-to-post career opportunities, we offer smart content and soon to be launched professional development courses'
TheMuse_answers['KPI'] = 'users - companies'
TheMuse_answers['revenue'] = 50000
TheMuse_answers['cofnum'] = 3
TheMuse_answers['employee'] = 0
TheMuse_answers['goal'] = 1200000
# print(TheMuse_answers)

OneMonth_answers = dict()
OneMonth_answers['name'] = 'One Month Rails'
OneMonth_answers['tagline'] = 'A 30-day online crash course in web development.'
OneMonth_answers['model'] = 'In addition to pay-to-post career opportunities, we offer smart content and soon to be launched professional development courses'
OneMonth_answers['KPI'] = 'users '
OneMonth_answers['revenue'] = 6000
OneMonth_answers['cofnum'] = 1
OneMonth_answers['employee'] = 0
OneMonth_answers['goal'] = 14000
# print(OneMonth_answers)

Makegameswithus_answers = dict()
Makegameswithus_answers['name'] = 'Make Games with Us'
Makegameswithus_answers['tagline'] = 'We will build a matchmaking website that allows engineers and artists to make mobile games together.'
Makegameswithus_answers['model'] = 'We will make money by taking a portion of the revenue from the games we publish.'
Makegameswithus_answers['KPI'] = 'artists - engineers - apps'
Makegameswithus_answers['revenue'] = 0
Makegameswithus_answers['cofnum'] = 2
Makegameswithus_answers['employee'] = 0
Makegameswithus_answers['goal'] = 0
# print(Makegameswithus_answers)

simcomps = [Dropbox_answers,Reddit_answers,TheMuse_answers,OneMonth_answers,Makegameswithus_answers]

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

def similarity(s1,s2,idfDict):
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
        s1tf[w] = s1d[w]/len(s1)
    for w in s2d:
        s2tf[w] = s2d[w]/len(s2)
    s1idf = dict()
    s2idf = dict()
    for w in a:
        # print(idfDict[w.lower()],idfDict[w.lower()])
        s1idf[w] = idfDict.get(w.lower(),0)
        s2idf[w] = idfDict.get(w.lower(),0)
    for w in a:
        s1d[w] = s1tf[w] * s1idf[w]
        s2d[w] = s2tf[w] * s2idf[w]
    # print(s1d,s2d)
    dotProd = 0
    norm1 = 0
    norm2 = 0
    for key in s1d:
        dotProd += s1d[key]*s2d[key]
        norm1 +=  s1d[key]**2
        norm2 +=  s2d[key]**2
    if norm1*norm2 == 0:
        return 0
    return dotProd/(math.sqrt(norm1)*math.sqrt(norm2))

def compareAnswers(answer1, answer2):
    sim = similarity(answer1,answer2,idfDict)
    return math.sqrt(sim*100)*10

def uniqueness(this_answer, answers):
    sims = []
    for ans in answers:
        sims.append((ans[0], compareAnswers(this_answer, ans[0])))
    return sims

def extract(model_keywords,answer):
    res = []
    for w in model_keywords:
        if w in answer:
            res.append(w)
    return res

# c1 = {'name':'c1','tagline':'I have a dream'}
# c2 = {'name':'c2','tagline':'i want a tech company'}


revmodkeys = ['freemium','ads','pay per click', 'ppc', 'cost per impression', 'cpi','cpm','advertising','affiliate promotion paid membership sites product sales']
def companyOverview(company, similar_companies):
    # entries 'tagline' 'model' 'KPI' 'revenue' 'cofnum' 'employee' 'goal'
    # How unique is this company's mission?
    companies_taglines = [x['tagline'] for x in similar_companies]
    unique = str(sum([x[1] for x in uniqueness(company['tagline'], companies_taglines)])/len(similar_companies))
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
print(companyOverview(Reddit_answers,simcomps))

def similarityList(company, companies):
    taglines = [comp['tagline'] for comp in companies]
    company_tuples = [] # tagline, similarity
    for com in companies:
        company_tuples.append((com, similarity(company['tagline'], com['tagline'], idfDict)))
    ans = sorted(company_tuples, key=itemgetter(1), reverse=False)
    # print(ans[0])
    line_out = [(ct[0]['name'] +" "+str(round(ct[1])))for ct in ans]
    str_out = "\n".join(line_out)
    return str_out
print(similarityList(Reddit_answers, simcomps))


suggestedNum = 5
quantitativeFeatures = 5

def rescale(v):
    minimum = min(v)
    maximum = max(v)
    res = []
    for value in v:
        res.append((value - minimum)/maximum * 100)
    return res

def heatMapInfo(companies):
    uniqueV = []
    revenueV = [company['revenue'] for company in companies]
    cofnumV = [company['confnum'] for company in companies]
    empV = [company['employee'] for company in companies]
    goalV = [company['goal'] for company in companies]
    companies_taglines = [x['tagline'] for x in companies]
    for company in companies:
        uniqueV.append(sum([x[1] for x in uniqueness(company['tagline'], companies_taglines)])/len(companies))
    mat = [uniqueV,revenueV, cofnumV,empV,goalV]
    colorShades = []
    for v in mat:
        colorShades.append(rescale(v))
    rowLable = [company['name'] for company in companies]
    return mat, colorShades, rowLable

print(heatMapInfo(simcomps))