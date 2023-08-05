#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2022-07-13.
#  2022, SMART Health IT.

import io
import json
import logging
import os
import typing
import unittest

from . import measure

from .fhirdate import FHIRDate
import logging


class MeasureTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Measure", js["resourceType"])
        return measure.Measure(js)
    
    def testMeasure1(self):
        inst = self.instantiate_from("measure-component-b-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Measure instance")
        self.implMeasure1(inst)
        
        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure1(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implMeasure1(self, inst):
        self.assertEqual(inst.group[0].id, "Main")
        self.assertEqual(inst.group[0].population[0].code.coding[0].code, "initial-population")
        self.assertEqual(inst.group[0].population[0].criteria.expression, "Initial Population")
        self.assertEqual(inst.group[0].population[0].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].population[1].code.coding[0].code, "denominator")
        self.assertEqual(inst.group[0].population[1].criteria.expression, "Denominator")
        self.assertEqual(inst.group[0].population[1].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].population[2].code.coding[0].code, "numerator")
        self.assertEqual(inst.group[0].population[2].criteria.expression, "Numerator")
        self.assertEqual(inst.group[0].population[2].criteria.language, "text/cql")
        self.assertEqual(inst.id, "component-b-example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.scoring.coding[0].code, "proportion")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Screening for Depression")
    
    def testMeasure2(self):
        inst = self.instantiate_from("measure-predecessor-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Measure instance")
        self.implMeasure2(inst)
        
        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure2(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implMeasure2(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2014-03-08").date)
        self.assertEqual(inst.date.as_json(), "2014-03-08")
        self.assertEqual(inst.description, "Exclusive breastfeeding measure of outcomes for exclusive breastmilk feeding of newborns.")
        self.assertEqual(inst.group[0].id, "PopulationGroup1")
        self.assertEqual(inst.group[0].population[0].code.coding[0].code, "initial-population")
        self.assertEqual(inst.group[0].population[0].criteria.expression, "InitialPopulation1")
        self.assertEqual(inst.group[0].population[0].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].population[1].code.coding[0].code, "denominator")
        self.assertEqual(inst.group[0].population[1].criteria.expression, "Denominator1")
        self.assertEqual(inst.group[0].population[1].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].population[2].code.coding[0].code, "denominator-exclusions")
        self.assertEqual(inst.group[0].population[2].criteria.expression, "DenominatorExclusions1")
        self.assertEqual(inst.group[0].population[2].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].population[3].code.coding[0].code, "numerator")
        self.assertEqual(inst.group[0].population[3].criteria.expression, "Numerator1")
        self.assertEqual(inst.group[0].population[3].criteria.language, "text/cql")
        self.assertEqual(inst.group[1].id, "PopulationGroup2")
        self.assertEqual(inst.group[1].population[0].code.coding[0].code, "initial-population")
        self.assertEqual(inst.group[1].population[0].criteria.expression, "InitialPopulation2")
        self.assertEqual(inst.group[1].population[0].criteria.language, "text/cql")
        self.assertEqual(inst.group[1].population[1].code.coding[0].code, "denominator")
        self.assertEqual(inst.group[1].population[1].criteria.expression, "Denominator2")
        self.assertEqual(inst.group[1].population[1].criteria.language, "text/cql")
        self.assertEqual(inst.group[1].population[2].code.coding[0].code, "denominator-exclusion")
        self.assertEqual(inst.group[1].population[2].criteria.expression, "DenominatorExclusions2")
        self.assertEqual(inst.group[1].population[2].criteria.language, "text/cql")
        self.assertEqual(inst.group[1].population[3].code.coding[0].code, "numerator")
        self.assertEqual(inst.group[1].population[3].criteria.expression, "Numerator2")
        self.assertEqual(inst.group[1].population[3].criteria.language, "text/cql")
        self.assertEqual(inst.id, "measure-predecessor-example")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "exclusive-breastfeeding-measure")
        self.assertEqual(inst.improvementNotation.coding[0].code, "increase")
        self.assertEqual(inst.improvementNotation.coding[0].system, "http://terminology.hl7.org/CodeSystem/measure-improvement-notation")
        self.assertEqual(inst.library[0], "Library/library-exclusive-breastfeeding-cqm-logic")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.purpose, "Measure of newborns who were fed breast milk only since birth")
        self.assertEqual(inst.relatedArtifact[0].citation, "American Academy of Pediatrics. (2005). Section on Breastfeeding. Policy Statement:Breastfeeding and the Use of Human Milk. Pediatrics.115:496-506.")
        self.assertEqual(inst.relatedArtifact[0].type, "documentation")
        self.assertEqual(inst.relatedArtifact[1].type, "documentation")
        self.assertEqual(inst.relatedArtifact[2].type, "documentation")
        self.assertEqual(inst.relatedArtifact[3].type, "documentation")
        self.assertEqual(inst.relatedArtifact[4].type, "documentation")
        self.assertEqual(inst.relatedArtifact[5].type, "documentation")
        self.assertEqual(inst.relatedArtifact[6].citation, "Kramer, M.S. & Kakuma, R. (2002).Optimal duration of exclusive breastfeeding. [107 refs] Cochrane Database of Systematic Reviews. (1):CD003517.")
        self.assertEqual(inst.relatedArtifact[6].type, "documentation")
        self.assertEqual(inst.relatedArtifact[7].citation, "Petrova, A., Hegyi, T., & Mehta, R. (2007). Maternal race/ethnicity and one-month exclusive breastfeeding in association with the in-hospital feeding modality. Breastfeeding Medicine. 2(2):92-8.")
        self.assertEqual(inst.relatedArtifact[7].type, "documentation")
        self.assertEqual(inst.relatedArtifact[8].type, "documentation")
        self.assertEqual(inst.relatedArtifact[9].type, "documentation")
        self.assertEqual(inst.scoring.coding[0].code, "proportion")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Exclusive Breastfeeding Measure")
        self.assertEqual(inst.topic[0].text, "Exclusive Breastfeeding")
        self.assertEqual(inst.type[0].coding[0].code, "process")
        self.assertEqual(inst.version, "4.0.1")
    
    def testMeasure3(self):
        inst = self.instantiate_from("measure-cms146-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Measure instance")
        self.implMeasure3(inst)
        
        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure3(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implMeasure3(self, inst):
        self.assertEqual(inst.approvalDate.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.approvalDate.as_json(), "2016-01-01")
        self.assertEqual(inst.author[0].name, "National Committee for Quality Assurance")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://www.ncqa.org/")
        self.assertEqual(inst.date.date, FHIRDate("2017-03-10").date)
        self.assertEqual(inst.date.as_json(), "2017-03-10")
        self.assertEqual(inst.description, "Percentage of children 3-18 years of age who were diagnosed with pharyngitis, ordered an antibiotic and received a group A streptococcus (strep) test for the episode.")
        self.assertEqual(inst.effectivePeriod.end.date, FHIRDate("2017-12-31").date)
        self.assertEqual(inst.effectivePeriod.end.as_json(), "2017-12-31")
        self.assertEqual(inst.effectivePeriod.start.date, FHIRDate("2017-01-01").date)
        self.assertEqual(inst.effectivePeriod.start.as_json(), "2017-01-01")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.group[0].id, "CMS146-group-1")
        self.assertEqual(inst.group[0].population[0].code.coding[0].code, "initial-population")
        self.assertEqual(inst.group[0].population[0].criteria.expression, "CMS146.InInitialPopulation")
        self.assertEqual(inst.group[0].population[0].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].population[1].code.coding[0].code, "numerator")
        self.assertEqual(inst.group[0].population[1].criteria.expression, "CMS146.InNumerator")
        self.assertEqual(inst.group[0].population[1].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].population[2].code.coding[0].code, "denominator")
        self.assertEqual(inst.group[0].population[2].criteria.expression, "CMS146.InDenominator")
        self.assertEqual(inst.group[0].population[2].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].population[3].code.coding[0].code, "denominator-exclusion")
        self.assertEqual(inst.group[0].population[3].criteria.expression, "CMS146.InDenominatorExclusions")
        self.assertEqual(inst.group[0].population[3].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].stratifier[0].code.text, "stratifier-ages-up-to-9")
        self.assertEqual(inst.group[0].stratifier[0].criteria.expression, "CMS146.AgesUpToNine")
        self.assertEqual(inst.group[0].stratifier[0].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].stratifier[1].code.text, "stratifier-ages-10-plus")
        self.assertEqual(inst.group[0].stratifier[1].criteria.expression, "CMS146.AgesTenPlus")
        self.assertEqual(inst.group[0].stratifier[1].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].stratifier[2].code.text, "stratifier-gender")
        self.assertEqual(inst.group[0].stratifier[2].criteria.expression, "Patient.gender")
        self.assertEqual(inst.group[0].stratifier[2].criteria.language, "text/fhirpath")
        self.assertEqual(inst.guidance, "This is an episode of care measure that examines all eligible episodes for the patient during the measurement period. If the patient has more than one episode, include all episodes in the measure")
        self.assertEqual(inst.id, "measure-cms146-example")
        self.assertEqual(inst.identifier[0].system, "http://hl7.org/fhir/cqi/ecqm/Measure/Identifier/cms")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "146")
        self.assertEqual(inst.identifier[1].system, "http://hl7.org/fhir/cqi/ecqm/Measure/Identifier/nqf")
        self.assertEqual(inst.identifier[1].use, "official")
        self.assertEqual(inst.identifier[1].value, "0002")
        self.assertEqual(inst.improvementNotation.coding[0].code, "increase")
        self.assertEqual(inst.improvementNotation.coding[0].system, "http://terminology.hl7.org/CodeSystem/measure-improvement-notation")
        self.assertEqual(inst.jurisdiction[0].coding[0].code, "US")
        self.assertEqual(inst.jurisdiction[0].coding[0].system, "urn:iso:std:iso:3166")
        self.assertEqual(inst.lastReviewDate.date, FHIRDate("2016-09-01").date)
        self.assertEqual(inst.lastReviewDate.as_json(), "2016-09-01")
        self.assertEqual(inst.library[0], "Library/library-cms146-example")
        self.assertEqual(inst.name, "CMS146")
        self.assertEqual(inst.publisher, "National Committee for Quality Assurance")
        self.assertEqual(inst.purpose, "Measure of children with a group A streptococcus test in the 7-day period from 3 days prior through 3 days after the diagnosis of pharyngitis")
        self.assertEqual(inst.relatedArtifact[0].citation, "Linder, J.A., D.W. Bates, G.M. Lee, J.A. Finkelstein. 2005. _Antibiotic treatment of children with sore throat._ JAMA 294(18):2315-2322. ")
        self.assertEqual(inst.relatedArtifact[0].type, "documentation")
        self.assertEqual(inst.relatedArtifact[1].citation, "Infectious Diseases Society of America. 2012. _Clinical Practice Guideline for the Diagnosis and Management of Group A Streptococcal Pharyngitis: 2012 Update._ ")
        self.assertEqual(inst.relatedArtifact[1].type, "documentation")
        self.assertEqual(inst.relatedArtifact[2].type, "documentation")
        self.assertEqual(inst.scoring.coding[0].code, "proportion")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.supplementalData[0].code.text, "supplemental-data-gender")
        self.assertEqual(inst.supplementalData[0].criteria.expression, "Patient.gender")
        self.assertEqual(inst.supplementalData[0].criteria.language, "text/fhirpath")
        self.assertEqual(inst.supplementalData[1].code.text, "supplemental-data-deceased")
        self.assertEqual(inst.supplementalData[1].criteria.expression, "deceasedBoolean")
        self.assertEqual(inst.supplementalData[1].criteria.language, "text/fhirpath")
        self.assertEqual(inst.text.status, "additional")
        self.assertEqual(inst.title, "Appropriate Testing for Children with Pharyngitis")
        self.assertEqual(inst.topic[0].coding[0].code, "57024-2")
        self.assertEqual(inst.topic[0].coding[0].system, "http://loinc.org")
        self.assertEqual(inst.type[0].coding[0].code, "process")
        self.assertEqual(inst.url, "http://hl7.org/fhir/Measure/measure-cms146-example")
        self.assertEqual(inst.useContext[0].code.code, "program")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.text, "eligibile-provider")
        self.assertEqual(inst.useContext[1].code.code, "age")
        self.assertEqual(inst.useContext[1].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[1].valueRange.high.unit, "a")
        self.assertEqual(inst.useContext[1].valueRange.high.value, 18)
        self.assertEqual(inst.useContext[1].valueRange.low.unit, "a")
        self.assertEqual(inst.useContext[1].valueRange.low.value, 3)
        self.assertEqual(inst.version, "1.0.0")
    
    def testMeasure4(self):
        inst = self.instantiate_from("measure-component-a-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Measure instance")
        self.implMeasure4(inst)
        
        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure4(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implMeasure4(self, inst):
        self.assertEqual(inst.group[0].id, "Main")
        self.assertEqual(inst.group[0].population[0].code.coding[0].code, "initial-population")
        self.assertEqual(inst.group[0].population[0].criteria.expression, "Initial Population")
        self.assertEqual(inst.group[0].population[0].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].population[1].code.coding[0].code, "denominator")
        self.assertEqual(inst.group[0].population[1].criteria.expression, "Denominator")
        self.assertEqual(inst.group[0].population[1].criteria.language, "text/cql")
        self.assertEqual(inst.group[0].population[2].code.coding[0].code, "numerator")
        self.assertEqual(inst.group[0].population[2].criteria.expression, "Numerator")
        self.assertEqual(inst.group[0].population[2].criteria.language, "text/cql")
        self.assertEqual(inst.id, "component-a-example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.scoring.coding[0].code, "proportion")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Screening for Alcohol Misuse")
    
    def testMeasure5(self):
        inst = self.instantiate_from("measure-composite-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Measure instance")
        self.implMeasure5(inst)
        
        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure5(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implMeasure5(self, inst):
        self.assertEqual(inst.compositeScoring.coding[0].code, "opportunity")
        self.assertEqual(inst.id, "composite-example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.relatedArtifact[0].resource, "Measure/component-a-example")
        self.assertEqual(inst.relatedArtifact[0].type, "composed-of")
        self.assertEqual(inst.relatedArtifact[1].resource, "Measure/component-b-example")
        self.assertEqual(inst.relatedArtifact[1].type, "composed-of")
        self.assertEqual(inst.scoring.coding[0].code, "proportion")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Behavioral Assessment Composite Measure")

    def evaluate_simplified_json(self, inst):
        """Ensure simplified json."""
        simplified_js, simplified_schema = inst.as_simplified_json()
        self.assertIsNotNone(simplified_js, "Must create simplified json")

        # test simplify identifiers
        if hasattr(inst, 'identifier'):
            assert 'identifier' not in simplified_js
            if inst.identifier:
                simplified_identifiers = [k for k in simplified_js.keys() if k.startswith('identifier_')]
                if isinstance(inst.identifier, typing.List):
                    identifiers_with_values = [i for i in inst.identifier if i.value]
                else:
                    identifiers_with_values = [inst.identifier]
                self.assertEqual(len(identifiers_with_values), len(simplified_identifiers), "Should simplify identifiers.")

        # test simplify lists
        for name in vars(inst):

            if name == 'identifier':
                continue

            if name == 'extension':
                continue

            value = getattr(inst, name)

            is_coding = value.__class__.__name__ == 'Coding' or (isinstance(value, typing.List) and len(value) == 1 and value[0].__class__.__name__ == 'Coding')
            if is_coding:
                # why are we skipping Coding test?
                continue

            is_date = 'FHIRDate' in value.__class__.__name__
            if is_date:
                simplified_value_is_date = 'FHIRDate' in simplified_js[name].__class__.__name__
                self.assertFalse(simplified_value_is_date, "Should simplify Date {} {} {}".format(name, value.__class__.__name__, vars(value)) )

            if isinstance(getattr(inst, name), typing.List) and len(getattr(inst, name)) == 1:
                # Properties that need to be renamed because of language keyword conflicts
                # see mapping
                if name not in simplified_js:
                    name = name.replace("_fhir", "")
                self.assertFalse(isinstance(simplified_js[name], typing.List), "Should simplify lists {}".format(name))

        # test simplify coding
        # meta has known coding attribute 'tags'
        if hasattr(inst, 'meta'):
            if inst.meta and inst.meta.tag and len(inst.meta.tag) > 0:
                simplified_tags = [k for k in simplified_js['meta'].keys() if k.startswith('tag_')]
                self.assertEqual(len(inst.meta.tag), len(simplified_tags), "Should simplify meta tags.")
                self.assertTrue('tag' not in simplified_js['meta'], "Should not have meta.tag")

        # test simplify extensions
        if hasattr(inst, 'extension'):
            if inst.extension and len(inst.extension) > 0:
                assert 'extension' not in simplified_js
                simplified_extensions = [k for k in simplified_js.keys() if k.startswith('extension_')]
                self.assertTrue(len(simplified_extensions) >= len(inst.extension), "Should simplify extensions.")
                for simplified_extension in simplified_extensions:
                    assert simplified_js[simplified_extension] is not None, f"Missing value for {simplified_extension}"
                    assert 'fhirclient.models.coding.Coding' not in str(simplified_js[simplified_extension]), "Should simplify codes"
                    if simplified_js[simplified_extension] == 'NA':
                        logging.getLogger(__name__).warning(
                            "Extension.value is NA for resource_type:{} simplified_extension:{}".format(
                                inst.resource_type, simplified_extension))
        # test simplify schema
        for k in simplified_js:
            assert k in simplified_schema, "Should have a schema definition for {}".format(k)

        # test simplified, flattened
        from flatten_json import flatten
        flattened = flatten(simplified_js, separator='|')
        # test values
        for simplified_key, simplified_values in flattened.items():
            if not simplified_values:
                continue
            if not isinstance(simplified_values, typing.List):
                simplified_values = [simplified_values]
            for simplified_value in simplified_values:
                simplified_value_is_fhir_resource = 'fhirclient.models' in simplified_value.__class__.__module__
                simplified_value_is_dict = isinstance(simplified_value, dict)
                if simplified_value_is_fhir_resource or simplified_value_is_dict:
                    msg = "Should simplify value {} {} {}".format(simplified_key, simplified_value.__class__.__name__, vars(simplified_value))
                    self.assertFalse(simplified_value_is_fhir_resource, msg)

        for flattened_key in flattened:
            dict_ = simplified_schema
            for flattened_key_part in flattened_key.split('|'):
                if flattened_key_part not in dict_ and flattened_key_part.isnumeric():
                    # traverse over list index
                    continue
                if flattened_key_part in dict_:
                    dict_ = dict_[flattened_key_part]
                    self.assertIsNotNone(dict_, "Should have a schema entry for {}".format(flattened_key_part))
                    if 'docstring' not in dict_:
                        logging.getLogger(__name__).warning(
                            "Missing docstring for resource_type:{} flattened_key:{} flattened_key_part:{} dict:{}".format(
                                inst.resource_type, flattened_key, flattened_key_part, dict_))
                break