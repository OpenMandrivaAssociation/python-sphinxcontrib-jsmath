%define	module	sphinxcontrib-jsmath

Summary:	JavaScript Math rendering support for the Sphinx documentation generator
Name:		python-%{module}
Version:	1.0.1
Release:	7
Source0:	https://github.com/sphinx-doc/%{module}/archive/%{version}.tar.gz
Patch0:		jsmath-fix-bogus-versioning.patch
License:	ISC
Group:		Development/Python
Url:		https://sphinx-doc.org/
BuildArch:	noarch
BuildSystem:	python

%description
JavaScript Math rendering support for the Sphinx documentation generator

%files
%{py_puresitedir}/sphinxcontrib*
