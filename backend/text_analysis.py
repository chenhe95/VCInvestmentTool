#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, KeywordsOptions, EntitiesOptions, SemanticRolesOptions, ConceptsOptions, CategoriesOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='4c5e2617-b877-401b-916c-e8eea8ab6309',
  password='lQqL2lyFSukU',
  version='2017-02-27')

text = u'Using generative design, virtual reality, 3D printing, and a cloud-based supply chain, Hackrod is challenging the traditional approach to automobile manufacturing. The company is developing a methodology that will enable the rapid prototyping of bespoke vehicle solutions and will place the consumer as co-creator in the automotive space. Beginning with the film “Autonomo,” where Hackrod aims to showcase its vehicles and then offer the designs as templates to customers, Hackrod’s design and manufacturing engine will feature engineering analysis and performance simulation and well as supply chain management, ordering, and hardware integration. Hackrod currently has a partnership with AutoDesk to create virtual car prototypes using the Autodesk VRED 3D visualization and virtual prototyping software.'

response = natural_language_understanding.analyze(
  text=text,
    features=Features(
    keywords=KeywordsOptions(
      sentiment=True,
      emotion=True,
      limit=2)))

print(json.dumps(response, indent=2))


response = natural_language_understanding.analyze(
  text=text,
  features=Features(
    entities=EntitiesOptions(
      sentiment=True,
      limit=1)))

print(json.dumps(response, indent=2))

response = natural_language_understanding.analyze(
  text=text,
  features=Features(
    semantic_roles=SemanticRolesOptions()))

print(json.dumps(response, indent=2))

response = natural_language_understanding.analyze(
  url='www.ibm.com',
  features=Features(
    concepts=ConceptsOptions(
      limit=3)))

print(json.dumps(response, indent=2))

response = natural_language_understanding.analyze(
  url='www.ibm.com',
  features=Features(
    categories=CategoriesOptions()))

print(json.dumps(response, indent=2))