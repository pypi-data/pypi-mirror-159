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

from . import bundle

from .fhirdate import FHIRDate
import logging


class BundleTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Bundle", js["resourceType"])
        return bundle.Bundle(js)
    
    def testBundle1(self):
        inst = self.instantiate_from("diagnosticreport-example-f202-bloodculture.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle1(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle1(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implBundle1(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "https://example.com/base/DiagnosticReport/f202")
        self.assertEqual(inst.entry[0].resource.id, "f202")
        self.assertEqual(inst.entry[1].fullUrl, "https://example.com/base/ServiceRequest/req")
        self.assertEqual(inst.entry[1].resource.id, "req")
        self.assertEqual(inst.id, "f202")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.type, "collection")
    
    def testBundle2(self):
        inst = self.instantiate_from("xds-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle2(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle2(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implBundle2(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "urn:uuid:3fdc72f4-a11d-4a9d-9260-a9f745779e1d")
        self.assertEqual(inst.entry[0].request.method, "POST")
        self.assertEqual(inst.entry[0].request.url, "DocumentReference")
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(inst.entry[1].fullUrl, "http://localhost:9556/svc/fhir/Patient/a2")
        self.assertEqual(inst.entry[1].request.ifNoneExist, "Patient?identifier=http://acme.org/xds/patients!89765a87b")
        self.assertEqual(inst.entry[1].request.method, "POST")
        self.assertEqual(inst.entry[1].request.url, "Patient")
        self.assertEqual(inst.entry[1].resource.id, "a2")
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(inst.entry[2].fullUrl, "http://localhost:9556/svc/fhir/Practitioner/a3")
        self.assertEqual(inst.entry[2].request.method, "POST")
        self.assertEqual(inst.entry[2].request.url, "Practitioner")
        self.assertEqual(inst.entry[2].resource.id, "a3")
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(inst.entry[3].fullUrl, "http://localhost:9556/svc/fhir/Practitioner/a4")
        self.assertEqual(inst.entry[3].request.method, "POST")
        self.assertEqual(inst.entry[3].request.url, "Practitioner")
        self.assertEqual(inst.entry[3].resource.id, "a4")
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(inst.entry[4].fullUrl, "http://localhost:9556/svc/fhir/Binary/1e404af3-077f-4bee-b7a6-a9be97e1ce32")
        self.assertEqual(inst.entry[4].request.method, "POST")
        self.assertEqual(inst.entry[4].request.url, "Binary")
        self.assertEqual(inst.entry[4].resource.id, "1e404af3-077f-4bee-b7a6-a9be97e1ce32")
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(inst.id, "xds")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.type, "transaction")
    
    def testBundle3(self):
        inst = self.instantiate_from("diagnosticreport-example-ghp.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle3(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle3(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implBundle3(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "https://example.com/base/DiagnosticReport/ghp")
        self.assertEqual(inst.entry[0].resource.id, "ghp")
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRDate("2015-08-16T10:35:23Z").date)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), "2015-08-16T10:35:23Z")
        self.assertEqual(inst.entry[1].fullUrl, "https://example.com/base/Specimen/rtt")
        self.assertEqual(inst.entry[1].resource.id, "rtt")
        self.assertEqual(inst.entry[2].fullUrl, "https://example.com/base/Specimen/ltt")
        self.assertEqual(inst.entry[2].resource.id, "ltt")
        self.assertEqual(inst.entry[3].fullUrl, "https://example.com/base/Specimen/urine")
        self.assertEqual(inst.entry[3].resource.id, "urine")
        self.assertEqual(inst.entry[4].fullUrl, "https://example.com/base/Observation/p2")
        self.assertEqual(inst.entry[4].resource.id, "p2")
        self.assertEqual(inst.entry[5].fullUrl, "https://example.com/base/Observation/r1")
        self.assertEqual(inst.entry[5].resource.id, "r1")
        self.assertEqual(inst.entry[6].fullUrl, "https://example.com/base/Observation/r2")
        self.assertEqual(inst.entry[6].resource.id, "r2")
        self.assertEqual(inst.entry[7].fullUrl, "https://example.com/base/Observation/r3")
        self.assertEqual(inst.entry[7].resource.id, "r3")
        self.assertEqual(inst.entry[8].fullUrl, "https://example.com/base/Observation/r4")
        self.assertEqual(inst.entry[8].resource.id, "r4")
        self.assertEqual(inst.entry[9].fullUrl, "https://example.com/base/Observation/r5")
        self.assertEqual(inst.entry[9].resource.id, "r5")
        self.assertEqual(inst.id, "ghp")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.type, "collection")
    
    def testBundle4(self):
        inst = self.instantiate_from("practitioner-examples-general.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle4(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle4(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implBundle4(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "http://hl7.org/fhir/Practitioner/1")
        self.assertEqual(inst.entry[0].resource.id, "1")
        self.assertEqual(inst.entry[1].fullUrl, "http://hl7.org/fhir/Practitioner/13")
        self.assertEqual(inst.entry[1].resource.id, "13")
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[2].fullUrl, "http://hl7.org/fhir/Practitioner/14")
        self.assertEqual(inst.entry[2].resource.id, "14")
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[3].fullUrl, "http://hl7.org/fhir/Practitioner/15")
        self.assertEqual(inst.entry[3].resource.id, "15")
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[4].fullUrl, "http://hl7.org/fhir/Practitioner/16")
        self.assertEqual(inst.entry[4].resource.id, "16")
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[5].fullUrl, "http://hl7.org/fhir/Practitioner/17")
        self.assertEqual(inst.entry[5].resource.id, "17")
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[6].fullUrl, "http://hl7.org/fhir/Practitioner/18")
        self.assertEqual(inst.entry[6].resource.id, "18")
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[7].fullUrl, "http://hl7.org/fhir/Practitioner/19")
        self.assertEqual(inst.entry[7].resource.id, "19")
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[8].fullUrl, "http://hl7.org/fhir/Practitioner/20")
        self.assertEqual(inst.entry[8].resource.id, "20")
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[9].fullUrl, "http://hl7.org/fhir/Practitioner/21")
        self.assertEqual(inst.entry[9].resource.id, "21")
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.id, "3ad0687e-f477-468c-afd5-fcc2bf897809")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.type, "collection")
    
    def testBundle5(self):
        inst = self.instantiate_from("diagnosticreport-example-lipids.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle5(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle5(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implBundle5(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "https://example.com/base/DiagnosticReport/lipids")
        self.assertEqual(inst.entry[0].resource.id, "lipids")
        self.assertEqual(inst.entry[1].fullUrl, "https://example.com/base/Observation/cholesterol")
        self.assertEqual(inst.entry[1].resource.id, "cholesterol")
        self.assertEqual(inst.entry[2].fullUrl, "https://example.com/base/Observation/triglyceride")
        self.assertEqual(inst.entry[2].resource.id, "triglyceride")
        self.assertEqual(inst.entry[3].fullUrl, "https://example.com/base/Observation/hdlcholesterol")
        self.assertEqual(inst.entry[3].resource.id, "hdlcholesterol")
        self.assertEqual(inst.entry[4].fullUrl, "https://example.com/base/Observation/ldlcholesterol")
        self.assertEqual(inst.entry[4].resource.id, "ldlcholesterol")
        self.assertEqual(inst.id, "lipids")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.type, "collection")
    
    def testBundle6(self):
        inst = self.instantiate_from("diagnosticreport-hla-genetics-results-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle6(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle6(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implBundle6(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "urn:uuid:b0a4b18e-94e7-4b1b-8031-c7ae4bdd8db9")
        self.assertEqual(inst.entry[0].request.method, "POST")
        self.assertEqual(inst.entry[0].request.url, "DiagnosticReport")
        self.assertEqual(inst.entry[1].fullUrl, "urn:uuid:8200dab6-18a2-4550-b913-a7db480c0804")
        self.assertEqual(inst.entry[1].request.method, "POST")
        self.assertEqual(inst.entry[1].request.url, "MolecularSequence")
        self.assertEqual(inst.entry[2].fullUrl, "urn:uuid:7c393185-f15c-45bc-a714-c0fdbea32675")
        self.assertEqual(inst.entry[2].request.method, "POST")
        self.assertEqual(inst.entry[2].request.url, "MolecularSequence")
        self.assertEqual(inst.entry[3].fullUrl, "urn:uuid:65c85f14-c3a0-4b72-818f-820e04fcc621")
        self.assertEqual(inst.entry[3].request.method, "POST")
        self.assertEqual(inst.entry[3].request.url, "MolecularSequence")
        self.assertEqual(inst.entry[4].fullUrl, "urn:uuid:fbba9fe7-0ece-4ec1-9233-a437a8d242a0")
        self.assertEqual(inst.entry[4].request.method, "POST")
        self.assertEqual(inst.entry[4].request.url, "MolecularSequence")
        self.assertEqual(inst.entry[5].fullUrl, "urn:uuid:cbabf93e-1b4b-46f2-ba1e-d84862670670")
        self.assertEqual(inst.entry[5].request.method, "POST")
        self.assertEqual(inst.entry[5].request.url, "MolecularSequence")
        self.assertEqual(inst.entry[6].fullUrl, "urn:uuid:c233ad3d-1572-48d6-93da-0a583535e138")
        self.assertEqual(inst.entry[6].request.method, "POST")
        self.assertEqual(inst.entry[6].request.url, "MolecularSequence")
        self.assertEqual(inst.entry[7].fullUrl, "urn:uuid:05fa52d7-5c67-460a-8722-d3460b24d6fe")
        self.assertEqual(inst.entry[7].request.method, "POST")
        self.assertEqual(inst.entry[7].request.url, "MolecularSequence")
        self.assertEqual(inst.entry[8].fullUrl, "urn:uuid:db69e549-6267-4777-b4b9-8813f3329309")
        self.assertEqual(inst.entry[8].request.method, "POST")
        self.assertEqual(inst.entry[8].request.url, "MolecularSequence")
        self.assertEqual(inst.entry[9].fullUrl, "urn:uuid:bb55c2bc-5ad2-4bc1-8ff3-c407d06b12d0")
        self.assertEqual(inst.entry[9].request.method, "POST")
        self.assertEqual(inst.entry[9].request.url, "MolecularSequence")
        self.assertEqual(inst.id, "hla-1")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.type, "transaction")
    
    def testBundle7(self):
        inst = self.instantiate_from("practitionerrole-examples-general.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle7(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle7(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implBundle7(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "http://hl7.org/fhir/PractitionerRole/f003-0")
        self.assertEqual(inst.entry[0].resource.id, "f003-0")
        self.assertEqual(inst.entry[1].fullUrl, "http://hl7.org/fhir/PractitionerRole/example-0")
        self.assertEqual(inst.entry[1].resource.id, "example-0")
        self.assertEqual(inst.entry[2].fullUrl, "http://hl7.org/fhir/PractitionerRole/example-1")
        self.assertEqual(inst.entry[2].resource.id, "example-1")
        self.assertEqual(inst.entry[3].fullUrl, "http://hl7.org/fhir/PractitionerRole/example-2")
        self.assertEqual(inst.entry[3].resource.id, "example-2")
        self.assertEqual(inst.entry[4].fullUrl, "http://hl7.org/fhir/PractitionerRole/f007-0")
        self.assertEqual(inst.entry[4].resource.id, "f007-0")
        self.assertEqual(inst.entry[5].fullUrl, "http://hl7.org/fhir/PractitionerRole/f004-0")
        self.assertEqual(inst.entry[5].resource.id, "f004-0")
        self.assertEqual(inst.entry[6].fullUrl, "http://hl7.org/fhir/PractitionerRole/xcda1-0")
        self.assertEqual(inst.entry[6].resource.id, "xcda1-0")
        self.assertEqual(inst.entry[7].fullUrl, "http://hl7.org/fhir/PractitionerRole/f202-0")
        self.assertEqual(inst.entry[7].resource.id, "f202-0")
        self.assertEqual(inst.entry[8].fullUrl, "http://hl7.org/fhir/PractitionerRole/f201-0")
        self.assertEqual(inst.entry[8].resource.id, "f201-0")
        self.assertEqual(inst.entry[9].fullUrl, "http://hl7.org/fhir/PractitionerRole/f203-0")
        self.assertEqual(inst.entry[9].resource.id, "f203-0")
        self.assertEqual(inst.id, "3ad0687e-f477-468c-afd5-fcc2bf897808")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.type, "collection")
    
    def testBundle8(self):
        inst = self.instantiate_from("diagnosticreport-example-f001-bloodexam.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle8(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle8(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implBundle8(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "https://example.com/base/DiagnosticReport/f001")
        self.assertEqual(inst.entry[0].resource.id, "f001")
        self.assertEqual(inst.entry[1].fullUrl, "https://example.com/base/ServiceRequest/req")
        self.assertEqual(inst.entry[1].resource.id, "req")
        self.assertEqual(inst.id, "f001")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.type, "collection")
    
    def testBundle9(self):
        inst = self.instantiate_from("document-example-dischargesummary.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle9(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle9(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implBundle9(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "http://fhir.healthintersections.com.au/open/Composition/180f219f-97a8-486d-99d9-ed631fe4fc57")
        self.assertEqual(inst.entry[0].resource.id, "180f219f-97a8-486d-99d9-ed631fe4fc57")
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRDate("2013-05-28T22:12:21Z").date)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), "2013-05-28T22:12:21Z")
        self.assertEqual(inst.entry[1].fullUrl, "http://fhir.healthintersections.com.au/open/Practitioner/example")
        self.assertEqual(inst.entry[1].resource.id, "example")
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRDate("2013-05-05T16:13:03Z").date)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), "2013-05-05T16:13:03Z")
        self.assertEqual(inst.entry[2].fullUrl, "http://fhir.healthintersections.com.au/open/Patient/d1")
        self.assertEqual(inst.entry[2].resource.id, "d1")
        self.assertEqual(inst.entry[3].fullUrl, "http://fhir.healthintersections.com.au/open/Encounter/doc-example")
        self.assertEqual(inst.entry[3].resource.id, "doc-example")
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRDate("2013-05-05T16:13:03Z").date)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), "2013-05-05T16:13:03Z")
        self.assertEqual(inst.entry[4].fullUrl, "urn:uuid:541a72a8-df75-4484-ac89-ac4923f03b81")
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRDate("2013-05-05T16:13:03Z").date)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), "2013-05-05T16:13:03Z")
        self.assertEqual(inst.entry[5].fullUrl, "urn:uuid:124a6916-5d84-4b8c-b250-10cefb8e6e86")
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.date, FHIRDate("2013-05-05T16:13:03Z").date)
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.as_json(), "2013-05-05T16:13:03Z")
        self.assertEqual(inst.entry[6].fullUrl, "urn:uuid:673f8db5-0ffd-4395-9657-6da00420bbc1")
        self.assertEqual(inst.entry[7].fullUrl, "urn:uuid:47600e0f-b6b5-4308-84b5-5dec157f7637")
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.date, FHIRDate("2013-05-05T16:13:03Z").date)
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.as_json(), "2013-05-05T16:13:03Z")
        self.assertEqual(inst.id, "father")
        self.assertEqual(inst.identifier.system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier.value, "urn:uuid:0c3151bd-1cbf-4d64-b04d-cd9187a4c6e0")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2013-05-28T22:12:21Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2013-05-28T22:12:21Z")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.signature.sigFormat, "image/jpg")
        self.assertEqual(inst.signature.type[0].code, "1.2.840.10065.1.12.1.1")
        self.assertEqual(inst.signature.type[0].display, "Author's Signature")
        self.assertEqual(inst.signature.type[0].system, "urn:iso-astm:E1762-95:2013")
        self.assertEqual(inst.signature.when.date, FHIRDate("2015-08-31T07:42:33+10:00").date)
        self.assertEqual(inst.signature.when.as_json(), "2015-08-31T07:42:33+10:00")
        self.assertEqual(inst.timestamp.date, FHIRDate("2013-05-28T22:12:21Z").date)
        self.assertEqual(inst.timestamp.as_json(), "2013-05-28T22:12:21Z")
        self.assertEqual(inst.type, "document")
    
    def testBundle10(self):
        inst = self.instantiate_from("location-examples-general.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle10(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle10(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implBundle10(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "http://hl7.org/fhir/Location/2")
        self.assertEqual(inst.entry[0].resource.id, "2")
        self.assertEqual(inst.entry[1].fullUrl, "http://hl7.org/fhir/Location/3")
        self.assertEqual(inst.entry[1].resource.id, "3")
        self.assertEqual(inst.id, "3ad0687e-f477-468c-afd5-fcc2bf897819")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.type, "collection")

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