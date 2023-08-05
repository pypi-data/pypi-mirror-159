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

from . import organization

from .fhirdate import FHIRDate
import logging


class OrganizationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Organization", js["resourceType"])
        return organization.Organization(js)
    
    def testOrganization1(self):
        inst = self.instantiate_from("organization-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization1(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization1(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implOrganization1(self, inst):
        self.assertEqual(inst.address[0].city, "Ann Arbor")
        self.assertEqual(inst.address[0].country, "USA")
        self.assertEqual(inst.address[0].line[0], "3300 Washtenaw Avenue, Suite 227")
        self.assertEqual(inst.address[0].postalCode, "48104")
        self.assertEqual(inst.address[0].state, "MI")
        self.assertEqual(inst.alias[0], "HL7 International")
        self.assertEqual(inst.id, "hl7")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "Health Level Seven International")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].value, "(+1) 734-677-7777")
        self.assertEqual(inst.telecom[1].system, "fax")
        self.assertEqual(inst.telecom[1].value, "(+1) 734-677-6622")
        self.assertEqual(inst.telecom[2].system, "email")
        self.assertEqual(inst.telecom[2].value, "hq@HL7.org")
        self.assertEqual(inst.text.status, "generated")
    
    def testOrganization2(self):
        inst = self.instantiate_from("organization-example-mmanu.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization2(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization2(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implOrganization2(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].country, "Swizterland")
        self.assertEqual(inst.id, "mmanu")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "Acme Corporation")
        self.assertEqual(inst.text.status, "generated")
    
    def testOrganization3(self):
        inst = self.instantiate_from("organization-example-gastro.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization3(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization3(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implOrganization3(self, inst):
        self.assertEqual(inst.id, "1")
        self.assertEqual(inst.identifier[0].system, "http://www.acme.org.au/units")
        self.assertEqual(inst.identifier[0].value, "Gastro")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "Gastroenterology")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "mobile")
        self.assertEqual(inst.telecom[0].value, "+1 555 234 3523")
        self.assertEqual(inst.telecom[1].system, "email")
        self.assertEqual(inst.telecom[1].use, "work")
        self.assertEqual(inst.telecom[1].value, "gastro@acme.org")
        self.assertEqual(inst.text.status, "generated")
    
    def testOrganization4(self):
        inst = self.instantiate_from("organization-example-mihealth.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization4(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization4(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implOrganization4(self, inst):
        self.assertEqual(inst.alias[0], "Michigan State Department of Health")
        self.assertEqual(inst.id, "3")
        self.assertEqual(inst.identifier[0].system, "http://michigan.gov/state-dept-ids")
        self.assertEqual(inst.identifier[0].value, "25")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "Michigan Health")
        self.assertEqual(inst.text.status, "generated")
    
    def testOrganization5(self):
        inst = self.instantiate_from("organization-example-lab.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization5(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization5(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implOrganization5(self, inst):
        self.assertEqual(inst.id, "1832473e-2fe0-452d-abe9-3cdb9879522f")
        self.assertEqual(inst.identifier[0].system, "http://www.acme.org.au/units")
        self.assertEqual(inst.identifier[0].value, "ClinLab")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "Clinical Lab")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "+1 555 234 1234")
        self.assertEqual(inst.telecom[1].system, "email")
        self.assertEqual(inst.telecom[1].use, "work")
        self.assertEqual(inst.telecom[1].value, "contact@labs.acme.org")
        self.assertEqual(inst.text.status, "generated")
    
    def testOrganization6(self):
        inst = self.instantiate_from("organization-example-f002-burgers-card.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization6(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization6(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implOrganization6(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].line[0], "South Wing, floor 2")
        self.assertEqual(inst.contact[0].address.line[0], "South Wing, floor 2")
        self.assertEqual(inst.contact[0].name.text, "mevr. D. de Haan")
        self.assertEqual(inst.contact[0].purpose.coding[0].code, "ADMIN")
        self.assertEqual(inst.contact[0].purpose.coding[0].system, "http://terminology.hl7.org/CodeSystem/contactentity-type")
        self.assertEqual(inst.contact[0].telecom[0].system, "phone")
        self.assertEqual(inst.contact[0].telecom[0].value, "022-655 2321")
        self.assertEqual(inst.contact[0].telecom[1].system, "email")
        self.assertEqual(inst.contact[0].telecom[1].value, "cardio@burgersumc.nl")
        self.assertEqual(inst.contact[0].telecom[2].system, "fax")
        self.assertEqual(inst.contact[0].telecom[2].value, "022-655 2322")
        self.assertEqual(inst.id, "f002")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "Burgers UMC Cardiology unit")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].value, "022-655 2320")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "dept")
        self.assertEqual(inst.type[0].coding[0].display, "Hospital Department")
        self.assertEqual(inst.type[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/organization-type")
    
    def testOrganization7(self):
        inst = self.instantiate_from("organization-example-f201-aumc.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization7(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization7(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implOrganization7(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].city, "Den Helder")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Walvisbaai 3")
        self.assertEqual(inst.address[0].postalCode, "2333ZA")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.contact[0].address.city, "Den helder")
        self.assertEqual(inst.contact[0].address.country, "NLD")
        self.assertEqual(inst.contact[0].address.line[0], "Walvisbaai 3")
        self.assertEqual(inst.contact[0].address.line[1], "Gebouw 2")
        self.assertEqual(inst.contact[0].address.postalCode, "2333ZA")
        self.assertEqual(inst.contact[0].name.family, "Brand")
        self.assertEqual(inst.contact[0].name.given[0], "Ronald")
        self.assertEqual(inst.contact[0].name.prefix[0], "Prof.Dr.")
        self.assertEqual(inst.contact[0].name.text, "Professor Brand")
        self.assertEqual(inst.contact[0].name.use, "official")
        self.assertEqual(inst.contact[0].telecom[0].system, "phone")
        self.assertEqual(inst.contact[0].telecom[0].use, "work")
        self.assertEqual(inst.contact[0].telecom[0].value, "+31715269702")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.identifier[0].system, "http://www.zorgkaartnederland.nl/")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "Artis University Medical Center")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "Artis University Medical Center (AUMC)")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "+31715269111")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "405608006")
        self.assertEqual(inst.type[0].coding[0].display, "Academic Medical Center")
        self.assertEqual(inst.type[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.type[0].coding[1].code, "V6")
        self.assertEqual(inst.type[0].coding[1].display, "University Medical Hospital")
        self.assertEqual(inst.type[0].coding[1].system, "urn:oid:2.16.840.1.113883.2.4.15.1060")
        self.assertEqual(inst.type[0].coding[2].code, "prov")
        self.assertEqual(inst.type[0].coding[2].display, "Healthcare Provider")
        self.assertEqual(inst.type[0].coding[2].system, "http://terminology.hl7.org/CodeSystem/organization-type")
    
    def testOrganization8(self):
        inst = self.instantiate_from("organization-example-good-health-care.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization8(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization8(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implOrganization8(self, inst):
        self.assertEqual(inst.id, "2.16.840.1.113883.19.5")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value, "2.16.840.1.113883.19.5")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "Good Health Clinic")
        self.assertEqual(inst.text.status, "generated")
    
    def testOrganization9(self):
        inst = self.instantiate_from("organization-example-f001-burgers.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization9(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization9(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implOrganization9(self, inst):
        self.assertEqual(inst.address[0].city, "Den Burg")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Galapagosweg 91")
        self.assertEqual(inst.address[0].postalCode, "9105 PZ")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.address[1].city, "Den Burg")
        self.assertEqual(inst.address[1].country, "NLD")
        self.assertEqual(inst.address[1].line[0], "PO Box 2311")
        self.assertEqual(inst.address[1].postalCode, "9100 AA")
        self.assertEqual(inst.address[1].use, "work")
        self.assertEqual(inst.contact[0].purpose.coding[0].code, "PRESS")
        self.assertEqual(inst.contact[0].purpose.coding[0].system, "http://terminology.hl7.org/CodeSystem/contactentity-type")
        self.assertEqual(inst.contact[0].telecom[0].system, "phone")
        self.assertEqual(inst.contact[0].telecom[0].value, "022-655 2334")
        self.assertEqual(inst.contact[1].purpose.coding[0].code, "PATINF")
        self.assertEqual(inst.contact[1].purpose.coding[0].system, "http://terminology.hl7.org/CodeSystem/contactentity-type")
        self.assertEqual(inst.contact[1].telecom[0].system, "phone")
        self.assertEqual(inst.contact[1].telecom[0].value, "022-655 2335")
        self.assertEqual(inst.id, "f001")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.528.1")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "91654")
        self.assertEqual(inst.identifier[1].system, "urn:oid:2.16.840.1.113883.2.4.6.1")
        self.assertEqual(inst.identifier[1].use, "usual")
        self.assertEqual(inst.identifier[1].value, "17-0112278")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "Burgers University Medical Center")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "022-655 2300")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "V6")
        self.assertEqual(inst.type[0].coding[0].display, "University Medical Hospital")
        self.assertEqual(inst.type[0].coding[0].system, "urn:oid:2.16.840.1.113883.2.4.15.1060")
        self.assertEqual(inst.type[0].coding[1].code, "prov")
        self.assertEqual(inst.type[0].coding[1].display, "Healthcare Provider")
        self.assertEqual(inst.type[0].coding[1].system, "http://terminology.hl7.org/CodeSystem/organization-type")
    
    def testOrganization10(self):
        inst = self.instantiate_from("organization-example-insurer.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization10(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization10(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implOrganization10(self, inst):
        self.assertEqual(inst.alias[0], "ABC Insurance")
        self.assertEqual(inst.id, "2")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.840.1.113883.3.19.2.3")
        self.assertEqual(inst.identifier[0].value, "666666")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "XYZ Insurance")
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