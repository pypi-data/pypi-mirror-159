#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Dosage) on 2022-07-13.
#  2022, SMART Health IT.


from . import backboneelement

class Dosage(backboneelement.BackboneElement):
    """ How the medication is/was taken or should be taken.
    
    Indicates how the medication is/was taken or should be taken by the
    patient.
    """

    _attribute_docstrings = {}
    """ Dictionary of attribute documentation."""
    _attribute_docstrings['sequence'] = """The order of the dosage instructions."""
    _attribute_docstrings['text'] = """Free text dosage instructions e.g. SIG."""
    _attribute_docstrings['additionalInstruction'] = """Supplemental instruction or warnings to the patient - e.g. "with meals", "may cause drowsiness"."""
    _attribute_docstrings['patientInstruction'] = """Patient or consumer oriented instructions."""
    _attribute_docstrings['timing'] = """When medication should be administered."""
    _attribute_docstrings['asNeededBoolean'] = """Take "as needed" (for x)."""
    _attribute_docstrings['asNeededCodeableConcept'] = """Take "as needed" (for x)."""
    _attribute_docstrings['site'] = """Body site to administer to."""
    _attribute_docstrings['route'] = """How drug should enter body."""
    _attribute_docstrings['method'] = """Technique for administering medication."""
    _attribute_docstrings['doseAndRate'] = """Amount of medication administered."""
    _attribute_docstrings['maxDosePerPeriod'] = """Upper limit on medication per unit of time."""
    _attribute_docstrings['maxDosePerAdministration'] = """Upper limit on medication per administration."""
    _attribute_docstrings['maxDosePerLifetime'] = """Upper limit on medication per lifetime of the patient."""

    @classmethod
    def attribute_docstrings(cls):
        """Get dict of attributes docstrings."""
        return cls._attribute_docstrings

    _attribute_enums = {}
    """ Dictionary of enum configuration."""

    @classmethod
    def attribute_enums(cls):
        """Get dict of attributes with enums, Code or CodeableConcept."""
        return cls._attribute_enums

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.sequence = None
        """ The order of the dosage instructions.
        Type `int`. """
        
        self.text = None
        """ Free text dosage instructions e.g. SIG.
        Type `str`. """
        
        self.additionalInstruction = None
        """ Supplemental instruction or warnings to the patient - e.g. "with
        meals", "may cause drowsiness".
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.patientInstruction = None
        """ Patient or consumer oriented instructions.
        Type `str`. """
        
        self.timing = None
        """ When medication should be administered.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.asNeededBoolean = None
        """ Take "as needed" (for x).
        Type `bool`. """
        
        self.asNeededCodeableConcept = None
        """ Take "as needed" (for x).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.site = None
        """ Body site to administer to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.route = None
        """ How drug should enter body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.method = None
        """ Technique for administering medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doseAndRate = None
        """ Amount of medication administered.
        List of `DosageDoseAndRate` items (represented as `dict` in JSON). """
        
        self.maxDosePerPeriod = None
        """ Upper limit on medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.maxDosePerAdministration = None
        """ Upper limit on medication per administration.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxDosePerLifetime = None
        """ Upper limit on medication per lifetime of the patient.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(Dosage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Dosage, self).elementProperties()
        js.extend([
            ("sequence", "sequence", int, False, None, False),
            ("text", "text", str, False, None, False),
            ("additionalInstruction", "additionalInstruction", codeableconcept.CodeableConcept, True, None, False),
            ("patientInstruction", "patientInstruction", str, False, None, False),
            ("timing", "timing", timing.Timing, False, None, False),
            ("asNeededBoolean", "asNeededBoolean", bool, False, "asNeeded", False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False, "asNeeded", False),
            ("site", "site", codeableconcept.CodeableConcept, False, None, False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("doseAndRate", "doseAndRate", DosageDoseAndRate, True, None, False),
            ("maxDosePerPeriod", "maxDosePerPeriod", ratio.Ratio, False, None, False),
            ("maxDosePerAdministration", "maxDosePerAdministration", quantity.Quantity, False, None, False),
            ("maxDosePerLifetime", "maxDosePerLifetime", quantity.Quantity, False, None, False),
        ])
        return js


from . import element

class DosageDoseAndRate(element.Element):
    """ Amount of medication administered.
    
    The amount of medication administered.
    """

    _attribute_docstrings = {}
    """ Dictionary of attribute documentation."""
    _attribute_docstrings['type'] = """The kind of dose or rate specified, for example, ordered or calculated."""
    _attribute_docstrings['doseRange'] = """Amount of medication per dose."""
    _attribute_docstrings['doseQuantity'] = """Amount of medication per dose."""
    _attribute_docstrings['rateRatio'] = """Amount of medication per unit of time."""
    _attribute_docstrings['rateRange'] = """Amount of medication per unit of time."""
    _attribute_docstrings['rateQuantity'] = """Amount of medication per unit of time."""

    @classmethod
    def attribute_docstrings(cls):
        """Get dict of attributes docstrings."""
        return cls._attribute_docstrings

    _attribute_enums = {}
    """ Dictionary of enum configuration."""
    _attribute_enums['type'] = {
        'url': 'http://terminology.hl7.org/CodeSystem/dose-rate-type',
        'restricted_to': ['calculated', 'ordered'],
        'binding_strength': 'example',
        'class_name': 'CodeableConcept'
    }

    @classmethod
    def attribute_enums(cls):
        """Get dict of attributes with enums, Code or CodeableConcept."""
        return cls._attribute_enums

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ The kind of dose or rate specified, for example, ordered or
        calculated.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doseRange = None
        """ Amount of medication per dose.
        Type `Range` (represented as `dict` in JSON). """
        
        self.doseQuantity = None
        """ Amount of medication per dose.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.rateRatio = None
        """ Amount of medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.rateRange = None
        """ Amount of medication per unit of time.
        Type `Range` (represented as `dict` in JSON). """
        
        self.rateQuantity = None
        """ Amount of medication per unit of time.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(DosageDoseAndRate, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DosageDoseAndRate, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("doseRange", "doseRange", range.Range, False, "dose", False),
            ("doseQuantity", "doseQuantity", quantity.Quantity, False, "dose", False),
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False),
            ("rateRange", "rateRange", range.Range, False, "rate", False),
            ("rateQuantity", "rateQuantity", quantity.Quantity, False, "rate", False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
