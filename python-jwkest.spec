%global         sum Python implementation of JWT, JWE, JWS and JWK
%global         uname pyjwkest

Name:           python-%{uname}
Version:        1.3.2
Release:        2%{?dist}
Summary:        %{sum}

URL:            https://github.com/rohe/pyjwkest
Source:         https://pypi.io/packages/source/p/%{uname}/%{uname}-%{version}.tar.gz
License:        Apache 2.0

BuildArch:      noarch

Buildrequires:  python-nose
Buildrequires:  python-setuptools
Buildrequires:  python2-devel
Buildrequires:  pytest

Requires:       python-crypto
Requires:       python-requests
Requires:       python-six
Requires:       python2-futures

%description
%{sum}.

%package -n python2-jwkest
Summary:        %{sum}

%description -n python2-jwkest
%{sum}.

%prep
%autosetup -n %{uname}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files -n python2-jwkest
%{python2_sitelib}/*
%{_bindir}/*

%changelog
* Thu Mar 2 2017 Nicolas Hicher <nhicher@redhat.com> - 1.3.2-2
- normalize spec file

* Wed Mar 1 2017 Nicolas Hicher <nhicher@redhat.com> - 1.3.2-1
- bump version for python-oic

* Tue Feb 24 2017 Nicolas Hicher <nhicher@redhat.com> - 1.0.1-1
- Initial packaging
