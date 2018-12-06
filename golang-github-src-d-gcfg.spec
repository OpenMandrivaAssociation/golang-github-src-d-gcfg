%global goipath  github.com/src-d/gcfg
Version: 1.3.0

%global common_description %{expand:
Package gcfg reads "INI-style" text-based configuration files with "name=value"
pairs grouped into sections (gcfg files).

This is a fork of https://github.com/go-gcfg/gcfg .}

%gometa

Name: %{goname}
Release: 2%{?dist}
Summary: Read INI-style configuration files into Go structs
License: BSD
URL: %{gourl}
Source0: %{gosource}
BuildRequires: golang(github.com/pkg/errors)
BuildRequires: golang(gopkg.in/warnings.v0)

%description
%{common_description}

%package devel
Summary: %{summary}
BuildArch: noarch

%description devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%gosetup -q

%install
%goinstall

%check
%gochecks

%files devel -f devel.file-list
%license LICENSE
%doc README

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 05 2018 Dominik Mierzejewski <dominik@greysector.net> - 1.3.0-1
- use the release rather than the corresponding git commit

* Fri Mar 30 2018 Dominik Mierzejewski <dominik@greysector.net> - 0-0.1.20180330gitf187355
- First package for Fedora
