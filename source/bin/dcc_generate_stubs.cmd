@ECHO OFF
SET PYTHONPATH=%~dp0..\;%PYTHONPATH%
python -m dcc_generate_stubs.cli %*