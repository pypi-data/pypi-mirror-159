"""
This module contains the base class for the different :py:class:`Analyzer` objects used by :py:mod:`kinisi`.
"""

# Copyright (c) Andrew R. McCluskey and Benjamin J. Morgan
# Distributed under the terms of the MIT License
# author: Andrew R. McCluskey (arm61)

from typing import Union, List
import numpy as np
from kinisi.parser import MDAnalysisParser, PymatgenParser


class Analyzer:
    """
    This class is the superclass for the :py:class:`kinisi.analyze.DiffusionAnalyzer`,
    :py:class:`kinisi.analyze.JumpDiffusionAnalyzer` and :py:class:`kinisi.analyze.ConductivityAnalyzer` classes.
    Therefore all of the properties here are available to these other classes.

    :param delta_t: An array of the timestep values.
    :param disp_3d: A list of arrays, where each array has the axes :code:`[atom, displacement observation,
        dimension]`. There is one array in the list for each delta_t value. Note: it is necessary to use a
        list of arrays as the number of observations is not necessary the same at each data point.
    :param volume: The volume of the simulation cell.
    """

    def __init__(self, delta_t: np.ndarray, disp_3d: List[np.ndarray], volume: float):
        self._delta_t = delta_t
        self._disp_3d = disp_3d
        self._volume = volume

    @classmethod
    def _from_pymatgen(cls,
                       trajectory: List[Union['pymatgen.core.structure.Structure',
                                              List['pymatgen.core.structure.Structure']]],
                       parser_params: dict,
                       dtype: str = None,
                       **kwargs):
        """
        Create a :py:class:`Analyzer` object from a list or nested list of
        :py:class:`pymatgen.core.structure.Structure` objects.

        :param trajectory: The list or nested list of structures to be analysed.
        :param parser_params: The parameters for the :py:class:`kinisi.parser.PymatgenParser` object.
            See the appropriate documentation for more guidance on this dictionary.
        :param dtype: If :py:attr:`trajectory` is a list of :py:class:`pymatgen.core.structure.Structure`
            objects, this should be :py:attr:`None`. However, if a list of lists is passed, then it is necessary
            to identify if these constitute a series of :py:attr:`consecutive` trajectories or a series of
            :py:attr:`identical` starting points with different random seeds, in which case the `dtype` should
            be either :py:attr:`consecutive` or :py:attr:`identical`.

        :return: Relevant :py:class:`Analyzer` object.
        """
        if dtype is None:
            u = PymatgenParser(trajectory, **parser_params)
            return cls(u.delta_t, u.disp_3d, u.volume, **kwargs)
        elif dtype == 'identical':
            u = [PymatgenParser(f, **parser_params) for f in trajectory]
            return cls(u[0].delta_t, cls._stack_trajectories(u), u[0].volume, **kwargs)
        elif dtype == 'consecutive':
            structures = _flatten_list([x for x in trajectory])
            u = PymatgenParser(structures, **parser_params)
            return cls(u.delta_t, u.disp_3d, u.volume, **kwargs)
        else:
            raise ValueError('The dtype specified was not recognised, please consult the kinisi documentation.')

    @classmethod
    def _from_Xdatcar(cls,
                      trajectory: Union['pymatgen.io.vasp.outputs.Xdatcar', List['pymatgen.io.vasp.outputs.Xdatcar']],
                      parser_params: dict,
                      dtype: str = None,
                      **kwargs):
        """
        Create a :py:class:`Analyzer` object from a single or a list of
        :py:class:`pymatgen.io.vasp.outputs.Xdatcar` objects.

        :param trajectory: The Xdatcar or list of Xdatcar objects to be analysed.
        :param parser_params: The parameters for the :py:class:`kinisi.parser.PymatgenParser` object. See the
            appropriate documentation for more guidance on this dictionary.
        :param dtype: If :py:attr:`trajectory` is a :py:class:`pymatgen.io.vasp.outputs.Xdatcar` object, this
            should be :py:attr:`None`. However, if a list of :py:class:`pymatgen.io.vasp.outputs.Xdatcar` objects is
            passed, then it is necessary to identify if these constitute a series of :py:attr:`consecutive`
            trajectories or a series of :py:attr:`identical` starting points with different random seeds, in which
            case the `dtype` should be either :py:attr:`consecutive` or :py:attr:`identical`.

        :return: Relevant :py:class:`Analyzer` object.
        """
        if dtype is None:
            structures = trajectory.structures
            u = PymatgenParser(structures, **parser_params)
            return cls(u.delta_t, u.disp_3d, u.volume, **kwargs)
        elif dtype == 'identical':
            u = [PymatgenParser(f.structures, **parser_params) for f in trajectory]
            return cls(u[0].delta_t, cls._stack_trajectories(u), u[0].volume, **kwargs)
        elif dtype == 'consecutive':
            structures = _flatten_list([x.structures for x in trajectory])
            u = PymatgenParser(structures, **parser_params)
            return cls(u.delta_t, u.disp_3d, u.volume, **kwargs)
        else:
            raise ValueError('The dtype specified was not recognised, please consult the kinisi documentation.')

    @classmethod
    def _from_file(cls, trajectory: Union[str, List[str]], parser_params: dict, dtype: str = None, **kwargs):
        """
        Create a :py:class:`Analyzer` object from a single or a list of Xdatcar file(s).

        :param trajectory: The file or list of Xdatcar files to be analysed.
        :param parser_params: The parameters for the :py:class:`kinisi.parser.PymatgenParser` object. See the
            appropriate documentation for more guidance on this dictionary.
        :param dtype: If :py:attr:`trajectory` is a single file, this should be :py:attr:`None`. However, if a
            list of files is passed, then it is necessary to identify if these constitute a series of
            :py:attr:`consecutive` trajectories or a series of :py:attr:`identical` starting points with different
            random seeds, in which case the `dtype` should be either :py:attr:`consecutive` or :py:attr:`identical`.

        :return: Relevant :py:class:`Analyzer` object.
        """
        try:
            from pymatgen.io.vasp import Xdatcar
        except ModuleNotFoundError:  # pragma: no cover
            raise ModuleNotFoundError("To use the from_file method, pymatgen must be installed.")  # pragma: no cover
        if dtype is None:
            structures = Xdatcar(trajectory).structures
            u = PymatgenParser(structures, **parser_params)
            return cls(u.delta_t, u.disp_3d, u.volume, **kwargs)
        elif dtype == 'identical':
            u = [PymatgenParser(Xdatcar(f).structures, **parser_params) for f in trajectory]
            return cls(u[0].delta_t, cls._stack_trajectories(u), u[0].volume, **kwargs)
        elif dtype == 'consecutive':
            trajectory_list = (Xdatcar(f) for f in trajectory)
            structures = _flatten_list([x.structures for x in trajectory_list])
            u = PymatgenParser(structures, **parser_params)
            return cls(u.delta_t, u.disp_3d, u.volume, **kwargs)
        else:
            raise ValueError('The dtype specified was not recognised, please consult the kinisi documentation.')

    @classmethod
    def _from_universe(cls,
                       trajectory: 'MDAnalysis.core.universe.Universe',
                       parser_params: dict,
                       dtype: str = None,
                       **kwargs):
        """
        Create an :py:class:`Analyzer` object from an :py:class:`MDAnalysis.core.universe.Universe` object.

        :param trajectory: The universe to be analysed.
        :param parser_params: The parameters for the :py:class:`kinisi.parser.MDAnalysisParser` object.
            See the appropriate documention for more guidance on this dictionary.
        :param dtype: If :py:attr:`trajectory` is a single file, this should be :py:attr:`None`. However, if a
            list of files is passed, then it is necessary to identify that these constitute a series of
            :py:attr:`identical` starting points with different random seeds, in which case the `dtype` should
            be :py:attr:`identical`. For a series of consecutive trajectories, please construct the relevant
            object using :py:mod:`MDAnalysis`.

        :return: Relevant :py:class:`Analyzer` object.
        """
        try:
            import MDAnalysis as mda
        except ModuleNotFoundError:  # pragma: no cover
            raise ModuleNotFoundError(
                "To use the MDAnalysis from file parsing, MDAnalysis must be installed.")  # pragma: no cover
        if dtype is None:
            u = MDAnalysisParser(trajectory, **parser_params)
            return cls(u.delta_t, u.disp_3d, u.volume, **kwargs)
        elif dtype == 'identical':
            u = [MDAnalysisParser(t, **parser_params) for t in trajectory]
            return cls(u[0].delta_t, cls._stack_trajectories(u), u[0].volume, **kwargs)
        else:
            raise ValueError('The dtype specified was not recognised, please consult the kinisi documentation.')

    @staticmethod
    def _stack_trajectories(u: Union[MDAnalysisParser, PymatgenParser]) -> List[np.ndarray]:
        """
        If more than one trajectory is given, then they are stacked to give the appearence that there are
        additional atoms in the trajectory.

        :param u: Results from the parsing of each trajectory.

        :return: The stacked displacement list.
        """
        joint_disp_3d = []
        for i in range(len(u[0].disp_3d)):
            disp = np.zeros((u[0].disp_3d[i].shape[0] * len(u), u[0].disp_3d[i].shape[1], u[0].disp_3d[i].shape[2]))
            disp[:u[0].disp_3d[i].shape[0]] = u[0].disp_3d[i]
            for j in range(1, len(u)):
                disp[u[0].disp_3d[i].shape[0] * j:u[0].disp_3d[i].shape[0] * (j + 1)] = u[j].disp_3d[i]
            joint_disp_3d.append(disp)
        return joint_disp_3d

    @property
    def dt(self) -> np.ndarray:
        """
        :return: Timestep values that have been sampled.
        """
        return self._diff.dt

    @property
    def dr(self) -> List['uravu.distribution.Distribution']:
        """
        :return: A list of :py:class:`uravu.distribution.Distribution` objects that describe the euclidian
            displacement at each :py:attr:`dt`.
        """
        return self._diff.euclidian_displacements

    @property
    def ngp_max(self) -> float:
        """
        :return: Position in dt where the non-Gaussian parameter is maximised.
        """
        return self.dt[self._diff.ngp.argmax()]

    @property
    def intercept(self) -> 'uravu.distribution.Distribution':
        """
        :return: The distribution describing the intercept.
        """
        return self._diff.intercept

    @property
    def volume(self) -> float:
        """
        :return: Volume of system, in cubic angstrom.
        """
        return self._volume


def _flatten_list(this_list: list) -> list:
    """
    Flatten nested lists.

    :param this_list: List to be flattened

    :return: Flattened list
    """
    return [item for sublist in this_list for item in sublist]
