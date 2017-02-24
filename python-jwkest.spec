%global         Python implementation of JWT, JWE, JWS and JWK
%global         uname pyjwkest

Name:           python-jwkest
Version:        1.0.1
Release:        1%{?dist}
Summary:        %{sum}

License:        Apache 2.0
URL:            https://github.com/rohe/pyjwkest
Source0:        https://pypi.python.org/packages/64/72/275288499e91cfea8ad21fdda17c0c41d449da69c822cb0aa7ebc6a1ca0b/%{uname}-%{version}.tar.gz

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
An incredibly simple HTTP basic auth implementation

%package -n python2-jwkest
Summary:        %{sum}

Buildrequires:  python-nose
Buildrequires:  python-setuptools
Buildrequires:  python2-devel
Buildrequires:  pytest
Requires:       python-crypto
Requires:       python-requests
Requires:       python-six
Requires:       python2-futures

%description -n python2-jwkest
An incredibly simple HTTP basic auth implementation

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
* Tue Feb 24 2017 Nicolas Hicher <nhicher@redhat.com> - 1.0.1-1
- Initial packaging
