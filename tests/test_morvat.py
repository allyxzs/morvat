from morvat.tools.code_autopsy import perform_code_autopsy
from morvat.tools.security_scan import scan_security_risks


def test_autopsy_detects_bare_except_and_untyped_function():
    sample_code = """
def legacy_func(x):
    try:
        return x + 1
    except:
        pass
"""
    result = perform_code_autopsy(sample_code)
    assert result["valid_syntax"] is True
    assert result["stats"]["untyped_functions"] == 1
    assert result["stats"]["bare_excepts"] == 1
    assert result["entropy_score"] >= 28


def test_security_scanner_detects_hardcoded_key_and_eval():
    sample_code = """
password = "super_secret_password_123"
eval("2 + 2")
"""
    findings = scan_security_risks(sample_code)
    assert len(findings) == 2
