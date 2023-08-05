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

from . import encounter

from .fhirdate import FHIRDate
import logging


class EncounterTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Encounter", js["resourceType"])
        return encounter.Encounter(js)
    
    def testEncounter1(self):
        inst = self.instantiate_from("encounter-example-home.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter1(inst)
        
        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter1(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implEncounter1(self, inst):
        self.assertEqual(inst.class_fhir.code, "HH")
        self.assertEqual(inst.class_fhir.display, "home health")
        self.assertEqual(inst.class_fhir.system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.contained[0].id, "home")
        self.assertEqual(inst.id, "home")
        self.assertEqual(inst.location[0].period.end.date, FHIRDate("2015-01-17T16:30:00+10:00").date)
        self.assertEqual(inst.location[0].period.end.as_json(), "2015-01-17T16:30:00+10:00")
        self.assertEqual(inst.location[0].period.start.date, FHIRDate("2015-01-17T16:00:00+10:00").date)
        self.assertEqual(inst.location[0].period.start.as_json(), "2015-01-17T16:00:00+10:00")
        self.assertEqual(inst.location[0].status, "completed")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.participant[0].period.end.date, FHIRDate("2015-01-17T16:30:00+10:00").date)
        self.assertEqual(inst.participant[0].period.end.as_json(), "2015-01-17T16:30:00+10:00")
        self.assertEqual(inst.participant[0].period.start.date, FHIRDate("2015-01-17T16:00:00+10:00").date)
        self.assertEqual(inst.participant[0].period.start.as_json(), "2015-01-17T16:00:00+10:00")
        self.assertEqual(inst.period.end.date, FHIRDate("2015-01-17T16:30:00+10:00").date)
        self.assertEqual(inst.period.end.as_json(), "2015-01-17T16:30:00+10:00")
        self.assertEqual(inst.period.start.date, FHIRDate("2015-01-17T16:00:00+10:00").date)
        self.assertEqual(inst.period.start.as_json(), "2015-01-17T16:00:00+10:00")
        self.assertEqual(inst.status, "finished")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Encounter with patient @example who is at home</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testEncounter2(self):
        inst = self.instantiate_from("encounter-example-f201-20130404.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter2(inst)
        
        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter2(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implEncounter2(self, inst):
        self.assertEqual(inst.class_fhir.code, "AMB")
        self.assertEqual(inst.class_fhir.display, "ambulatory")
        self.assertEqual(inst.class_fhir.system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.identifier[0].use, "temp")
        self.assertEqual(inst.identifier[0].value, "Encounter_Roel_20130404")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.priority.coding[0].code, "17621005")
        self.assertEqual(inst.priority.coding[0].display, "Normal")
        self.assertEqual(inst.priority.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.reasonCode[0].text, "The patient had fever peaks over the last couple of days. He is worried about these peaks.")
        self.assertEqual(inst.status, "finished")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "11429006")
        self.assertEqual(inst.type[0].coding[0].display, "Consultation")
        self.assertEqual(inst.type[0].coding[0].system, "http://snomed.info/sct")
    
    def testEncounter3(self):
        inst = self.instantiate_from("encounter-example-f003-abscess.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter3(inst)
        
        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter3(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implEncounter3(self, inst):
        self.assertEqual(inst.class_fhir.code, "AMB")
        self.assertEqual(inst.class_fhir.display, "ambulatory")
        self.assertEqual(inst.class_fhir.system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].code, "305956004")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].display, "Referral by physician")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.hospitalization.dischargeDisposition.coding[0].code, "306689006")
        self.assertEqual(inst.hospitalization.dischargeDisposition.coding[0].display, "Discharge to home")
        self.assertEqual(inst.hospitalization.dischargeDisposition.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.hospitalization.preAdmissionIdentifier.system, "http://www.bmc.nl/zorgportal/identifiers/pre-admissions")
        self.assertEqual(inst.hospitalization.preAdmissionIdentifier.use, "official")
        self.assertEqual(inst.hospitalization.preAdmissionIdentifier.value, "93042")
        self.assertEqual(inst.id, "f003")
        self.assertEqual(inst.identifier[0].system, "http://www.bmc.nl/zorgportal/identifiers/encounters")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "v6751")
        self.assertEqual(inst.length.code, "min")
        self.assertEqual(inst.length.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.length.unit, "min")
        self.assertEqual(inst.length.value, 90)
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.priority.coding[0].code, "103391001")
        self.assertEqual(inst.priority.coding[0].display, "Non-urgent ear, nose and throat admission")
        self.assertEqual(inst.priority.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.reasonCode[0].coding[0].code, "18099001")
        self.assertEqual(inst.reasonCode[0].coding[0].display, "Retropharyngeal abscess")
        self.assertEqual(inst.reasonCode[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.status, "finished")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "270427003")
        self.assertEqual(inst.type[0].coding[0].display, "Patient-initiated encounter")
        self.assertEqual(inst.type[0].coding[0].system, "http://snomed.info/sct")
    
    def testEncounter4(self):
        inst = self.instantiate_from("encounter-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter4(inst)
        
        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter4(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implEncounter4(self, inst):
        self.assertEqual(inst.class_fhir.code, "IMP")
        self.assertEqual(inst.class_fhir.display, "inpatient encounter")
        self.assertEqual(inst.class_fhir.system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "in-progress")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Encounter with patient @example</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testEncounter5(self):
        inst = self.instantiate_from("encounter-example-f002-lung.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter5(inst)
        
        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter5(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implEncounter5(self, inst):
        self.assertEqual(inst.class_fhir.code, "AMB")
        self.assertEqual(inst.class_fhir.display, "ambulatory")
        self.assertEqual(inst.class_fhir.system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].code, "305997006")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].display, "Referral by radiologist")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.hospitalization.dischargeDisposition.coding[0].code, "306689006")
        self.assertEqual(inst.hospitalization.dischargeDisposition.coding[0].display, "Discharge to home")
        self.assertEqual(inst.hospitalization.dischargeDisposition.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.hospitalization.preAdmissionIdentifier.system, "http://www.bmc.nl/zorgportal/identifiers/pre-admissions")
        self.assertEqual(inst.hospitalization.preAdmissionIdentifier.use, "official")
        self.assertEqual(inst.hospitalization.preAdmissionIdentifier.value, "98682")
        self.assertEqual(inst.id, "f002")
        self.assertEqual(inst.identifier[0].system, "http://www.bmc.nl/zorgportal/identifiers/encounters")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "v3251")
        self.assertEqual(inst.length.code, "min")
        self.assertEqual(inst.length.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.length.unit, "min")
        self.assertEqual(inst.length.value, 140)
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.priority.coding[0].code, "103391001")
        self.assertEqual(inst.priority.coding[0].display, "Urgent")
        self.assertEqual(inst.priority.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.reasonCode[0].coding[0].code, "34068001")
        self.assertEqual(inst.reasonCode[0].coding[0].display, "Partial lobectomy of lung")
        self.assertEqual(inst.reasonCode[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.status, "finished")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "270427003")
        self.assertEqual(inst.type[0].coding[0].display, "Patient-initiated encounter")
        self.assertEqual(inst.type[0].coding[0].system, "http://snomed.info/sct")
    
    def testEncounter6(self):
        inst = self.instantiate_from("encounter-example-f203-20130311.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter6(inst)
        
        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter6(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implEncounter6(self, inst):
        self.assertEqual(inst.class_fhir.code, "IMP")
        self.assertEqual(inst.class_fhir.display, "inpatient encounter")
        self.assertEqual(inst.class_fhir.system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.diagnosis[0].rank, 1)
        self.assertEqual(inst.diagnosis[0].use.coding[0].code, "AD")
        self.assertEqual(inst.diagnosis[0].use.coding[0].display, "Admission diagnosis")
        self.assertEqual(inst.diagnosis[0].use.coding[0].system, "http://terminology.hl7.org/CodeSystem/diagnosis-role")
        self.assertEqual(inst.diagnosis[1].use.coding[0].code, "DD")
        self.assertEqual(inst.diagnosis[1].use.coding[0].display, "Discharge diagnosis")
        self.assertEqual(inst.diagnosis[1].use.coding[0].system, "http://terminology.hl7.org/CodeSystem/diagnosis-role")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].code, "309902002")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].display, "Clinical Oncology Department")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.hospitalization.dietPreference[0].coding[0].code, "276026009")
        self.assertEqual(inst.hospitalization.dietPreference[0].coding[0].display, "Fluid balance regulation")
        self.assertEqual(inst.hospitalization.dietPreference[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.hospitalization.reAdmission.coding[0].display, "readmitted")
        self.assertEqual(inst.hospitalization.specialArrangement[0].coding[0].code, "wheel")
        self.assertEqual(inst.hospitalization.specialArrangement[0].coding[0].display, "Wheelchair")
        self.assertEqual(inst.hospitalization.specialArrangement[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/encounter-special-arrangements")
        self.assertEqual(inst.hospitalization.specialCourtesy[0].coding[0].code, "NRM")
        self.assertEqual(inst.hospitalization.specialCourtesy[0].coding[0].display, "normal courtesy")
        self.assertEqual(inst.hospitalization.specialCourtesy[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-EncounterSpecialCourtesy")
        self.assertEqual(inst.id, "f203")
        self.assertEqual(inst.identifier[0].use, "temp")
        self.assertEqual(inst.identifier[0].value, "Encounter_Roel_20130311")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.participant[0].type[0].coding[0].code, "PART")
        self.assertEqual(inst.participant[0].type[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.period.end.date, FHIRDate("2013-03-20").date)
        self.assertEqual(inst.period.end.as_json(), "2013-03-20")
        self.assertEqual(inst.period.start.date, FHIRDate("2013-03-11").date)
        self.assertEqual(inst.period.start.as_json(), "2013-03-11")
        self.assertEqual(inst.priority.coding[0].code, "394849002")
        self.assertEqual(inst.priority.coding[0].display, "High priority")
        self.assertEqual(inst.priority.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.reasonCode[0].text, "The patient seems to suffer from bilateral pneumonia and renal insufficiency, most likely due to chemotherapy.")
        self.assertEqual(inst.status, "finished")
        self.assertEqual(inst.statusHistory[0].period.start.date, FHIRDate("2013-03-08").date)
        self.assertEqual(inst.statusHistory[0].period.start.as_json(), "2013-03-08")
        self.assertEqual(inst.statusHistory[0].status, "arrived")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "183807002")
        self.assertEqual(inst.type[0].coding[0].display, "Inpatient stay for nine days")
        self.assertEqual(inst.type[0].coding[0].system, "http://snomed.info/sct")
    
    def testEncounter7(self):
        inst = self.instantiate_from("encounter-example-xcda.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter7(inst)
        
        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter7(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implEncounter7(self, inst):
        self.assertEqual(inst.class_fhir.code, "AMB")
        self.assertEqual(inst.class_fhir.display, "ambulatory")
        self.assertEqual(inst.class_fhir.system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.id, "xcda")
        self.assertEqual(inst.identifier[0].system, "http://healthcare.example.org/identifiers/enocunter")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "1234213.52345873")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.reasonCode[0].coding[0].code, "T-D8200")
        self.assertEqual(inst.reasonCode[0].coding[0].display, "Arm")
        self.assertEqual(inst.reasonCode[0].coding[0].system, "http://ihe.net/xds/connectathon/eventCodes")
        self.assertEqual(inst.status, "finished")
        self.assertEqual(inst.text.status, "generated")
    
    def testEncounter8(self):
        inst = self.instantiate_from("encounter-example-f202-20130128.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter8(inst)
        
        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter8(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implEncounter8(self, inst):
        self.assertEqual(inst.class_fhir.code, "AMB")
        self.assertEqual(inst.class_fhir.display, "ambulatory")
        self.assertEqual(inst.class_fhir.system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.diagnosis[0].rank, 2)
        self.assertEqual(inst.diagnosis[0].use.coding[0].code, "AD")
        self.assertEqual(inst.diagnosis[0].use.coding[0].display, "Admission diagnosis")
        self.assertEqual(inst.diagnosis[0].use.coding[0].system, "http://terminology.hl7.org/CodeSystem/diagnosis-role")
        self.assertEqual(inst.diagnosis[1].rank, 1)
        self.assertEqual(inst.diagnosis[1].use.coding[0].code, "CC")
        self.assertEqual(inst.diagnosis[1].use.coding[0].display, "Chief complaint")
        self.assertEqual(inst.diagnosis[1].use.coding[0].system, "http://terminology.hl7.org/CodeSystem/diagnosis-role")
        self.assertEqual(inst.id, "f202")
        self.assertEqual(inst.identifier[0].use, "temp")
        self.assertEqual(inst.identifier[0].value, "Encounter_Roel_20130128")
        self.assertEqual(inst.length.code, "min")
        self.assertEqual(inst.length.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.length.unit, "minutes")
        self.assertEqual(inst.length.value, 56)
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.priority.coding[0].code, "103391001")
        self.assertEqual(inst.priority.coding[0].display, "Urgent")
        self.assertEqual(inst.priority.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.reasonCode[0].text, "The patient is treated for a tumor.")
        self.assertEqual(inst.status, "finished")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "367336001")
        self.assertEqual(inst.type[0].coding[0].display, "Chemotherapy")
        self.assertEqual(inst.type[0].coding[0].system, "http://snomed.info/sct")
    
    def testEncounter9(self):
        inst = self.instantiate_from("encounter-example-emerg.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter9(inst)
        
        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter9(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implEncounter9(self, inst):
        self.assertEqual(inst.classHistory[0].class_fhir.code, "EMER")
        self.assertEqual(inst.classHistory[0].class_fhir.display, "emergency")
        self.assertEqual(inst.classHistory[0].class_fhir.system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.classHistory[0].period.end.date, FHIRDate("2017-02-01T09:27:00+10:00").date)
        self.assertEqual(inst.classHistory[0].period.end.as_json(), "2017-02-01T09:27:00+10:00")
        self.assertEqual(inst.classHistory[0].period.start.date, FHIRDate("2017-02-01T07:15:00+10:00").date)
        self.assertEqual(inst.classHistory[0].period.start.as_json(), "2017-02-01T07:15:00+10:00")
        self.assertEqual(inst.classHistory[1].class_fhir.code, "IMP")
        self.assertEqual(inst.classHistory[1].class_fhir.display, "inpatient encounter")
        self.assertEqual(inst.classHistory[1].class_fhir.system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.classHistory[1].period.start.date, FHIRDate("2017-02-01T09:27:00+10:00").date)
        self.assertEqual(inst.classHistory[1].period.start.as_json(), "2017-02-01T09:27:00+10:00")
        self.assertEqual(inst.class_fhir.code, "IMP")
        self.assertEqual(inst.class_fhir.display, "inpatient encounter")
        self.assertEqual(inst.class_fhir.system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].code, "emd")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].display, "From accident/emergency department")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].system, "http://terminology.hl7.org/CodeSystem/admit-source")
        self.assertEqual(inst.id, "emerg")
        self.assertEqual(inst.location[0].period.end.date, FHIRDate("2017-02-01T08:45:00+10:00").date)
        self.assertEqual(inst.location[0].period.end.as_json(), "2017-02-01T08:45:00+10:00")
        self.assertEqual(inst.location[0].period.start.date, FHIRDate("2017-02-01T07:15:00+10:00").date)
        self.assertEqual(inst.location[0].period.start.as_json(), "2017-02-01T07:15:00+10:00")
        self.assertEqual(inst.location[0].status, "active")
        self.assertEqual(inst.location[1].period.end.date, FHIRDate("2017-02-01T09:27:00+10:00").date)
        self.assertEqual(inst.location[1].period.end.as_json(), "2017-02-01T09:27:00+10:00")
        self.assertEqual(inst.location[1].period.start.date, FHIRDate("2017-02-01T08:45:00+10:00").date)
        self.assertEqual(inst.location[1].period.start.as_json(), "2017-02-01T08:45:00+10:00")
        self.assertEqual(inst.location[1].status, "active")
        self.assertEqual(inst.location[2].period.end.date, FHIRDate("2017-02-01T12:15:00+10:00").date)
        self.assertEqual(inst.location[2].period.end.as_json(), "2017-02-01T12:15:00+10:00")
        self.assertEqual(inst.location[2].period.start.date, FHIRDate("2017-02-01T09:27:00+10:00").date)
        self.assertEqual(inst.location[2].period.start.as_json(), "2017-02-01T09:27:00+10:00")
        self.assertEqual(inst.location[2].status, "active")
        self.assertEqual(inst.location[3].period.end.date, FHIRDate("2017-02-01T12:45:00+10:00").date)
        self.assertEqual(inst.location[3].period.end.as_json(), "2017-02-01T12:45:00+10:00")
        self.assertEqual(inst.location[3].period.start.date, FHIRDate("2017-02-01T12:15:00+10:00").date)
        self.assertEqual(inst.location[3].period.start.as_json(), "2017-02-01T12:15:00+10:00")
        self.assertEqual(inst.location[3].status, "reserved")
        self.assertEqual(inst.location[4].period.start.date, FHIRDate("2017-02-01T12:45:00+10:00").date)
        self.assertEqual(inst.location[4].period.start.as_json(), "2017-02-01T12:45:00+10:00")
        self.assertEqual(inst.location[4].status, "active")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.start.date, FHIRDate("2017-02-01T07:15:00+10:00").date)
        self.assertEqual(inst.period.start.as_json(), "2017-02-01T07:15:00+10:00")
        self.assertEqual(inst.status, "in-progress")
        self.assertEqual(inst.statusHistory[0].period.end.date, FHIRDate("2017-02-01T07:35:00+10:00").date)
        self.assertEqual(inst.statusHistory[0].period.end.as_json(), "2017-02-01T07:35:00+10:00")
        self.assertEqual(inst.statusHistory[0].period.start.date, FHIRDate("2017-02-01T07:15:00+10:00").date)
        self.assertEqual(inst.statusHistory[0].period.start.as_json(), "2017-02-01T07:15:00+10:00")
        self.assertEqual(inst.statusHistory[0].status, "arrived")
        self.assertEqual(inst.statusHistory[1].period.end.date, FHIRDate("2017-02-01T08:45:00+10:00").date)
        self.assertEqual(inst.statusHistory[1].period.end.as_json(), "2017-02-01T08:45:00+10:00")
        self.assertEqual(inst.statusHistory[1].period.start.date, FHIRDate("2017-02-01T07:35:00+10:00").date)
        self.assertEqual(inst.statusHistory[1].period.start.as_json(), "2017-02-01T07:35:00+10:00")
        self.assertEqual(inst.statusHistory[1].status, "triaged")
        self.assertEqual(inst.statusHistory[2].period.end.date, FHIRDate("2017-02-01T12:15:00+10:00").date)
        self.assertEqual(inst.statusHistory[2].period.end.as_json(), "2017-02-01T12:15:00+10:00")
        self.assertEqual(inst.statusHistory[2].period.start.date, FHIRDate("2017-02-01T08:45:00+10:00").date)
        self.assertEqual(inst.statusHistory[2].period.start.as_json(), "2017-02-01T08:45:00+10:00")
        self.assertEqual(inst.statusHistory[2].status, "in-progress")
        self.assertEqual(inst.statusHistory[3].period.end.date, FHIRDate("2017-02-01T12:45:00+10:00").date)
        self.assertEqual(inst.statusHistory[3].period.end.as_json(), "2017-02-01T12:45:00+10:00")
        self.assertEqual(inst.statusHistory[3].period.start.date, FHIRDate("2017-02-01T12:15:00+10:00").date)
        self.assertEqual(inst.statusHistory[3].period.start.as_json(), "2017-02-01T12:15:00+10:00")
        self.assertEqual(inst.statusHistory[3].status, "onleave")
        self.assertEqual(inst.statusHistory[4].period.start.date, FHIRDate("2017-02-01T12:45:00+10:00").date)
        self.assertEqual(inst.statusHistory[4].period.start.as_json(), "2017-02-01T12:45:00+10:00")
        self.assertEqual(inst.statusHistory[4].status, "in-progress")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Emergency visit that escalated into inpatient patient @example</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testEncounter10(self):
        inst = self.instantiate_from("encounter-example-f001-heart.json")
        self.assertIsNotNone(inst, "Must have instantiated a Encounter instance")
        self.implEncounter10(inst)
        
        js = inst.as_json()
        self.assertEqual("Encounter", js["resourceType"])
        inst2 = encounter.Encounter(js)
        self.implEncounter10(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implEncounter10(self, inst):
        self.assertEqual(inst.class_fhir.code, "AMB")
        self.assertEqual(inst.class_fhir.display, "ambulatory")
        self.assertEqual(inst.class_fhir.system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].code, "305956004")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].display, "Referral by physician")
        self.assertEqual(inst.hospitalization.admitSource.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.hospitalization.dischargeDisposition.coding[0].code, "306689006")
        self.assertEqual(inst.hospitalization.dischargeDisposition.coding[0].display, "Discharge to home")
        self.assertEqual(inst.hospitalization.dischargeDisposition.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.hospitalization.preAdmissionIdentifier.system, "http://www.amc.nl/zorgportal/identifiers/pre-admissions")
        self.assertEqual(inst.hospitalization.preAdmissionIdentifier.use, "official")
        self.assertEqual(inst.hospitalization.preAdmissionIdentifier.value, "93042")
        self.assertEqual(inst.id, "f001")
        self.assertEqual(inst.identifier[0].system, "http://www.amc.nl/zorgportal/identifiers/visits")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "v1451")
        self.assertEqual(inst.length.code, "min")
        self.assertEqual(inst.length.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.length.unit, "min")
        self.assertEqual(inst.length.value, 140)
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.priority.coding[0].code, "310361003")
        self.assertEqual(inst.priority.coding[0].display, "Non-urgent cardiological admission")
        self.assertEqual(inst.priority.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.reasonCode[0].coding[0].code, "34068001")
        self.assertEqual(inst.reasonCode[0].coding[0].display, "Heart valve replacement")
        self.assertEqual(inst.reasonCode[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.status, "finished")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "270427003")
        self.assertEqual(inst.type[0].coding[0].display, "Patient-initiated encounter")
        self.assertEqual(inst.type[0].coding[0].system, "http://snomed.info/sct")

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