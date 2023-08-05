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

from . import contract

from .fhirdate import FHIRDate
import logging


class ContractTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Contract", js["resourceType"])
        return contract.Contract(js)
    
    def testContract1(self):
        inst = self.instantiate_from("pcd-example-notOrg.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract1(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract1(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implContract1(self, inst):
        self.assertEqual(inst.friendly[0].contentAttachment.title, "The terms of the consent in friendly consumer speak.")
        self.assertEqual(inst.id, "pcd-example-notOrg")
        self.assertEqual(inst.issued.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.issued.as_json(), "2015-11-18")
        self.assertEqual(inst.legal[0].contentAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.subType[0].coding[0].code, "Opt-In")
        self.assertEqual(inst.subType[0].coding[0].display, "Default Authorization with exceptions.")
        self.assertEqual(inst.subType[0].coding[0].system, "http://www.infoway-inforoute.ca.org/Consent-subtype-codes")
        self.assertEqual(inst.term[0].offer.text, "Withhold this order and any results or related objects from any provider.")
        self.assertEqual(inst.term[0].type.coding[0].code, "withhold-from")
        self.assertEqual(inst.term[0].type.coding[0].display, "Withhold all data from specified actor entity.")
        self.assertEqual(inst.term[0].type.coding[0].system, "http://example.org/fhir/consent-term-type-codes")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "57016-8")
        self.assertEqual(inst.type.coding[0].system, "http://loinc.org")
    
    def testContract2(self):
        inst = self.instantiate_from("contract-example-ins-policy.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract2(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract2(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implContract2(self, inst):
        self.assertEqual(inst.applies.start.date, FHIRDate("2017-01-01").date)
        self.assertEqual(inst.applies.start.as_json(), "2017-01-01")
        self.assertEqual(inst.id, "INS-101")
        self.assertEqual(inst.identifier[0].system, "http://xyz-insurance.com/forms")
        self.assertEqual(inst.identifier[0].value, "YCSCWLN(01-2017)")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.term[0].asset[0].period[0].start.date, FHIRDate("2017-06-01").date)
        self.assertEqual(inst.term[0].asset[0].period[0].start.as_json(), "2017-06-01")
        self.assertEqual(inst.term[0].asset[0].subtype[0].text, "sample")
        self.assertEqual(inst.term[0].asset[0].type[0].coding[0].code, "RicardianContract")
        self.assertEqual(inst.term[0].asset[0].type[0].coding[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].effectiveTime.date, FHIRDate("1995").date)
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].effectiveTime.as_json(), "1995")
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].entityCodeableConcept.text, "Ford Bobcat")
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].factor, 1.0)
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].identifier.system, "http://somewhere.motor-vehicle.com/vin")
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].identifier.value, "XXSVT34-7665t952236")
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].net.currency, "CAD")
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].net.value, 200.0)
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].points, 1.0)
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].quantity.value, 1)
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].unitPrice.currency, "CAD")
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].unitPrice.value, 200.0)
        self.assertEqual(inst.term[0].group[0].offer.text, "Eligible Providers")
        self.assertEqual(inst.term[0].group[1].offer.text, "Responsibility for Payment")
        self.assertEqual(inst.term[0].group[2].group[0].group[0].offer.text, "Emergency Room Copay")
        self.assertEqual(inst.term[0].group[2].group[0].group[1].offer.text, "Professional Visit Copay")
        self.assertEqual(inst.term[0].group[2].group[0].offer.text, "Copays")
        self.assertEqual(inst.term[0].group[2].group[1].offer.text, "Calendar Year Deductible")
        self.assertEqual(inst.term[0].group[2].group[2].offer.text, "Out-Of-Pocket Maximum")
        self.assertEqual(inst.term[0].group[2].group[3].group[0].offer.text, "Ambulance Services")
        self.assertEqual(inst.term[0].group[2].group[3].group[1].offer.text, "Dental Services")
        self.assertEqual(inst.term[0].group[2].group[3].group[2].offer.text, "Diagnostic Services")
        self.assertEqual(inst.term[0].group[2].group[3].group[3].offer.text, "Emergency Room Services")
        self.assertEqual(inst.term[0].group[2].group[3].group[4].offer.text, "Hospital Inpatient Care")
        self.assertEqual(inst.term[0].group[2].group[3].offer.text, "Medical Services")
        self.assertEqual(inst.term[0].group[2].offer.text, "List of Benefits")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "healthinsurance")
        self.assertEqual(inst.type.coding[0].display, "Health Insurance")
        self.assertEqual(inst.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/contract-type")
    
    def testContract3(self):
        inst = self.instantiate_from("contract-example-42cfr-part2.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract3(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract3(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implContract3(self, inst):
        self.assertEqual(inst.applies.start.date, FHIRDate("2013-11-01T21:18:27-04:00").date)
        self.assertEqual(inst.applies.start.as_json(), "2013-11-01T21:18:27-04:00")
        self.assertEqual(inst.contentDerivative.coding[0].code, "registration")
        self.assertEqual(inst.contentDerivative.coding[0].system, "http://terminology.hl7.org/CodeSystem/contract-content-derivative")
        self.assertEqual(inst.id, "C-2121")
        self.assertEqual(inst.issued.date, FHIRDate("2013-11-01T21:18:27-04:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-11-01T21:18:27-04:00")
        self.assertEqual(inst.legal[0].contentAttachment.contentType, "application/pdf")
        self.assertEqual(inst.legal[0].contentAttachment.language, "en-US")
        self.assertEqual(inst.legal[0].contentAttachment.title, "MDHHS-5515 Consent To Share Your Health Information")
        self.assertEqual(inst.legal[0].contentAttachment.url, "http://org.mihin.ecms/ConsentDirective-2121")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2016-07-19T18:18:42.108-04:00").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2016-07-19T18:18:42.108-04:00")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.meta.versionId, "1")
        self.assertEqual(inst.signer[0].signature[0].type[0].code, "1.2.840.10065.1.12.1.1")
        self.assertEqual(inst.signer[0].signature[0].type[0].system, "urn:iso-astm:E1762-95:2013")
        self.assertEqual(inst.signer[0].signature[0].when.date, FHIRDate("2017-02-08T10:57:34+01:00").date)
        self.assertEqual(inst.signer[0].signature[0].when.as_json(), "2017-02-08T10:57:34+01:00")
        self.assertEqual(inst.signer[0].type.code, "SELF")
        self.assertEqual(inst.signer[0].type.system, "http://mdhhs.org/fhir/consent-signer-type")
        self.assertEqual(inst.status, "executed")
        self.assertEqual(inst.subType[0].coding[0].code, "hcd")
        self.assertEqual(inst.subType[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/consentcategorycodes")
        self.assertEqual(inst.term[0].action[0].intent.coding[0].code, "HPRGRP")
        self.assertEqual(inst.term[0].action[0].intent.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.term[0].action[0].status.text, "Sample")
        self.assertEqual(inst.term[0].action[0].subject[0].role.coding[0].code, "IR")
        self.assertEqual(inst.term[0].action[0].subject[0].role.coding[0].display, "Recipient")
        self.assertEqual(inst.term[0].action[0].subject[0].role.coding[0].system, "http://mdhhs.org/fhir/consent-actor-type")
        self.assertEqual(inst.term[0].action[0].subject[0].role.text, "Recipient of restricted health information")
        self.assertEqual(inst.term[0].action[0].subject[1].role.coding[0].code, "IS")
        self.assertEqual(inst.term[0].action[0].subject[1].role.coding[0].display, "Sender")
        self.assertEqual(inst.term[0].action[0].subject[1].role.coding[0].system, "http://mdhhs.org/fhir/consent-actor-type")
        self.assertEqual(inst.term[0].action[0].subject[1].role.text, "Sender of restricted health information")
        self.assertEqual(inst.term[0].action[0].type.coding[0].code, "action-a")
        self.assertEqual(inst.term[0].action[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/contractaction")
        self.assertEqual(inst.term[0].asset[0].period[0].end.date, FHIRDate("2019-11-01T21:18:27-04:00").date)
        self.assertEqual(inst.term[0].asset[0].period[0].end.as_json(), "2019-11-01T21:18:27-04:00")
        self.assertEqual(inst.term[0].asset[0].period[0].start.date, FHIRDate("2013-11-01T21:18:27-04:00").date)
        self.assertEqual(inst.term[0].asset[0].period[0].start.as_json(), "2013-11-01T21:18:27-04:00")
        self.assertEqual(inst.term[0].offer.decision.coding[0].code, "OPTIN")
        self.assertEqual(inst.term[0].offer.decision.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.term[0].offer.text, "Can't refuse")
        self.assertEqual(inst.term[0].offer.type.coding[0].code, "statutory")
        self.assertEqual(inst.term[0].offer.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/contracttermtypecodes")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "OPTIN")
        self.assertEqual(inst.type.coding[0].system, "http://mdhhs.org/fhir/consentdirective-type")
        self.assertEqual(inst.type.text, "Opt-in consent directive")
    
    def testContract4(self):
        inst = self.instantiate_from("pcd-example-notLabs.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract4(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract4(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implContract4(self, inst):
        self.assertEqual(inst.friendly[0].contentAttachment.title, "The terms of the consent in friendly consumer speak.")
        self.assertEqual(inst.id, "pcd-example-notLabs")
        self.assertEqual(inst.issued.date, FHIRDate("2014-08-17").date)
        self.assertEqual(inst.issued.as_json(), "2014-08-17")
        self.assertEqual(inst.legal[0].contentAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.subType[0].coding[0].code, "Opt-In")
        self.assertEqual(inst.subType[0].coding[0].display, "Default Authorization with exceptions.")
        self.assertEqual(inst.subType[0].coding[0].system, "http://www.infoway-inforoute.ca.org/Consent-subtype-codes")
        self.assertEqual(inst.term[0].group[0].offer.text, "Withhold orders from any provider.")
        self.assertEqual(inst.term[0].group[0].subType.coding[0].code, "ServiceRequest")
        self.assertEqual(inst.term[0].group[0].subType.coding[0].system, "http://hl7.org/fhir/resource-types")
        self.assertEqual(inst.term[0].group[0].type.coding[0].code, "withhold-object-type")
        self.assertEqual(inst.term[0].group[0].type.coding[0].system, "http://example.org/fhir/consent-term-type-codes")
        self.assertEqual(inst.term[0].group[1].offer.text, "Withhold order results from any provider.")
        self.assertEqual(inst.term[0].group[1].subType.coding[0].code, "DiagnosticReport")
        self.assertEqual(inst.term[0].group[1].subType.coding[0].system, "http://hl7.org/fhir/resource-types")
        self.assertEqual(inst.term[0].group[1].type.coding[0].code, "withhold-object-type")
        self.assertEqual(inst.term[0].group[1].type.coding[0].system, "http://example.org/fhir/consent-term-type-codes")
        self.assertEqual(inst.term[0].offer.text, "sample")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "57016-8")
        self.assertEqual(inst.type.coding[0].system, "http://loinc.org")
    
    def testContract5(self):
        inst = self.instantiate_from("pcd-example-notThem.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract5(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract5(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implContract5(self, inst):
        self.assertEqual(inst.friendly[0].contentAttachment.title, "The terms of the consent in friendly consumer speak.")
        self.assertEqual(inst.id, "pcd-example-notThem")
        self.assertEqual(inst.issued.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.issued.as_json(), "2015-11-18")
        self.assertEqual(inst.legal[0].contentAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.signer[0].signature[0].type[0].code, "1.2.840.10065.1.12.1.1")
        self.assertEqual(inst.signer[0].signature[0].type[0].system, "urn:iso-astm:E1762-95:2013")
        self.assertEqual(inst.signer[0].signature[0].when.date, FHIRDate("2013-06-08T10:57:34-07:00").date)
        self.assertEqual(inst.signer[0].signature[0].when.as_json(), "2013-06-08T10:57:34-07:00")
        self.assertEqual(inst.signer[0].type.code, "COVPTY")
        self.assertEqual(inst.signer[0].type.system, "http://terminology.hl7.org/CodeSystem/contractsignertypecodes")
        self.assertEqual(inst.subType[0].coding[0].code, "Opt-In")
        self.assertEqual(inst.subType[0].coding[0].display, "Default Authorization with exceptions.")
        self.assertEqual(inst.subType[0].coding[0].system, "http://www.infoway-inforoute.ca.org/Consent-subtype-codes")
        self.assertEqual(inst.term[0].offer.text, "Withhold this order and any results or related objects from specified nurse provider.")
        self.assertEqual(inst.term[0].type.coding[0].code, "withhold-from")
        self.assertEqual(inst.term[0].type.coding[0].display, "Withhold all data from specified actor entity.")
        self.assertEqual(inst.term[0].type.coding[0].system, "http://example.org/fhir/consent-term-type-codes")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "57016-8")
        self.assertEqual(inst.type.coding[0].system, "http://loinc.org")
    
    def testContract6(self):
        inst = self.instantiate_from("pcd-example-notAuthor.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract6(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract6(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implContract6(self, inst):
        self.assertEqual(inst.friendly[0].contentAttachment.title, "The terms of the consent in friendly consumer speak.")
        self.assertEqual(inst.id, "pcd-example-notAuthor")
        self.assertEqual(inst.issued.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.issued.as_json(), "2015-11-18")
        self.assertEqual(inst.legal[0].contentAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.subType[0].coding[0].code, "Opt-In")
        self.assertEqual(inst.subType[0].coding[0].display, "Default Authorization with exceptions.")
        self.assertEqual(inst.subType[0].coding[0].system, "http://www.infoway-inforoute.ca.org/Consent-subtype-codes")
        self.assertEqual(inst.term[0].offer.text, "Withhold all data authored by Good Health provider.")
        self.assertEqual(inst.term[0].type.coding[0].code, "withhold-authored-by")
        self.assertEqual(inst.term[0].type.coding[0].display, "Withhold all data authored by specified actor entity.")
        self.assertEqual(inst.term[0].type.coding[0].system, "http://example.org/fhir/consent-term-type-codes")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "57016-8")
        self.assertEqual(inst.type.coding[0].system, "http://loinc.org")
    
    def testContract7(self):
        inst = self.instantiate_from("contract-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract7(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract7(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implContract7(self, inst):
        self.assertEqual(inst.id, "C-123")
        self.assertEqual(inst.identifier[0].system, "http://happyvalley.com/contract")
        self.assertEqual(inst.identifier[0].value, "12347")
        self.assertEqual(inst.legallyBindingAttachment.contentType, "application/pdf")
        self.assertEqual(inst.legallyBindingAttachment.url, "http://www.aws3.com/storage/doc.pdf")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.rule[0].contentAttachment.contentType, "application/txt")
        self.assertEqual(inst.rule[0].contentAttachment.url, "http://www.rfc-editor.org/bcp/bcp13.txt")
        self.assertEqual(inst.term[0].asset[0].period[0].start.date, FHIRDate("2017-06-01").date)
        self.assertEqual(inst.term[0].asset[0].period[0].start.as_json(), "2017-06-01")
        self.assertEqual(inst.term[0].asset[0].subtype[0].text, "sample")
        self.assertEqual(inst.term[0].asset[0].type[0].coding[0].code, "RicardianContract")
        self.assertEqual(inst.term[0].asset[0].type[0].coding[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].effectiveTime.date, FHIRDate("1995").date)
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].effectiveTime.as_json(), "1995")
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].entityCodeableConcept.text, "Ford Bobcat")
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].factor, 1.0)
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].identifier.system, "http://somewhere.motor-vehicle.com/vin")
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].identifier.value, "XXSVT34-7665t952236")
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].net.currency, "CAD")
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].net.value, 200.0)
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].points, 1.0)
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].quantity.value, 1)
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].unitPrice.currency, "CAD")
        self.assertEqual(inst.term[0].asset[0].valuedItem[0].unitPrice.value, 200.0)
        self.assertEqual(inst.term[0].offer.text, "Can't refuse")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the contract</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testContract8(self):
        inst = self.instantiate_from("pcd-example-notThis.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract8(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract8(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implContract8(self, inst):
        self.assertEqual(inst.friendly[0].contentAttachment.title, "The terms of the consent in friendly consumer speak.")
        self.assertEqual(inst.id, "pcd-example-notThis")
        self.assertEqual(inst.issued.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.issued.as_json(), "2015-11-18")
        self.assertEqual(inst.legal[0].contentAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.subType[0].coding[0].code, "Opt-In")
        self.assertEqual(inst.subType[0].coding[0].display, "Default Authorization with exceptions.")
        self.assertEqual(inst.subType[0].coding[0].system, "http://www.infoway-inforoute.ca.org/Consent-subtype-codes")
        self.assertEqual(inst.term[0].applies.start.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.term[0].applies.start.as_json(), "2015-11-18")
        self.assertEqual(inst.term[0].identifier.system, "http://example.org/fhir/term-items")
        self.assertEqual(inst.term[0].identifier.value, "3347689")
        self.assertEqual(inst.term[0].issued.date, FHIRDate("2015-11-01").date)
        self.assertEqual(inst.term[0].issued.as_json(), "2015-11-01")
        self.assertEqual(inst.term[0].offer.text, "Withhold this order and any results or related objects from any provider.")
        self.assertEqual(inst.term[0].type.coding[0].code, "withhold-identified-object-and-related")
        self.assertEqual(inst.term[0].type.coding[0].display, "Withhold the identified object and any other resources that are related to this object.")
        self.assertEqual(inst.term[0].type.coding[0].system, "http://example.org/fhir/consent-term-type-codes")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "57016-8")
        self.assertEqual(inst.type.coding[0].system, "http://loinc.org")

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