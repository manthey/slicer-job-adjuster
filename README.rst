===================
Slicer Job Adjuster
===================

Adjust a Slicer CLI Web job before submission and after finish

This is an example Girder plugin that could modify a Slicer CLI Web job when it
is run.  Currently, it expects the tasks to already be uploaded when Girder
starts; it should hook into an event to bind to new tasks, too.

This was created using the Girder plugin cookie-cutter template.  Aside from
changes to __init__.py, the only other change was adding the slicer_cli_web
dependency to setup.py.
