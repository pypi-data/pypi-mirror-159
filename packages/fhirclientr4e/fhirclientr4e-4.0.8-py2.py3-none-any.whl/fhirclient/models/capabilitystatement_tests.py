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

from . import capabilitystatement

from .fhirdate import FHIRDate
import logging


class CapabilityStatementTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CapabilityStatement", js["resourceType"])
        return capabilitystatement.CapabilityStatement(js)
    
    def testCapabilityStatement1(self):
        inst = self.instantiate_from("capabilitystatement-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CapabilityStatement instance")
        self.implCapabilityStatement1(inst)
        
        js = inst.as_json()
        self.assertEqual("CapabilityStatement", js["resourceType"])
        inst2 = capabilitystatement.CapabilityStatement(js)
        self.implCapabilityStatement1(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implCapabilityStatement1(self, inst):
        self.assertEqual(inst.contact[0].name, "System Administrator")
        self.assertEqual(inst.contact[0].telecom[0].system, "email")
        self.assertEqual(inst.contact[0].telecom[0].value, "wile@acme.org")
        self.assertEqual(inst.copyright, "Copyright © Acme Healthcare and GoodCorp EHR Systems")
        self.assertEqual(inst.date.date, FHIRDate("2012-01-04").date)
        self.assertEqual(inst.date.as_json(), "2012-01-04")
        self.assertEqual(inst.description, "This is the FHIR capability statement for the main EHR at ACME for the private interface - it does not describe the public interface")
        self.assertEqual(inst.document[0].documentation, "Basic rules for all documents in the EHR system")
        self.assertEqual(inst.document[0].mode, "consumer")
        self.assertEqual(inst.document[0].profile, "http://fhir.hl7.org/base/Profilebc054d23-75e1-4dc6-aca5-838b6b1ac81d/_history/b5fdd9fc-b021-4ea1-911a-721a60663796")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.fhirVersion, "4.0.1")
        self.assertEqual(inst.format[0], "xml")
        self.assertEqual(inst.format[1], "json")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.implementation.description, "main EHR at ACME")
        self.assertEqual(inst.implementation.url, "http://10.2.3.4/fhir")
        self.assertEqual(inst.implementationGuide[0], "http://hl7.org/fhir/us/lab")
        self.assertEqual(inst.instantiates[0], "http://ihe.org/fhir/CapabilityStatement/pixm-client")
        self.assertEqual(inst.jurisdiction[0].coding[0].code, "US")
        self.assertEqual(inst.jurisdiction[0].coding[0].display, "United States of America (the)")
        self.assertEqual(inst.jurisdiction[0].coding[0].system, "urn:iso:std:iso:3166")
        self.assertEqual(inst.kind, "instance")
        self.assertEqual(inst.messaging[0].documentation, "ADT A08 equivalent for external system notifications")
        self.assertEqual(inst.messaging[0].endpoint[0].address, "mllp:10.1.1.10:9234")
        self.assertEqual(inst.messaging[0].endpoint[0].protocol.code, "mllp")
        self.assertEqual(inst.messaging[0].endpoint[0].protocol.system, "http://terminology.hl7.org/CodeSystem/message-transport")
        self.assertEqual(inst.messaging[0].reliableCache, 30)
        self.assertEqual(inst.messaging[0].supportedMessage[0].definition, "MessageDefinition/example")
        self.assertEqual(inst.messaging[0].supportedMessage[0].mode, "receiver")
        self.assertEqual(inst.name, "ACME-EHR")
        self.assertEqual(inst.patchFormat[0], "application/xml-patch+xml")
        self.assertEqual(inst.patchFormat[1], "application/json-patch+json")
        self.assertEqual(inst.publisher, "ACME Corporation")
        self.assertEqual(inst.purpose, "Main EHR capability statement, published for contracting and operational support")
        self.assertEqual(inst.rest[0].compartment[0], "http://hl7.org/fhir/CompartmentDefinition/patient")
        self.assertEqual(inst.rest[0].documentation, "Main FHIR endpoint for acem health")
        self.assertEqual(inst.rest[0].interaction[0].code, "transaction")
        self.assertEqual(inst.rest[0].interaction[1].code, "history-system")
        self.assertEqual(inst.rest[0].mode, "server")
        self.assertTrue(inst.rest[0].resource[0].conditionalCreate)
        self.assertEqual(inst.rest[0].resource[0].conditionalDelete, "not-supported")
        self.assertEqual(inst.rest[0].resource[0].conditionalRead, "full-support")
        self.assertFalse(inst.rest[0].resource[0].conditionalUpdate)
        self.assertEqual(inst.rest[0].resource[0].documentation, "This server does not let the clients create identities.")
        self.assertEqual(inst.rest[0].resource[0].interaction[0].code, "read")
        self.assertEqual(inst.rest[0].resource[0].interaction[1].code, "vread")
        self.assertEqual(inst.rest[0].resource[0].interaction[1].documentation, "Only supported for patient records since 12-Dec 2012")
        self.assertEqual(inst.rest[0].resource[0].interaction[2].code, "update")
        self.assertEqual(inst.rest[0].resource[0].interaction[3].code, "history-instance")
        self.assertEqual(inst.rest[0].resource[0].interaction[4].code, "create")
        self.assertEqual(inst.rest[0].resource[0].interaction[5].code, "history-type")
        self.assertEqual(inst.rest[0].resource[0].profile, "http://registry.fhir.org/r4/StructureDefinition/7896271d-57f6-4231-89dc-dcc91eab2416")
        self.assertTrue(inst.rest[0].resource[0].readHistory)
        self.assertEqual(inst.rest[0].resource[0].searchInclude[0], "Organization")
        self.assertEqual(inst.rest[0].resource[0].searchParam[0].definition, "http://hl7.org/fhir/SearchParameter/Patient-identifier")
        self.assertEqual(inst.rest[0].resource[0].searchParam[0].documentation, "Only supports search by institution MRN")
        self.assertEqual(inst.rest[0].resource[0].searchParam[0].name, "identifier")
        self.assertEqual(inst.rest[0].resource[0].searchParam[0].type, "token")
        self.assertEqual(inst.rest[0].resource[0].searchParam[1].definition, "http://hl7.org/fhir/SearchParameter/Patient-general-practitioner")
        self.assertEqual(inst.rest[0].resource[0].searchParam[1].name, "general-practitioner")
        self.assertEqual(inst.rest[0].resource[0].searchParam[1].type, "reference")
        self.assertEqual(inst.rest[0].resource[0].searchRevInclude[0], "Person")
        self.assertEqual(inst.rest[0].resource[0].supportedProfile[0], "http://registry.fhir.org/r4/StructureDefinition/00ab9e7a-06c7-4f77-9234-4154ca1e3347")
        self.assertEqual(inst.rest[0].resource[0].type, "Patient")
        self.assertFalse(inst.rest[0].resource[0].updateCreate)
        self.assertEqual(inst.rest[0].resource[0].versioning, "versioned-update")
        self.assertTrue(inst.rest[0].security.cors)
        self.assertEqual(inst.rest[0].security.description, "See Smart on FHIR documentation")
        self.assertEqual(inst.rest[0].security.service[0].coding[0].code, "SMART-on-FHIR")
        self.assertEqual(inst.rest[0].security.service[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/restful-security-service")
        self.assertEqual(inst.software.name, "EHR")
        self.assertEqual(inst.software.releaseDate.date, FHIRDate("2012-01-04").date)
        self.assertEqual(inst.software.releaseDate.as_json(), "2012-01-04")
        self.assertEqual(inst.software.version, "0.00.020.2134")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "ACME EHR capability statement")
        self.assertEqual(inst.url, "urn:uuid:68D043B5-9ECF-4559-A57A-396E0D452311")
        self.assertEqual(inst.useContext[0].code.code, "focus")
        self.assertEqual(inst.useContext[0].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].code, "positive")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].system, "http://terminology.hl7.org/CodeSystem/variant-state")
        self.assertEqual(inst.version, "20130510")
    
    def testCapabilityStatement2(self):
        inst = self.instantiate_from("capabilitystatement-phr-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CapabilityStatement instance")
        self.implCapabilityStatement2(inst)
        
        js = inst.as_json()
        self.assertEqual("CapabilityStatement", js["resourceType"])
        inst2 = capabilitystatement.CapabilityStatement(js)
        self.implCapabilityStatement2(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implCapabilityStatement2(self, inst):
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.date.date, FHIRDate("2013-06-18").date)
        self.assertEqual(inst.date.as_json(), "2013-06-18")
        self.assertEqual(inst.description, "Prototype Capability Statement for September 2013 Connectathon")
        self.assertEqual(inst.fhirVersion, "4.0.1")
        self.assertEqual(inst.format[0], "json")
        self.assertEqual(inst.format[1], "xml")
        self.assertEqual(inst.id, "phr")
        self.assertEqual(inst.kind, "capability")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "PHR Template")
        self.assertEqual(inst.publisher, "FHIR Project")
        self.assertEqual(inst.rest[0].documentation, "Protoype server Capability Statement for September 2013 Connectathon")
        self.assertEqual(inst.rest[0].mode, "server")
        self.assertEqual(inst.rest[0].resource[0].interaction[0].code, "read")
        self.assertEqual(inst.rest[0].resource[0].interaction[1].code, "search-type")
        self.assertEqual(inst.rest[0].resource[0].interaction[1].documentation, "When a client searches patients with no search criteria, they get a list of all patients they have access too. Servers may elect to offer additional search parameters, but this is not required")
        self.assertEqual(inst.rest[0].resource[0].type, "Patient")
        self.assertEqual(inst.rest[0].resource[1].interaction[0].code, "read")
        self.assertEqual(inst.rest[0].resource[1].interaction[1].code, "search-type")
        self.assertEqual(inst.rest[0].resource[1].searchParam[0].documentation, "_id parameter always supported. For the connectathon, servers may elect which search parameters are supported")
        self.assertEqual(inst.rest[0].resource[1].searchParam[0].name, "_id")
        self.assertEqual(inst.rest[0].resource[1].searchParam[0].type, "token")
        self.assertEqual(inst.rest[0].resource[1].type, "DocumentReference")
        self.assertEqual(inst.rest[0].resource[2].interaction[0].code, "read")
        self.assertEqual(inst.rest[0].resource[2].interaction[1].code, "search-type")
        self.assertEqual(inst.rest[0].resource[2].searchParam[0].documentation, "Standard _id parameter")
        self.assertEqual(inst.rest[0].resource[2].searchParam[0].name, "_id")
        self.assertEqual(inst.rest[0].resource[2].searchParam[0].type, "token")
        self.assertEqual(inst.rest[0].resource[2].type, "Condition")
        self.assertEqual(inst.rest[0].resource[3].interaction[0].code, "read")
        self.assertEqual(inst.rest[0].resource[3].interaction[1].code, "search-type")
        self.assertEqual(inst.rest[0].resource[3].searchParam[0].documentation, "Standard _id parameter")
        self.assertEqual(inst.rest[0].resource[3].searchParam[0].name, "_id")
        self.assertEqual(inst.rest[0].resource[3].searchParam[0].type, "token")
        self.assertEqual(inst.rest[0].resource[3].searchParam[1].documentation, "which diagnostic discipline/department created the report")
        self.assertEqual(inst.rest[0].resource[3].searchParam[1].name, "service")
        self.assertEqual(inst.rest[0].resource[3].searchParam[1].type, "token")
        self.assertEqual(inst.rest[0].resource[3].type, "DiagnosticReport")
        self.assertEqual(inst.rest[0].security.service[0].text, "OAuth")
        self.assertEqual(inst.software.name, "ACME PHR Server")
        self.assertEqual(inst.status, "draft")
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