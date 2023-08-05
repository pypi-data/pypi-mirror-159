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

from . import patient

from .fhirdate import FHIRDate
import logging


class PatientTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Patient", js["resourceType"])
        return patient.Patient(js)
    
    def testPatient1(self):
        inst = self.instantiate_from("patient-example-xds.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient1(inst)
        
        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient1(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implPatient1(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].city, "Metropolis")
        self.assertEqual(inst.address[0].country, "USA")
        self.assertEqual(inst.address[0].line[0], "100 Main St")
        self.assertEqual(inst.address[0].postalCode, "44130")
        self.assertEqual(inst.address[0].state, "Il")
        self.assertEqual(inst.birthDate.date, FHIRDate("1956-05-27").date)
        self.assertEqual(inst.birthDate.as_json(), "1956-05-27")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "xds")
        self.assertEqual(inst.identifier[0].system, "urn:oid:1.2.3.4.5")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "MR")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0203")
        self.assertEqual(inst.identifier[0].use, "usual")
        self.assertEqual(inst.identifier[0].value, "89765a87b")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].family, "Doe")
        self.assertEqual(inst.name[0].given[0], "John")
        self.assertEqual(inst.text.status, "generated")
    
    def testPatient2(self):
        inst = self.instantiate_from("patient-example-f001-pieter.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient2(inst)
        
        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient2(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implPatient2(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].city, "Amsterdam")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Van Egmondkade 23")
        self.assertEqual(inst.address[0].postalCode, "1024 RJ")
        self.assertEqual(inst.address[0].use, "home")
        self.assertEqual(inst.birthDate.date, FHIRDate("1944-11-17").date)
        self.assertEqual(inst.birthDate.as_json(), "1944-11-17")
        self.assertEqual(inst.communication[0].language.coding[0].code, "nl")
        self.assertEqual(inst.communication[0].language.coding[0].display, "Dutch")
        self.assertEqual(inst.communication[0].language.coding[0].system, "urn:ietf:bcp:47")
        self.assertEqual(inst.communication[0].language.text, "Nederlands")
        self.assertTrue(inst.communication[0].preferred)
        self.assertEqual(inst.contact[0].name.family, "Abels")
        self.assertEqual(inst.contact[0].name.given[0], "Sarah")
        self.assertEqual(inst.contact[0].name.use, "usual")
        self.assertEqual(inst.contact[0].relationship[0].coding[0].code, "C")
        self.assertEqual(inst.contact[0].relationship[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0131")
        self.assertEqual(inst.contact[0].telecom[0].system, "phone")
        self.assertEqual(inst.contact[0].telecom[0].use, "mobile")
        self.assertEqual(inst.contact[0].telecom[0].value, "0690383372")
        self.assertFalse(inst.deceasedBoolean)
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "f001")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.840.1.113883.2.4.6.3")
        self.assertEqual(inst.identifier[0].use, "usual")
        self.assertEqual(inst.identifier[0].value, "738472983")
        self.assertEqual(inst.identifier[1].system, "urn:oid:2.16.840.1.113883.2.4.6.3")
        self.assertEqual(inst.identifier[1].use, "usual")
        self.assertEqual(inst.maritalStatus.coding[0].code, "M")
        self.assertEqual(inst.maritalStatus.coding[0].display, "Married")
        self.assertEqual(inst.maritalStatus.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus")
        self.assertEqual(inst.maritalStatus.text, "Getrouwd")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertTrue(inst.multipleBirthBoolean)
        self.assertEqual(inst.name[0].family, "van de Heuvel")
        self.assertEqual(inst.name[0].given[0], "Pieter")
        self.assertEqual(inst.name[0].suffix[0], "MSc")
        self.assertEqual(inst.name[0].use, "usual")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "mobile")
        self.assertEqual(inst.telecom[0].value, "0648352638")
        self.assertEqual(inst.telecom[1].system, "email")
        self.assertEqual(inst.telecom[1].use, "home")
        self.assertEqual(inst.telecom[1].value, "p.heuvel@gmail.com")
        self.assertEqual(inst.text.status, "generated")
    
    def testPatient3(self):
        inst = self.instantiate_from("patient-example-d.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient3(inst)
        
        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient3(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implPatient3(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.birthDate.date, FHIRDate("1982-08-02").date)
        self.assertEqual(inst.birthDate.as_json(), "1982-08-02")
        self.assertTrue(inst.deceasedBoolean)
        self.assertEqual(inst.gender, "female")
        self.assertEqual(inst.id, "pat4")
        self.assertEqual(inst.identifier[0].system, "urn:oid:0.1.2.3.4.5.6.7")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "MR")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0203")
        self.assertEqual(inst.identifier[0].use, "usual")
        self.assertEqual(inst.identifier[0].value, "123458")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].family, "Notsowell")
        self.assertEqual(inst.name[0].given[0], "Sandy")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.text.status, "generated")
    
    def testPatient4(self):
        inst = self.instantiate_from("patient-example-infant-twin-1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient4(inst)
        
        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient4(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implPatient4(self, inst):
        self.assertEqual(inst.birthDate.date, FHIRDate("2017-05-15").date)
        self.assertEqual(inst.birthDate.as_json(), "2017-05-15")
        self.assertEqual(inst.contact[0].name.family, "Organa")
        self.assertEqual(inst.contact[0].name.given[0], "Leia")
        self.assertEqual(inst.contact[0].name.use, "maiden")
        self.assertEqual(inst.contact[0].relationship[0].coding[0].code, "72705000")
        self.assertEqual(inst.contact[0].relationship[0].coding[0].display, "Mother")
        self.assertEqual(inst.contact[0].relationship[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.contact[0].relationship[0].coding[1].code, "N")
        self.assertEqual(inst.contact[0].relationship[0].coding[1].system, "http://terminology.hl7.org/CodeSystem/v2-0131")
        self.assertEqual(inst.contact[0].relationship[0].coding[2].code, "MTH")
        self.assertEqual(inst.contact[0].relationship[0].coding[2].system, "http://terminology.hl7.org/CodeSystem/v3-RoleCode")
        self.assertEqual(inst.contact[0].telecom[0].system, "phone")
        self.assertEqual(inst.contact[0].telecom[0].use, "mobile")
        self.assertEqual(inst.contact[0].telecom[0].value, "+31201234567")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName")
        self.assertEqual(inst.extension[0].valueString, "Organa")
        self.assertEqual(inst.gender, "female")
        self.assertEqual(inst.id, "infant-twin-1")
        self.assertEqual(inst.identifier[0].system, "http://coruscanthealth.org/main-hospital/patient-identifier")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "MR")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0203")
        self.assertEqual(inst.identifier[0].value, "MRN7465737865")
        self.assertEqual(inst.identifier[1].system, "http://new-republic.gov/galactic-citizen-identifier")
        self.assertEqual(inst.identifier[1].value, "7465737865")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.multipleBirthInteger, 1)
        self.assertEqual(inst.name[0].family, "Solo")
        self.assertEqual(inst.name[0].given[0], "Jaina")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.text.status, "generated")
    
    def testPatient5(self):
        inst = self.instantiate_from("patient-example-ncpi-ig-3.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient5(inst)
        
        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient5(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implPatient5(self, inst):
        self.assertEqual(inst.address[0].city, "Philadelphia")
        self.assertEqual(inst.address[0].line[0], "3401 Civic Center Blvd.")
        self.assertEqual(inst.address[0].postalCode, "19104")
        self.assertEqual(inst.address[0].state, "PA")
        self.assertEqual(inst.address[0].text, "3401 Civic Center Blvd., Philadelphia, PA 19104")
        self.assertEqual(inst.address[0].type, "both")
        self.assertEqual(inst.address[0].use, "home")
        self.assertEqual(inst.contact[0].address.city, "Philadelphia")
        self.assertEqual(inst.contact[0].address.line[0], "3401 Civic Center Blvd.")
        self.assertEqual(inst.contact[0].address.postalCode, "19104")
        self.assertEqual(inst.contact[0].address.state, "PA")
        self.assertEqual(inst.contact[0].address.text, "3401 Civic Center Blvd., Philadelphia, PA 19104")
        self.assertEqual(inst.contact[0].address.type, "both")
        self.assertEqual(inst.contact[0].address.use, "home")
        self.assertEqual(inst.contact[0].gender, "female")
        self.assertEqual(inst.contact[0].name.family, "Smith")
        self.assertEqual(inst.contact[0].name.given[0], "Jane")
        self.assertEqual(inst.contact[0].name.given[1], "Samantha")
        self.assertEqual(inst.contact[0].name.text, "Jane Samantha Smith")
        self.assertEqual(inst.contact[0].name.use, "official")
        self.assertEqual(inst.contact[0].relationship[0].coding[0].code, "C")
        self.assertEqual(inst.contact[0].relationship[0].coding[0].display, "Emergency Contact")
        self.assertEqual(inst.contact[0].relationship[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0131")
        self.assertEqual(inst.contact[0].relationship[0].text, "Spouse")
        self.assertEqual(inst.contact[0].telecom[0].rank, 1)
        self.assertEqual(inst.contact[0].telecom[0].system, "phone")
        self.assertEqual(inst.contact[0].telecom[0].use, "home")
        self.assertEqual(inst.contact[0].telecom[0].value, "(555) 555-5555")
        self.assertEqual(inst.extension[0].extension[0].url, "ombCategory")
        self.assertEqual(inst.extension[0].extension[0].valueCoding.code, "2106-3")
        self.assertEqual(inst.extension[0].extension[0].valueCoding.display, "White")
        self.assertEqual(inst.extension[0].extension[0].valueCoding.system, "urn:oid:2.16.840.1.113883.6.238")
        self.assertEqual(inst.extension[0].extension[1].url, "detailed")
        self.assertEqual(inst.extension[0].extension[1].valueCoding.code, "2113-9")
        self.assertEqual(inst.extension[0].extension[1].valueCoding.display, "Irish")
        self.assertEqual(inst.extension[0].extension[1].valueCoding.system, "urn:oid:2.16.840.1.113883.6.238")
        self.assertEqual(inst.extension[0].extension[2].url, "text")
        self.assertEqual(inst.extension[0].extension[2].valueString, "White")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race")
        self.assertEqual(inst.extension[1].extension[0].url, "ombCategory")
        self.assertEqual(inst.extension[1].extension[0].valueCoding.code, "2186-5")
        self.assertEqual(inst.extension[1].extension[0].valueCoding.display, "Not Hispanic or Latino")
        self.assertEqual(inst.extension[1].extension[0].valueCoding.system, "urn:oid:2.16.840.1.113883.6.238")
        self.assertEqual(inst.extension[1].extension[1].url, "text")
        self.assertEqual(inst.extension[1].extension[1].valueString, "Not Hispanic or Latino")
        self.assertEqual(inst.extension[1].url, "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "patient-example-3")
        self.assertEqual(inst.name[0].family, "Smith")
        self.assertEqual(inst.name[0].given[0], "Jone")
        self.assertEqual(inst.name[0].given[1], "Samuel")
        self.assertEqual(inst.name[0].text, "John Samuel Smith")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.telecom[0].rank, 1)
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "home")
        self.assertEqual(inst.telecom[0].value, "(555) 555-5555")
        self.assertEqual(inst.text.status, "extensions")
    
    def testPatient6(self):
        inst = self.instantiate_from("patient-example-infant-mom.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient6(inst)
        
        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient6(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implPatient6(self, inst):
        self.assertEqual(inst.birthDate.date, FHIRDate("1995-10-12").date)
        self.assertEqual(inst.birthDate.as_json(), "1995-10-12")
        self.assertEqual(inst.gender, "female")
        self.assertEqual(inst.id, "infant-mom")
        self.assertEqual(inst.maritalStatus.coding[0].code, "M")
        self.assertEqual(inst.maritalStatus.coding[0].display, "Married")
        self.assertEqual(inst.maritalStatus.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].family, "Solo")
        self.assertEqual(inst.name[0].given[0], "Leia")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.name[1].family, "Organa")
        self.assertEqual(inst.name[1].given[0], "Leia")
        self.assertEqual(inst.name[1].use, "maiden")
        self.assertEqual(inst.text.status, "generated")
    
    def testPatient7(self):
        inst = self.instantiate_from("patient-example-newborn.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient7(inst)
        
        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient7(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implPatient7(self, inst):
        self.assertEqual(inst.birthDate.date, FHIRDate("2017-09-05").date)
        self.assertEqual(inst.birthDate.as_json(), "2017-09-05")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName")
        self.assertEqual(inst.extension[0].valueString, "Everywoman")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "newborn")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.multipleBirthInteger, 2)
        self.assertEqual(inst.text.status, "generated")
    
    def testPatient8(self):
        inst = self.instantiate_from("patient-example-infant-fetal.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient8(inst)
        
        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient8(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implPatient8(self, inst):
        self.assertEqual(inst.contact[0].name.family, "Organa")
        self.assertEqual(inst.contact[0].name.given[0], "Leia")
        self.assertEqual(inst.contact[0].name.use, "maiden")
        self.assertEqual(inst.contact[0].relationship[0].coding[0].code, "72705000")
        self.assertEqual(inst.contact[0].relationship[0].coding[0].display, "Mother")
        self.assertEqual(inst.contact[0].relationship[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.contact[0].relationship[0].coding[1].code, "N")
        self.assertEqual(inst.contact[0].relationship[0].coding[1].system, "http://terminology.hl7.org/CodeSystem/v2-0131")
        self.assertEqual(inst.contact[0].relationship[0].coding[2].code, "MTH")
        self.assertEqual(inst.contact[0].relationship[0].coding[2].system, "http://terminology.hl7.org/CodeSystem/v3-RoleCode")
        self.assertEqual(inst.contact[0].telecom[0].system, "phone")
        self.assertEqual(inst.contact[0].telecom[0].use, "mobile")
        self.assertEqual(inst.contact[0].telecom[0].value, "+31201234567")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName")
        self.assertEqual(inst.extension[0].valueString, "Organa")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "infant-fetal")
        self.assertEqual(inst.identifier[0].system, "http://coruscanthealth.org/main-hospital/patient-identifier")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "MR")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0203")
        self.assertEqual(inst.identifier[0].value, "MRN657865757378")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "generated")
    
    def testPatient9(self):
        inst = self.instantiate_from("patient-genetics-example1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient9(inst)
        
        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient9(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implPatient9(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].line[0], "2222 Home Street")
        self.assertEqual(inst.address[0].use, "home")
        self.assertEqual(inst.birthDate.date, FHIRDate("1973-05-31").date)
        self.assertEqual(inst.birthDate.as_json(), "1973-05-31")
        self.assertEqual(inst.gender, "female")
        self.assertEqual(inst.id, "genetics-example1")
        self.assertEqual(inst.identifier[0].system, "http://hl7.org/fhir/sid/us-ssn")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "SS")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0203")
        self.assertEqual(inst.identifier[0].value, "444222222")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].family, "Everywoman")
        self.assertEqual(inst.name[0].given[0], "Eve")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "555-555-2003")
        self.assertEqual(inst.text.status, "generated")
    
    def testPatient10(self):
        inst = self.instantiate_from("patient-example-b.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient10(inst)
        
        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient10(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implPatient10(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.gender, "other")
        self.assertEqual(inst.id, "pat2")
        self.assertEqual(inst.identifier[0].system, "urn:oid:0.1.2.3.4.5.6.7")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "MR")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0203")
        self.assertEqual(inst.identifier[0].use, "usual")
        self.assertEqual(inst.identifier[0].value, "123456")
        self.assertEqual(inst.link[0].type, "seealso")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].family, "Donald")
        self.assertEqual(inst.name[0].given[0], "Duck")
        self.assertEqual(inst.name[0].given[1], "D")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.photo[0].contentType, "image/gif")
        self.assertEqual(inst.text.status, "generated")

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