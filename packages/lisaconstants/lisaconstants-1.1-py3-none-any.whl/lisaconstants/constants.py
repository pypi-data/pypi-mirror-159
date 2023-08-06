#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LISA Python Constants.

This module provides values sanctioned by the LISA Consortium for physical constants and mission parameters.

LISA Python Constants is intended to be consistently used by other pieces of software related to the simulation of
the instrument, of gravitational wave signals, and others.

Authors:
    Jean-Baptiste Bayle <j2b.bayle@gmail.com>
    Aurelien Hees <aurelien.hees@obspm.fr>
    Maude Lejeune <lejeune@apc.in2p3.fr>
"""

class Constant:
    """Defines a constant with associated metadata.

    Attributes:
        ALL: dictionary of all constants
    """

    ALL = {}

    @classmethod
    def alias(cls, name, original):
        """Give an existing constant an alias name.

        Args:
            name: alias name
            original: original name
        """
        cls.ALL[name] = cls.ALL[original]

    def __init__(self, name, value, unit, description, error=None, references=None):
        """Initialize a constant with attributes.

        Args:
            name: constant name
            value: constant value
            unit: associated unit, or None
            description: description
            error: uncertainty on value, or None
            references: list of references, or None
        """
        self.name = str(name)
        self.value = value
        self.description = str(description)
        self.unit = unit
        self.error = error

        if references is None:
            self.references = []
        elif isinstance(references, str):
            self.references = [references]
        else:
            self.references = references

        # Add to list of defined constants
        self.ALL[name] = self

    def __repr__(self):
        if self.unit is None:
            return f'<{self.name} ({self.value})>'
        return f'<{self.name} ({self.value} {self.unit})'


Constant('SPEED_OF_LIGHT',
    value=299792458.0,
    unit='m s^{-1}',
    description="Speed of light in a vacuum",
    error='Exact',
    references=[
        "P.J. Mohr, B.N. Taylor, D.B. Newell, 9 July 2015, 'The 2014 CODATA Recommended Values of the Fundamental"
        "Physical Constants', National Institute of Standards and Technology, Gaithersburg, MD 20899-8401;"
        "http://www.codata.org/",
        "http://physics.nist.gov/constants (Web Version 7.0). See also the IAU (2009) System of Astronomical Constants"
        "(IAU, August 2009, 'IAU 2009 Astronomical Constants', IAU 2009 Resolution B2 adopted at the XXVII-th General"
        "Assembly of the IAU. See also IAU, 10 August 2009, 'IAU WG on NSFA Current Best Estimates',"
        "http://maia.usno.navy.mil/NSFA/NSFA_cbe.html)",
    ],
)

Constant.alias('c', 'SPEED_OF_LIGHT')

Constant('SIDEREALYEAR_J2000DAY',
    value=365.256363004,
    unit='day',
    description="Number of days per sidereal year",
    references=[
        "J.L. Simon, P. Bretagnon, J. Chapront, M. Chapront-Touze, G. Francou, J. Laskar, 1994,"
        "'Numerical expressions for precession formulae and mean elements for the Moon and the planets',"
        "A&A, 282, 663 (1994A&A...282..663S)",
    ],
)

Constant('TROPICALYEAR_J2000DAY',
    value=365.242190402,
    unit='day',
    description="Number of days per tropical year",
    references=[
        "J.L. Simon, P. Bretagnon, J. Chapront, M. Chapront-Touze, G. Francou, J. Laskar, 1994,"
        "'Numerical expressions for precession formulae and mean elements for the Moon and the planets',"
        "A&A, 282, 663 (1994A&A...282..663S)",
    ],
)

Constant('ASTRONOMICAL_YEAR',
    value=Constant.ALL["SIDEREALYEAR_J2000DAY"].value * 60 * 60 * 24,
    unit='s',
    description="Astronomical year",
    references=[
        "J.L. Simon, P. Bretagnon, J. Chapront, M. Chapront-Touze, G. Francou, J. Laskar, 1994,"
        "'Numerical expressions for precession formulae and mean elements for the Moon and the planets',"
        "A&A, 282, 663 (1994A&A...282..663S)",
    ],
)

Constant('ASTRONOMICAL_UNIT',
    value=149597870700.0,
    unit='m',
    description="Astronomical unit",
    references=[
        "IAU, August 2012, 'Re-definition of the astronomical unit of length',"
        "IAU 2012 Resolution B2 adopted at the XXVIII-th General Assembly of the IAU",
    ],
)

Constant.alias('au', 'ASTRONOMICAL_UNIT')

Constant("GM_SUN",
    value=1.327124400419394e+20,
    unit='m^3 s^{-2}',
    description="Sun gravitational parameter",
    references=[
        "Table 8 from http://ipnpr.jpl.nasa.gov/progress_report/42-196/196C.pdf",
    ],
)

Constant("SUN_SCHWARZSCHILD_RADIUS",
    value=2 * Constant.ALL["GM_SUN"].value / Constant.ALL["c"].value**2,
    unit='m',
    description="Sun Schwarzschild radius",
)

Constant("PARSEC_METER",
    value=3.0856775814913674e+16,
    unit='m',
    description="Parsec expressed in meters",
)

Constant("NEWTON_CONSTANT",
    value=6.674080e-11,
    unit='m^3 kg^{-1} s^{-2}',
    description="Newton's universal constant of gravitation",
    references=[
        "P.J. Mohr, B.N. Taylor, D.B. Newell, 9 July 2015, 'The 2014 CODATA Recommended Values of the Fundamental"
        "Physical Constants', National Institute of Standards and Technology, Gaithersburg, MD 20899-8401;"
        "http://www.codata.org/",
        "http://physics.nist.gov/constants (Web Version 7.0). See also the IAU (2009) System of Astronomical Constants"
        "(IAU, August 2009, 'IAU 2009 Astronomical Constants', IAU 2009 Resolution B2 adopted at the XXVII-th General"
        "Assembly of the IAU. See also IAU, 10 August 2009, 'IAU WG on NSFA Current Best Estimates',"
        "http://maia.usno.navy.mil/NSFA/NSFA_cbe.html)",
    ],
)

Constant("SUN_MASS",
    value=1.98848e+30,
    unit='kg',
    description="Solar mass",
)

Constant("ELEMENTARY_CHARGE",
    value=1.602176634E-19,
    unit='C',
    description="The elementary charge is the electric charge carried by a single proton or, "
    "equivalently, the magnitude of the negative electric charge carried by a single electron.",
    error='Exact',
    references=[
        "2018 CODATA Value: elementary charge. The NIST Reference on Constants, Units, and Uncertainty. "
        "NIST. 20 May 2019. Retrieved 2019-05-20.",
    ],
)

Constant.alias('e', "ELEMENTARY_CHARGE")

Constant("BOLTZMANN_CONSTANT",
    value=1.380649E-23,
    unit='J K^{-1}',
    description="The Boltzmann constant is the proportionality factor that relates the average "
    "relative kinetic energy of particles in a gas with the thermodynamic temperature of the gas.",
    error='Exact',
    references=[
        "2018 CODATA Value: Boltzmann constant. The NIST Reference on Constants, Units, and Uncertainty. "
        "NIST. 20 May 2019. Retrieved 20 May 2019.",
    ],
)

Constant.alias('Kb', "BOLTZMANN_CONSTANT")

Constant("STEFAN_BOLTZMANN_CONSTANT",
    value=5.670374419184429453970E-8,
    unit='kg s^{-3} K^{-4}',
    description="The Stefan-Boltzmann constant is the constant of proportionality in the Stefan–Boltzmann "
    "law: 'the total intensity radiated over all wavelengths increases as the temperature increases', "
    "of a black body which is proportional to the fourth power of the thermodynamic temperature.",
    error='Exact (numerical approximation)',
    references=[
         "2018 CODATA Value: Stefan–Boltzmann constant. The NIST Reference on Constants, Units, and Uncertainty. "
         "NIST. 20 May 2019. Retrieved 2019-05-20.",
    ],
)

Constant("VACUUM_PERMEABILITY",
    value=1.25663706143592E-06,
    unit='kg m s^{-2} A^{-2}',
    description="Vacuum permeability is the magnetic permeability in a classical vacuum.",
)


Constant("FUSED_SILICA_THERMAL_OPD",
    value=9.82E-6,
    unit='K^{-1}',
    description="Thermal optical path difference change of fused silica.",
)

Constant("FUSED_SILICAL_THERMAL_EXPANSION",
    value=5E-7,
    unit='K^{-1}',
    description="Thermal expansion of fused silica.",
)

Constant("CRYSTAL_QUARTZ_THERMAL_OPD",
    value=6.1E-7,
    unit='K^{-1}',
    description="Thermal optical path difference change of crystal quartz.",
)

Constant("ZERODUR_THERMAL_EXPANSION",
    value=2E-8,
    unit='K^{-1}',
    description="Thermal expansion of Zerodur.",
)

Constant("TITANIUM_THERMAL_EXPANSION",
    value=8.6E-6,
    unit='K^{-1}',
    description="Thermal expansion of titanium.",
)

Constant("GOLD_PLATINUM_THERMAL_EXPANSION",
    value=1.52E-5,
    unit='K^{-1}',
    description="Thermal expansion of gold-platinum.",
)

Constant("WATER_MOLECULAR_WEIGHT",
    value=2.99150711295358E-26,
    unit='kg',
    description="Molecular weight of water.",
)
