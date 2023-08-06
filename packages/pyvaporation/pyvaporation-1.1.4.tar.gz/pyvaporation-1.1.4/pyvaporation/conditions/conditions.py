import typing

import attr
import numpy

from ..mixtures import Composition


# TODO: Enum or not Enum?
class CalculationType:
    polynomial: str = "polynomial"
    exponential: str = "exponential"
    logarithmic: str = "logarithmic"


@attr.s(auto_attribs=True)
class TemperatureProgram:
    coefficients: typing.List[float]
    type: str = CalculationType.polynomial

    def polynomial(self, x: float) -> float:
        """
        Calculates temperature using polynomial approximation
        :param x: parameter used for calculation of temperature
        :return: Temperature value calculated using polynomial relation defined with .coefficients
        """
        return sum(
            [self.coefficients[i] * x**i for i in range(len(self.coefficients))]
        )

    def exponential(self, x: float) -> float:
        """
        Calculates temperature using exponential approximation
        :param x: parameter used for calculation of temperature
        :return: Temperature value calculated using exponential-polynomial relation defined with .coefficients
        """
        return self.coefficients[0] * numpy.exp(
            sum(
                [
                    self.coefficients[i] * x ** (i - 1)
                    for i in range(1, len(self.coefficients))
                ]
            )
        )

    def logarithmic(self, x: float) -> float:
        """
        Calculates temperature using logarithmic approximation
        :param x: parameter used for calculation of temperature
        :return: Temperature value calculated using logarithmic-polynomial relation defined with .coefficients
        """
        return self.coefficients[0] * numpy.log(
            sum(
                [
                    self.coefficients[i] * x ** (i - 1)
                    for i in range(1, len(self.coefficients))
                ]
            )
        )

    def program(self, time):
        """
        Calculation of the Temperature based on a given temperature program
        :param time - time in hours
        :return - Temperature in K
        """
        return getattr(self, self.type)(time)


@attr.s(auto_attribs=True)
class Conditions:
    """
    A class for specification initial conditions for modelling of the test_pervaporation processes
    """

    membrane_area: float
    initial_feed_temperature: float
    initial_feed_amount: float
    initial_feed_composition: Composition
    permeate_temperature: typing.Optional[float] = None
    permeate_pressure: typing.Optional[float] = None
    temperature_program: typing.Optional[TemperatureProgram] = None
