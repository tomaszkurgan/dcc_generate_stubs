@ECHO OFF
SET PYTHONPATH=%~dp0..\;%PYTHONPATH%
python -m maya_generate_stubs.cli %*