import typing

import FreeCAD
import Part as PartModule


# ChFi2d_FilletAPIPy.xml
class FilletAPI(FreeCAD.PyObjectBase):
    """Algorithm that creates fillet edge"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: PartModule.Wire, arg2: PartModule.Plane, /): ...

    @typing.overload
    def __init__(self, arg1: PartModule.Edge, arg2: PartModule.Edge, arg3: PartModule.Plane, /):
        """
        Algorithm that creates fillet edge
        Possible exceptions: (TypeError).
        """

    @typing.overload
    def init(self, arg1: PartModule.Wire, arg2: PartModule.Plane, /): ...

    @typing.overload
    def init(self, arg1: PartModule.Edge, arg2: PartModule.Edge, arg3: PartModule.Plane, /):
        """
        Initializes a fillet algorithm: accepts a wire consisting of two edges in a plane
        Possible exceptions: (TypeError).
        """

    def numberOfResults(self, arg1: FreeCAD.Vector, /) -> int:
        """
        Returns number of possible solutions
        Possible exceptions: (FreeCAD.Base.CADKernelError).
        """

    def perform(self, radius: float, /) -> bool:
        """
        perform(radius) -> bool

        Constructs a fillet edge
        Possible exceptions: (FreeCAD.Base.CADKernelError).
        """

    def result(self, point: FreeCAD.Vector, solution: int = -1, /) -> tuple[typing.Any, typing.Any, typing.Any]:
        """
        result(point, solution=-1)

        Returns result (fillet edge, modified edge1, modified edge2)
        Possible exceptions: (FreeCAD.Base.CADKernelError).
        """


# ChFi2d_FilletAlgoPy.xml
class FilletAlgo(FreeCAD.PyObjectBase):
    """Algorithm that creates fillet edge"""

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: PartModule.Wire, arg2: PartModule.Plane, /): ...

    @typing.overload
    def __init__(self, arg1: PartModule.Edge, arg2: PartModule.Edge, arg3: PartModule.Plane, /):
        """
        Algorithm that creates fillet edge
        Possible exceptions: (TypeError).
        """

    @typing.overload
    def init(self, arg1: PartModule.Wire, arg2: PartModule.Plane, /): ...

    @typing.overload
    def init(self, arg1: PartModule.Edge, arg2: PartModule.Edge, arg3: PartModule.Plane, /):
        """
        Initializes a fillet algorithm: accepts a wire consisting of two edges in a plane
        Possible exceptions: (TypeError).
        """

    def numberOfResults(self, arg1: FreeCAD.Vector, /) -> int:
        """
        Returns number of possible solutions
        Possible exceptions: (FreeCAD.Base.CADKernelError).
        """

    def perform(self, radius: float, /) -> bool:
        """
        perform(radius) -> bool

        Constructs a fillet edge
        Possible exceptions: (FreeCAD.Base.CADKernelError).
        """

    def result(self, point: FreeCAD.Vector, solution: int = -1, /) -> tuple[typing.Any, typing.Any, typing.Any]:
        """
        result(point, solution=-1)

        Returns result (fillet edge, modified edge1, modified edge2)
        Possible exceptions: (FreeCAD.Base.CADKernelError).
        """


# ChFi2d_AnaFilletAlgoPy.xml
class AnaFilletAlgo(FreeCAD.PyObjectBase):
    """
    An analytical algorithm for calculation of the fillets.
    It is implemented for segments and arcs of circle only.
    """

    @typing.overload
    def __init__(self): ...

    @typing.overload
    def __init__(self, arg1: PartModule.Wire, arg2: PartModule.Plane, /): ...

    @typing.overload
    def __init__(self, arg1: PartModule.Edge, arg2: PartModule.Edge, arg3: PartModule.Plane, /):
        """
        An analytical algorithm for calculation of the fillets.
        It is implemented for segments and arcs of circle only.
        Possible exceptions: (TypeError).
        """

    @typing.overload
    def init(self, arg1: PartModule.Wire, arg2: PartModule.Plane, /): ...

    @typing.overload
    def init(self, arg1: PartModule.Edge, arg2: PartModule.Edge, arg3: PartModule.Plane, /):
        """
        Initializes a fillet algorithm: accepts a wire consisting of two edges in a plane
        Possible exceptions: (TypeError).
        """

    def perform(self, radius: float, /) -> bool:
        """
        perform(radius) -> bool

        Constructs a fillet edge
        Possible exceptions: (FreeCAD.Base.CADKernelError).
        """

    def result(self) -> tuple[typing.Any, typing.Any, typing.Any]:
        """
        result()

        Returns result (fillet edge, modified edge1, modified edge2)
        Possible exceptions: (FreeCAD.Base.CADKernelError).
        """


# ChFi2d_ChamferAPIPy.xml
class ChamferAPI(FreeCAD.PyObjectBase):
    """Algorithm that creates a chamfer between two linear edges"""

    @typing.overload
    def __init__(self, arg1: PartModule.Wire, /): ...

    @typing.overload
    def __init__(self, arg1: PartModule.Edge, arg2: PartModule.Edge, /):
        """
        Algorithm that creates a chamfer between two linear edges
        Possible exceptions: (TypeError).
        """

    @typing.overload
    def init(self, arg1: PartModule.Wire, /): ...

    @typing.overload
    def init(self, arg1: PartModule.Edge, arg2: PartModule.Edge, /):
        """
        Initializes a chamfer algorithm: accepts a wire consisting of two edges in a plane
        Possible exceptions: (TypeError).
        """

    def perform(self) -> bool:
        """
        perform(radius) -> bool

        Constructs a chamfer edge
        Possible exceptions: (FreeCAD.Base.CADKernelError).
        """

    def result(self, point: float, solution: float, /) -> tuple[typing.Any, typing.Any, typing.Any]:
        """
        result(point, solution=-1)

        Returns result (chamfer edge, modified edge1, modified edge2)
        Possible exceptions: (FreeCAD.Base.CADKernelError).
        """
