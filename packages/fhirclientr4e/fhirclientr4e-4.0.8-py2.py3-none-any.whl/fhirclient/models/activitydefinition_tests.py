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

from . import activitydefinition

from .fhirdate import FHIRDate
import logging


class ActivityDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ActivityDefinition", js["resourceType"])
        return activitydefinition.ActivityDefinition(js)
    
    def testActivityDefinition1(self):
        inst = self.instantiate_from("activitydefinition-predecessor-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ActivityDefinition instance")
        self.implActivityDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("ActivityDefinition", js["resourceType"])
        inst2 = activitydefinition.ActivityDefinition(js)
        self.implActivityDefinition1(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implActivityDefinition1(self, inst):
        self.assertEqual(inst.approvalDate.date, FHIRDate("2016-03-12").date)
        self.assertEqual(inst.approvalDate.as_json(), "2016-03-12")
        self.assertEqual(inst.author[0].name, "Motive Medical Intelligence")
        self.assertEqual(inst.author[0].telecom[0].system, "phone")
        self.assertEqual(inst.author[0].telecom[0].use, "work")
        self.assertEqual(inst.author[0].telecom[0].value, "415-362-4007")
        self.assertEqual(inst.author[0].telecom[1].system, "email")
        self.assertEqual(inst.author[0].telecom[1].use, "work")
        self.assertEqual(inst.author[0].telecom[1].value, "info@motivemi.com")
        self.assertEqual(inst.code.coding[0].code, "306206005")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Referral to service (procedure)")
        self.assertEqual(inst.contact[0].telecom[0].system, "phone")
        self.assertEqual(inst.contact[0].telecom[0].use, "work")
        self.assertEqual(inst.contact[0].telecom[0].value, "415-362-4007")
        self.assertEqual(inst.contact[0].telecom[1].system, "email")
        self.assertEqual(inst.contact[0].telecom[1].use, "work")
        self.assertEqual(inst.contact[0].telecom[1].value, "info@motivemi.com")
        self.assertEqual(inst.copyright, "© Copyright 2016 Motive Medical Intelligence. All rights reserved.")
        self.assertEqual(inst.date.date, FHIRDate("2017-03-03T14:06:00Z").date)
        self.assertEqual(inst.date.as_json(), "2017-03-03T14:06:00Z")
        self.assertEqual(inst.description, "refer to primary care mental-health integrated care program for evaluation and treatment of mental health conditions now")
        self.assertEqual(inst.effectivePeriod.end.date, FHIRDate("2017-12-31").date)
        self.assertEqual(inst.effectivePeriod.end.as_json(), "2017-12-31")
        self.assertEqual(inst.effectivePeriod.start.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.effectivePeriod.start.as_json(), "2016-01-01")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id, "referralPrimaryCareMentalHealth-initial")
        self.assertEqual(inst.identifier[0].system, "http://motivemi.com/artifacts")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "referralPrimaryCareMentalHealth")
        self.assertEqual(inst.jurisdiction[0].coding[0].code, "US")
        self.assertEqual(inst.jurisdiction[0].coding[0].system, "urn:iso:std:iso:3166")
        self.assertEqual(inst.kind, "ServiceRequest")
        self.assertEqual(inst.lastReviewDate.date, FHIRDate("2016-08-15").date)
        self.assertEqual(inst.lastReviewDate.as_json(), "2016-08-15")
        self.assertEqual(inst.name, "ReferralPrimaryCareMentalHealth")
        self.assertEqual(inst.participant[0].type, "practitioner")
        self.assertEqual(inst.publisher, "Motive Medical Intelligence")
        self.assertEqual(inst.relatedArtifact[0].display, "Practice Guideline for the Treatment of Patients with Major Depressive Disorder")
        self.assertEqual(inst.relatedArtifact[0].type, "citation")
        self.assertEqual(inst.relatedArtifact[0].url, "http://psychiatryonline.org/pb/assets/raw/sitewide/practice_guidelines/guidelines/mdd.pdf")
        self.assertEqual(inst.relatedArtifact[1].resource, "ActivityDefinition/referralPrimaryCareMentalHealth")
        self.assertEqual(inst.relatedArtifact[1].type, "successor")
        self.assertEqual(inst.status, "retired")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Referral to Primary Care Mental Health")
        self.assertEqual(inst.topic[0].text, "Mental Health Referral")
        self.assertEqual(inst.url, "http://motivemi.com/artifacts/ActivityDefinition/referralPrimaryCareMentalHealth")
        self.assertEqual(inst.useContext[0].code.code, "age")
        self.assertEqual(inst.useContext[0].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].code, "D000328")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].display, "Adult")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].system, "https://meshb.nlm.nih.gov")
        self.assertEqual(inst.useContext[1].code.code, "focus")
        self.assertEqual(inst.useContext[1].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[1].valueCodeableConcept.coding[0].code, "87512008")
        self.assertEqual(inst.useContext[1].valueCodeableConcept.coding[0].display, "Mild major depression")
        self.assertEqual(inst.useContext[1].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.useContext[2].code.code, "focus")
        self.assertEqual(inst.useContext[2].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[2].valueCodeableConcept.coding[0].code, "40379007")
        self.assertEqual(inst.useContext[2].valueCodeableConcept.coding[0].display, "Major depression, recurrent, mild")
        self.assertEqual(inst.useContext[2].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.useContext[3].code.code, "focus")
        self.assertEqual(inst.useContext[3].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[3].valueCodeableConcept.coding[0].code, "225444004")
        self.assertEqual(inst.useContext[3].valueCodeableConcept.coding[0].display, "At risk for suicide (finding)")
        self.assertEqual(inst.useContext[3].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.useContext[4].code.code, "focus")
        self.assertEqual(inst.useContext[4].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[4].valueCodeableConcept.coding[0].code, "306206005")
        self.assertEqual(inst.useContext[4].valueCodeableConcept.coding[0].display, "Referral to service (procedure)")
        self.assertEqual(inst.useContext[4].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.useContext[5].code.code, "user")
        self.assertEqual(inst.useContext[5].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[5].valueCodeableConcept.coding[0].code, "309343006")
        self.assertEqual(inst.useContext[5].valueCodeableConcept.coding[0].display, "Physician")
        self.assertEqual(inst.useContext[5].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.useContext[6].code.code, "venue")
        self.assertEqual(inst.useContext[6].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[6].valueCodeableConcept.coding[0].code, "440655000")
        self.assertEqual(inst.useContext[6].valueCodeableConcept.coding[0].display, "Outpatient environment")
        self.assertEqual(inst.useContext[6].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.version, "1.0.0")
    
    def testActivityDefinition2(self):
        inst = self.instantiate_from("activitydefinition-medicationorder-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ActivityDefinition instance")
        self.implActivityDefinition2(inst)
        
        js = inst.as_json()
        self.assertEqual("ActivityDefinition", js["resourceType"])
        inst2 = activitydefinition.ActivityDefinition(js)
        self.implActivityDefinition2(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implActivityDefinition2(self, inst):
        self.assertEqual(inst.approvalDate.date, FHIRDate("2016-03-12").date)
        self.assertEqual(inst.approvalDate.as_json(), "2016-03-12")
        self.assertEqual(inst.author[0].name, "Motive Medical Intelligence")
        self.assertEqual(inst.author[0].telecom[0].system, "phone")
        self.assertEqual(inst.author[0].telecom[0].use, "work")
        self.assertEqual(inst.author[0].telecom[0].value, "415-362-4007")
        self.assertEqual(inst.author[0].telecom[1].system, "email")
        self.assertEqual(inst.author[0].telecom[1].use, "work")
        self.assertEqual(inst.author[0].telecom[1].value, "info@motivemi.com")
        self.assertEqual(inst.contact[0].telecom[0].system, "phone")
        self.assertEqual(inst.contact[0].telecom[0].use, "work")
        self.assertEqual(inst.contact[0].telecom[0].value, "415-362-4007")
        self.assertEqual(inst.contact[0].telecom[1].system, "email")
        self.assertEqual(inst.contact[0].telecom[1].use, "work")
        self.assertEqual(inst.contact[0].telecom[1].value, "info@motivemi.com")
        self.assertEqual(inst.contained[0].id, "citalopramMedication")
        self.assertEqual(inst.contained[1].id, "citalopramSubstance")
        self.assertEqual(inst.copyright, "© Copyright 2016 Motive Medical Intelligence. All rights reserved.")
        self.assertEqual(inst.date.date, FHIRDate("2015-08-15").date)
        self.assertEqual(inst.date.as_json(), "2015-08-15")
        self.assertEqual(inst.description, "Citalopram 20 mg tablet 1 tablet oral 1 time daily now (30 table; 3 refills")
        self.assertEqual(inst.dosage[0].doseAndRate[0].doseQuantity.unit, "{tbl}")
        self.assertEqual(inst.dosage[0].doseAndRate[0].doseQuantity.value, 1)
        self.assertEqual(inst.dosage[0].doseAndRate[0].type.coding[0].code, "ordered")
        self.assertEqual(inst.dosage[0].doseAndRate[0].type.coding[0].display, "Ordered")
        self.assertEqual(inst.dosage[0].doseAndRate[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/dose-rate-type")
        self.assertEqual(inst.dosage[0].route.coding[0].code, "26643006")
        self.assertEqual(inst.dosage[0].route.coding[0].display, "Oral route (qualifier value)")
        self.assertEqual(inst.dosage[0].route.text, "Oral route (qualifier value)")
        self.assertEqual(inst.dosage[0].text, "1 tablet oral 1 time daily")
        self.assertEqual(inst.dosage[0].timing.repeat.frequency, 1)
        self.assertEqual(inst.dosage[0].timing.repeat.period, 1)
        self.assertEqual(inst.dosage[0].timing.repeat.periodUnit, "d")
        self.assertEqual(inst.dynamicValue[0].expression.description, "dispenseRequest.numberOfRepeatsAllowed is three (3)")
        self.assertEqual(inst.dynamicValue[0].expression.expression, "3")
        self.assertEqual(inst.dynamicValue[0].expression.language, "text/cql")
        self.assertEqual(inst.dynamicValue[0].path, "dispenseRequest.numberOfRepeatsAllowed")
        self.assertEqual(inst.dynamicValue[1].expression.description, "dispenseRequest.quantity is thirty (30) tablets")
        self.assertEqual(inst.dynamicValue[1].expression.expression, "30 '{tbl}'")
        self.assertEqual(inst.dynamicValue[1].expression.language, "text/cql")
        self.assertEqual(inst.dynamicValue[1].path, "dispenseRequest.quantity")
        self.assertEqual(inst.effectivePeriod.end.date, FHIRDate("2017-12-31").date)
        self.assertEqual(inst.effectivePeriod.end.as_json(), "2017-12-31")
        self.assertEqual(inst.effectivePeriod.start.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.effectivePeriod.start.as_json(), "2016-01-01")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id, "citalopramPrescription")
        self.assertEqual(inst.identifier[0].system, "http://motivemi.com")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "citalopramPrescription")
        self.assertEqual(inst.jurisdiction[0].coding[0].code, "US")
        self.assertEqual(inst.jurisdiction[0].coding[0].system, "urn:iso:std:iso:3166")
        self.assertEqual(inst.kind, "MedicationRequest")
        self.assertEqual(inst.lastReviewDate.date, FHIRDate("2016-08-15").date)
        self.assertEqual(inst.lastReviewDate.as_json(), "2016-08-15")
        self.assertEqual(inst.name, "CitalopramPrescription")
        self.assertEqual(inst.publisher, "Motive Medical Intelligence")
        self.assertEqual(inst.purpose, "Defines a guideline supported prescription for the treatment of depressive disorders")
        self.assertEqual(inst.relatedArtifact[0].display, "Practice Guideline for the Treatment of Patients with Major Depressive Disorder")
        self.assertEqual(inst.relatedArtifact[0].type, "citation")
        self.assertEqual(inst.relatedArtifact[0].url, "http://psychiatryonline.org/pb/assets/raw/sitewide/practice_guidelines/guidelines/mdd.pdf")
        self.assertEqual(inst.relatedArtifact[1].resource, "#citalopramMedication")
        self.assertEqual(inst.relatedArtifact[1].type, "composed-of")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Citalopram Prescription")
        self.assertEqual(inst.topic[0].text, "Mental Health Treatment")
        self.assertEqual(inst.url, "http://motivemi.com/artifacts/ActivityDefinition/citalopramPrescription")
        self.assertEqual(inst.usage, "This activity definition is used as part of various suicide risk order sets")
        self.assertEqual(inst.useContext[0].code.code, "age")
        self.assertEqual(inst.useContext[0].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].code, "D000328")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].display, "Adult")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].system, "https://meshb.nlm.nih.gov")
        self.assertEqual(inst.useContext[1].code.code, "focus")
        self.assertEqual(inst.useContext[1].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[1].valueCodeableConcept.coding[0].code, "87512008")
        self.assertEqual(inst.useContext[1].valueCodeableConcept.coding[0].display, "Mild major depression")
        self.assertEqual(inst.useContext[1].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.useContext[2].code.code, "focus")
        self.assertEqual(inst.useContext[2].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[2].valueCodeableConcept.coding[0].code, "40379007")
        self.assertEqual(inst.useContext[2].valueCodeableConcept.coding[0].display, "Major depression, recurrent, mild")
        self.assertEqual(inst.useContext[2].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.useContext[3].code.code, "focus")
        self.assertEqual(inst.useContext[3].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[3].valueCodeableConcept.coding[0].code, "225444004")
        self.assertEqual(inst.useContext[3].valueCodeableConcept.coding[0].display, "At risk for suicide (finding)")
        self.assertEqual(inst.useContext[3].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.useContext[4].code.code, "focus")
        self.assertEqual(inst.useContext[4].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[4].valueCodeableConcept.coding[0].code, "306206005")
        self.assertEqual(inst.useContext[4].valueCodeableConcept.coding[0].display, "Referral to service (procedure)")
        self.assertEqual(inst.useContext[4].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.useContext[5].code.code, "user")
        self.assertEqual(inst.useContext[5].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[5].valueCodeableConcept.coding[0].code, "309343006")
        self.assertEqual(inst.useContext[5].valueCodeableConcept.coding[0].display, "Physician")
        self.assertEqual(inst.useContext[5].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.useContext[6].code.code, "venue")
        self.assertEqual(inst.useContext[6].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[6].valueCodeableConcept.coding[0].code, "440655000")
        self.assertEqual(inst.useContext[6].valueCodeableConcept.coding[0].display, "Outpatient environment")
        self.assertEqual(inst.useContext[6].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.version, "1.0.0")
    
    def testActivityDefinition3(self):
        inst = self.instantiate_from("activitydefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ActivityDefinition instance")
        self.implActivityDefinition3(inst)
        
        js = inst.as_json()
        self.assertEqual("ActivityDefinition", js["resourceType"])
        inst2 = activitydefinition.ActivityDefinition(js)
        self.implActivityDefinition3(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implActivityDefinition3(self, inst):
        self.assertEqual(inst.approvalDate.date, FHIRDate("2017-03-01").date)
        self.assertEqual(inst.approvalDate.as_json(), "2017-03-01")
        self.assertEqual(inst.author[0].name, "Motive Medical Intelligence")
        self.assertEqual(inst.author[0].telecom[0].system, "phone")
        self.assertEqual(inst.author[0].telecom[0].use, "work")
        self.assertEqual(inst.author[0].telecom[0].value, "415-362-4007")
        self.assertEqual(inst.author[0].telecom[1].system, "email")
        self.assertEqual(inst.author[0].telecom[1].use, "work")
        self.assertEqual(inst.author[0].telecom[1].value, "info@motivemi.com")
        self.assertEqual(inst.code.coding[0].code, "306206005")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Referral to service (procedure)")
        self.assertEqual(inst.contact[0].telecom[0].system, "phone")
        self.assertEqual(inst.contact[0].telecom[0].use, "work")
        self.assertEqual(inst.contact[0].telecom[0].value, "415-362-4007")
        self.assertEqual(inst.contact[0].telecom[1].system, "email")
        self.assertEqual(inst.contact[0].telecom[1].use, "work")
        self.assertEqual(inst.contact[0].telecom[1].value, "info@motivemi.com")
        self.assertEqual(inst.copyright, "© Copyright 2016 Motive Medical Intelligence. All rights reserved.")
        self.assertEqual(inst.date.date, FHIRDate("2017-03-03T14:06:00Z").date)
        self.assertEqual(inst.date.as_json(), "2017-03-03T14:06:00Z")
        self.assertEqual(inst.description, "refer to primary care mental-health integrated care program for evaluation and treatment of mental health conditions now")
        self.assertEqual(inst.effectivePeriod.end.date, FHIRDate("2017-12-31").date)
        self.assertEqual(inst.effectivePeriod.end.as_json(), "2017-12-31")
        self.assertEqual(inst.effectivePeriod.start.date, FHIRDate("2017-03-01").date)
        self.assertEqual(inst.effectivePeriod.start.as_json(), "2017-03-01")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id, "referralPrimaryCareMentalHealth")
        self.assertEqual(inst.identifier[0].system, "http://motivemi.com/artifacts")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "referralPrimaryCareMentalHealth")
        self.assertEqual(inst.jurisdiction[0].coding[0].code, "US")
        self.assertEqual(inst.jurisdiction[0].coding[0].system, "urn:iso:std:iso:3166")
        self.assertEqual(inst.kind, "ServiceRequest")
        self.assertEqual(inst.lastReviewDate.date, FHIRDate("2017-03-01").date)
        self.assertEqual(inst.lastReviewDate.as_json(), "2017-03-01")
        self.assertEqual(inst.name, "ReferralPrimaryCareMentalHealth")
        self.assertEqual(inst.participant[0].type, "practitioner")
        self.assertEqual(inst.publisher, "Motive Medical Intelligence")
        self.assertEqual(inst.relatedArtifact[0].display, "Practice Guideline for the Treatment of Patients with Major Depressive Disorder")
        self.assertEqual(inst.relatedArtifact[0].type, "citation")
        self.assertEqual(inst.relatedArtifact[0].url, "http://psychiatryonline.org/pb/assets/raw/sitewide/practice_guidelines/guidelines/mdd.pdf")
        self.assertEqual(inst.relatedArtifact[1].resource, "ActivityDefinition/referralPrimaryCareMentalHealth-initial")
        self.assertEqual(inst.relatedArtifact[1].type, "predecessor")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Referral to Primary Care Mental Health")
        self.assertEqual(inst.topic[0].text, "Mental Health Referral")
        self.assertEqual(inst.url, "http://motivemi.com/artifacts/ActivityDefinition/referralPrimaryCareMentalHealth")
        self.assertEqual(inst.useContext[0].code.code, "age")
        self.assertEqual(inst.useContext[0].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].code, "D000328")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].display, "Adult")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].system, "https://meshb.nlm.nih.gov")
        self.assertEqual(inst.useContext[1].code.code, "focus")
        self.assertEqual(inst.useContext[1].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[1].valueCodeableConcept.coding[0].code, "87512008")
        self.assertEqual(inst.useContext[1].valueCodeableConcept.coding[0].display, "Mild major depression")
        self.assertEqual(inst.useContext[1].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.useContext[2].code.code, "focus")
        self.assertEqual(inst.useContext[2].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[2].valueCodeableConcept.coding[0].code, "40379007")
        self.assertEqual(inst.useContext[2].valueCodeableConcept.coding[0].display, "Major depression, recurrent, mild")
        self.assertEqual(inst.useContext[2].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.useContext[3].code.code, "focus")
        self.assertEqual(inst.useContext[3].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[3].valueCodeableConcept.coding[0].code, "225444004")
        self.assertEqual(inst.useContext[3].valueCodeableConcept.coding[0].display, "At risk for suicide (finding)")
        self.assertEqual(inst.useContext[3].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.useContext[4].code.code, "focus")
        self.assertEqual(inst.useContext[4].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[4].valueCodeableConcept.coding[0].code, "306206005")
        self.assertEqual(inst.useContext[4].valueCodeableConcept.coding[0].display, "Referral to service (procedure)")
        self.assertEqual(inst.useContext[4].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.useContext[5].code.code, "user")
        self.assertEqual(inst.useContext[5].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[5].valueCodeableConcept.coding[0].code, "309343006")
        self.assertEqual(inst.useContext[5].valueCodeableConcept.coding[0].display, "Physician")
        self.assertEqual(inst.useContext[5].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.useContext[6].code.code, "venue")
        self.assertEqual(inst.useContext[6].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[6].valueCodeableConcept.coding[0].code, "440655000")
        self.assertEqual(inst.useContext[6].valueCodeableConcept.coding[0].display, "Outpatient environment")
        self.assertEqual(inst.useContext[6].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.version, "1.1.0")
    
    def testActivityDefinition4(self):
        inst = self.instantiate_from("activitydefinition-servicerequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ActivityDefinition instance")
        self.implActivityDefinition4(inst)
        
        js = inst.as_json()
        self.assertEqual("ActivityDefinition", js["resourceType"])
        inst2 = activitydefinition.ActivityDefinition(js)
        self.implActivityDefinition4(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implActivityDefinition4(self, inst):
        self.assertEqual(inst.bodySite[0].coding[0].code, "17401000")
        self.assertEqual(inst.bodySite[0].coding[0].display, "Heart valve structure")
        self.assertEqual(inst.bodySite[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.coding[0].code, "34068001")
        self.assertEqual(inst.code.coding[0].display, "Heart valve replacement")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.description, "Heart valve replacement")
        self.assertEqual(inst.id, "heart-valve-replacement")
        self.assertEqual(inst.kind, "ServiceRequest")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.participant[0].role.coding[0].code, "207RI0011X")
        self.assertEqual(inst.participant[0].role.coding[0].display, "Interventional Cardiology")
        self.assertEqual(inst.participant[0].role.coding[0].system, "http://nucc.org/provider-taxonomy")
        self.assertEqual(inst.participant[0].role.text, "Interventional Cardiology")
        self.assertEqual(inst.participant[0].type, "practitioner")
        self.assertEqual(inst.purpose, "Describes the proposal to perform a Heart Valve replacement.")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.topic[0].coding[0].code, "34068001")
        self.assertEqual(inst.topic[0].coding[0].display, "Heart valve replacement")
        self.assertEqual(inst.topic[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.useContext[0].code.code, "age")
        self.assertEqual(inst.useContext[0].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].code, "D000328")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].display, "Adult")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].system, "https://meshb.nlm.nih.gov")
        self.assertEqual(inst.useContext[1].code.code, "user")
        self.assertEqual(inst.useContext[1].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[1].valueCodeableConcept.coding[0].code, "309343006")
        self.assertEqual(inst.useContext[1].valueCodeableConcept.coding[0].display, "Physician")
        self.assertEqual(inst.useContext[1].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
    
    def testActivityDefinition5(self):
        inst = self.instantiate_from("activitydefinition-supplyrequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ActivityDefinition instance")
        self.implActivityDefinition5(inst)
        
        js = inst.as_json()
        self.assertEqual("ActivityDefinition", js["resourceType"])
        inst2 = activitydefinition.ActivityDefinition(js)
        self.implActivityDefinition5(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implActivityDefinition5(self, inst):
        self.assertEqual(inst.code.coding[0].code, "BlueTubes")
        self.assertEqual(inst.code.coding[0].display, "Blood collect tubes blue cap")
        self.assertEqual(inst.description, "10 Blood collect tubes blue cap")
        self.assertEqual(inst.id, "blood-tubes-supply")
        self.assertEqual(inst.kind, "SupplyRequest")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.purpose, "Describes a request for 10 Blood collection tubes with blue caps.")
        self.assertEqual(inst.quantity.value, 10)
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.transform, "StructureMap/supplyrequest-transform")

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