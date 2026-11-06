"""Tests for hf-upload's namespace check."""

from mcap_converter.cli.upload import allowed_namespaces


def test_allows_own_namespace_and_organizations():
    user_info = {"name": "someone", "orgs": [{"name": "Some-Org"}]}

    assert allowed_namespaces(user_info) == {"someone", "Some-Org"}


def test_allows_own_namespace_without_organizations():
    assert allowed_namespaces({"name": "someone"}) == {"someone"}
