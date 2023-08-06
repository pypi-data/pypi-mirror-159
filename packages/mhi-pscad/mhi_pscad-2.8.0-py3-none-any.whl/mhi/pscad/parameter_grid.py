#===============================================================================
# Parameter Grid
#===============================================================================

"""
The PSCAD Parameter Grid Proxy Object
"""

#===============================================================================
# Imports
#===============================================================================

import logging

import mhi.common.path

from .project import Project

#===============================================================================
# Logging
#===============================================================================

LOG = logging.getLogger(__name__)

#===============================================================================
# Parameter Grid
#===============================================================================

class ParameterGrid:
    
    def __init__(self, pscad):
        self._pscad = pscad

    def view(self, subject):
        """
        Load subject into the parameter grid.

        The property grid is able to view and modify several components at
        once.

        If the subject is a component or component definition, all of the
        instances of that component are loaded into the parameter grid.

        If the subject is a project, all of the corresponding project types
        (libraries or cases) are loaded into the parameter grid.
        """
        self._pscad._param_grid(source=subject)

    def view_cases(self):
        """
        Load all project cases into the parameter grid.
        """
        self._pscad._param_grid(kind='Case')
        
    def view_libraries(self):
        """
        Load all libraries into the parameter grid.

        Note: The 'master' library is always omitted.
        """
        self._pscad._param_grid(kind='Library')

    def view_simulation_sets(self):
        """
        Load all simulation sets into the property grid.

        This allows for viewing / editing multiple simulation sets in the
        workspace at once.
        """
        self._pscad._param_grid(kind='SimSets')

    def view_simulation_tasks(self):
        """
        Load all simulation tasks into the property grid.

        This allows for viewing / editing multiple simulation tasks in the
        workspace at once.
        """
        self._pscad._param_grid(kind='SimSetTasks')

    def view_simulation_task_overrides(self):
        """
        Load simulation tasks’ project overrides into the property grid.

        This allows for viewing / editing multiple sets of project overrides
        in the workspace at once.
        """
        self._pscad._param_grid(kind='SimSetTaskOverrides')

    def view_simulation_task_layers(self, scope):
        """
        Load simulation tasks’ layers configurations into the property grid.

        This allows for viewing / editing multiple sets of layers
        configurations in the workspace at once.
        """

        if isinstance(scope, Project):
            prj = scope
            namespace = prj.name
        elif isinstance(scope, str):
            namespace = scope
        else:
            raise TypeError("Expected project or string")
        
        self._pscad._param_grid(kind='SimSetTaskLayers', namespace=namespace)

    def save(self, filename: str, folder: str = None) -> None:
        """
        Write parameter grid to a CSV file.

        Parameters:
            filename (str): Filename of the CSV file to write.
            folder (str): Directory where the CSV file will be stored (optional)
        """

        filename = mhi.common.path.expand_path(filename, abspath=True,
                                               folder=folder)

        LOG.info("%s: Save parameter grid to '%s'", self, filename)

        return self._pscad._param_grid_save(filename)
    
    def load(self, filename: str, folder: str = None) -> None:
        """
        Load parameter grid from a CSV file.

        Parameters:
            filename (str): Filename of the CSV file to read.
            folder (str): Directory to read the CSV file from (optional)
        """

        filename = mhi.common.path.expand_path(filename, abspath=True,
                                               folder=folder)

        LOG.info("%s: Load parameter grid from '%s'", self, filename)

        return self._pscad._param_grid_load(filename)

        
