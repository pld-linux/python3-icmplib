%define		module	icmplib
Summary:	Modern implementation of the ICMP protocol in Python
Name:		python3-%{module}
Version:	3.0.3
Release:	1
License:	GPL v3+
Group:		Libraries/Python
Source0:	https://pypi.debian.net/icmplib/%{module}-%{version}.tar.gz
# Source0-md5:	44389ecd00494114d519296286b51fdf
URL:		https://pypi.org/project/icmplib/
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modern implementation of the ICMP protocol in Python.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
