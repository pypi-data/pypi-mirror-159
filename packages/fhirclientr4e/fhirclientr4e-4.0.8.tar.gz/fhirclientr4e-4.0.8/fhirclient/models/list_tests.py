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

from . import list

from .fhirdate import FHIRDate
import logging


class ListTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("List", js["resourceType"])
        return list.List(js)
    
    def testList1(self):
        inst = self.instantiate_from("list-example-medlist.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList1(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList1(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implList1(self, inst):
        self.assertEqual(inst.code.coding[0].code, "182836005")
        self.assertEqual(inst.code.coding[0].display, "Review of medication")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Medication Review")
        self.assertEqual(inst.date.date, FHIRDate("2013-11-20T23:10:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2013-11-20T23:10:23+11:00")
        self.assertEqual(inst.entry[0].flag.coding[0].code, "01")
        self.assertEqual(inst.entry[0].flag.coding[0].display, "Prescribed")
        self.assertEqual(inst.entry[0].flag.coding[0].system, "http://nehta.gov.au/codes/medications/changetype")
        self.assertTrue(inst.entry[1].deleted)
        self.assertEqual(inst.entry[1].flag.coding[0].code, "02")
        self.assertEqual(inst.entry[1].flag.coding[0].display, "Cancelled")
        self.assertEqual(inst.entry[1].flag.coding[0].system, "http://nehta.gov.au/codes/medications/changetype")
        self.assertEqual(inst.id, "med-list")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode, "changes")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
    
    def testList2(self):
        inst = self.instantiate_from("list-example-familyhistory-genetics-profile-annie.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList2(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList2(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implList2(self, inst):
        self.assertEqual(inst.code.coding[0].code, "8670-2")
        self.assertEqual(inst.code.coding[0].display, "History of family member diseases")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.contained[0].id, "image")
        self.assertEqual(inst.contained[1].id, "1")
        self.assertEqual(inst.contained[2].id, "2")
        self.assertEqual(inst.contained[3].id, "3")
        self.assertEqual(inst.contained[4].id, "4")
        self.assertEqual(inst.contained[5].id, "5")
        self.assertEqual(inst.contained[6].id, "6")
        self.assertEqual(inst.contained[7].id, "7")
        self.assertEqual(inst.contained[8].id, "8")
        self.assertEqual(inst.contained[9].id, "9")
        self.assertEqual(inst.id, "prognosis")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode, "snapshot")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
    
    def testList3(self):
        inst = self.instantiate_from("list-example-simple-empty.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList3(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList3(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implList3(self, inst):
        self.assertEqual(inst.code.coding[0].code, "346638")
        self.assertEqual(inst.code.coding[0].display, "Patient Admission List")
        self.assertEqual(inst.code.coding[0].system, "http://acme.com/list-codes")
        self.assertEqual(inst.date.date, FHIRDate("2016-07-14T11:54:05+10:00").date)
        self.assertEqual(inst.date.as_json(), "2016-07-14T11:54:05+10:00")
        self.assertEqual(inst.id, "example-simple-empty")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode, "snapshot")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
    
    def testList4(self):
        inst = self.instantiate_from("list-example-empty.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList4(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList4(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implList4(self, inst):
        self.assertEqual(inst.code.coding[0].code, "182836005")
        self.assertEqual(inst.code.coding[0].display, "Review of medication")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Medication Review")
        self.assertEqual(inst.date.date, FHIRDate("2012-11-26T07:30:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2012-11-26T07:30:23+11:00")
        self.assertEqual(inst.emptyReason.coding[0].code, "nilknown")
        self.assertEqual(inst.emptyReason.coding[0].display, "Nil Known")
        self.assertEqual(inst.emptyReason.coding[0].system, "http://terminology.hl7.org/CodeSystem/list-empty-reason")
        self.assertEqual(inst.emptyReason.text, "The patient is not on any medications")
        self.assertEqual(inst.id, "example-empty")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode, "snapshot")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
    
    def testList5(self):
        inst = self.instantiate_from("list-example-familyhistory-genetics-profile.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList5(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList5(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implList5(self, inst):
        self.assertEqual(inst.code.coding[0].code, "8670-2")
        self.assertEqual(inst.code.coding[0].display, "History of family member diseases")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.contained[0].id, "1")
        self.assertEqual(inst.contained[1].id, "2")
        self.assertEqual(inst.contained[2].id, "3")
        self.assertEqual(inst.contained[3].id, "4")
        self.assertEqual(inst.contained[4].id, "5")
        self.assertEqual(inst.contained[5].id, "6")
        self.assertEqual(inst.contained[6].id, "7")
        self.assertEqual(inst.contained[7].id, "8")
        self.assertEqual(inst.id, "genetic")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode, "snapshot")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
    
    def testList6(self):
        inst = self.instantiate_from("list-example-familyhistory-f201-roel.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList6(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList6(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implList6(self, inst):
        self.assertEqual(inst.code.coding[0].code, "8670-2")
        self.assertEqual(inst.code.coding[0].display, "History of family member diseases")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.contained[0].id, "fmh-1")
        self.assertEqual(inst.contained[1].id, "fmh-2")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode, "snapshot")
        self.assertEqual(inst.note[0].text, "Both parents, both brothers and both children (twin) are still alive.")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
    
    def testList7(self):
        inst = self.instantiate_from("list-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList7(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList7(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implList7(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2012-11-25T22:17:00+11:00").date)
        self.assertEqual(inst.date.as_json(), "2012-11-25T22:17:00+11:00")
        self.assertTrue(inst.entry[0].deleted)
        self.assertEqual(inst.entry[0].flag.text, "Deleted due to error")
        self.assertEqual(inst.entry[1].flag.text, "Added")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "urn:uuid:a9fcea7c-fcdf-4d17-a5e0-f26dda030b59")
        self.assertEqual(inst.identifier[0].value, "23974652")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode, "changes")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
    
    def testList8(self):
        inst = self.instantiate_from("list-example-allergies.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList8(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList8(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implList8(self, inst):
        self.assertEqual(inst.code.coding[0].code, "52472-8")
        self.assertEqual(inst.code.coding[0].display, "Allergies and Adverse Drug Reactions")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Current Allergy List")
        self.assertEqual(inst.date.date, FHIRDate("2015-07-14T23:10:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2015-07-14T23:10:23+11:00")
        self.assertEqual(inst.id, "current-allergies")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode, "working")
        self.assertEqual(inst.orderedBy.coding[0].code, "entry-date")
        self.assertEqual(inst.orderedBy.coding[0].system, "http://terminology.hl7.org/CodeSystem/list-order")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Current Allergy List")
    
    def testList9(self):
        inst = self.instantiate_from("list-example-double-cousin-relationship-pedigree.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList9(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList9(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implList9(self, inst):
        self.assertEqual(inst.code.coding[0].code, "80738-8")
        self.assertEqual(inst.code.coding[0].display, "TPMT gene mutations found [Identifier] in Blood or Tissue by Sequencing Nominal")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "TPMT gene mutations found [Identifier] in Blood or Tissue by Sequencing Nominal")
        self.assertEqual(inst.contained[0].id, "1")
        self.assertEqual(inst.contained[1].id, "2")
        self.assertEqual(inst.contained[2].id, "3")
        self.assertEqual(inst.contained[3].id, "4")
        self.assertEqual(inst.contained[4].id, "5")
        self.assertEqual(inst.contained[5].id, "6")
        self.assertEqual(inst.id, "example-double-cousin-relationship")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode, "snapshot")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
    
    def testList10(self):
        inst = self.instantiate_from("list-example-long.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList10(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList10(inst2)
        self.evaluate_simplified_json(inst2)
        # should take a strict param
        js2 = inst.as_json(strict=False)

    def implList10(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2018-02-21T12:17:00+11:00").date)
        self.assertEqual(inst.date.as_json(), "2018-02-21T12:17:00+11:00")
        self.assertEqual(inst.id, "long")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode, "changes")
        self.assertEqual(inst.status, "current")
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