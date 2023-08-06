@ECHO OFF

REM Script to execute publishing
REM See https://flit.pypa.io/en/latest/cmdline.html#flit-publish

flit publish --pypirc .\.pypirc
