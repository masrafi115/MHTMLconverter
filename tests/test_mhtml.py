"""
"""

import mhtmlconverter.mhtml

import pathlib

import markdown

import shutil

def test_mhtml() -> None:
    """
        Test MHTML
    """
    out = pathlib.Path("./tests/resources/results/test_mhtml.html")
    outdir = pathlib.Path("./tests/resources/results/_resources")
    
    if out.exists():    out.unlink()
    if outdir.exists():
        shutil.rmtree(outdir.resolve())
    
    mhtmlconverter.mhtml.mhtml_to_html("./tests/resources/test_mhtml.mhtml","results/test_mhtml.html")

    assert(out.exists())

def test_mhtml_complex() -> None:
    """
        Test MHTML
    """
    out = pathlib.Path("./tests/resources/results/complex/test_mhtml.html")
    outdir = pathlib.Path("./tests/resources/results/complex/_resources")
    
    if out.exists():    out.unlink()
    if outdir.exists():
        shutil.rmtree(outdir.resolve())
    
    mhtmlconverter.mhtml.mhtml_to_html("./tests/resources/test_mhtml.mhtml","results/complex/test_mhtml.html")

    assert(out.exists())

def test_mhtml_relative() -> None:
    """
        Test MHTML
    """
    out = pathlib.Path("./tests/resources/results/test_relative/test_mhtml.html")
    outdir = pathlib.Path("./tests/resources/results/relative_resources")
    
    if out.exists():    out.unlink()
    if outdir.exists():
        shutil.rmtree(outdir.resolve())
    
    mhtmlconverter.mhtml.mhtml_to_html("./tests/resources/test_mhtml.mhtml","results/test_relative/test_mhtml.html","../relative_resources")

    assert(out.exists())